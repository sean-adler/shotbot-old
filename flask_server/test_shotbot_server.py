from arduino import Arduino
from flask import Flask, render_template
from time import sleep
from utils import *
import os
import json

###########################
###    Arduino setup    ###
###########################

# Specify the Uno's port as an argument.

#uno = Arduino('/dev/tty.usbmodem621')

"""
================
PIN DECLARATIONS
================
(These vars are never used: Here for documentation only.)
whiskey = 0
tequila = 1
vodka = 2
gin = 3
orange_juice = 4
pineapple_juice = 5
cranberry_juice = 6
sour_mix = 7
"""

# Declare all output pins

#uno.output([0,1,2,3,4,5,6,7])

################################
###    Flask server setup    ###
################################

# Create server
app = Flask(__name__)

# Called if exception is raised
@app.teardown_request
def teardown_request(exception):
    #uno.turnOff()
    # placeholder return statement.
    return ''

# Route takes drink requests
@app.route('/pour/<ingredients>')
def prepare_request(ingredients):
    """
    Takes the 8-digit URL string and passes it to the recursive 'pour' function
    as a list of ints.
    """
    ingredientList = [int(n) for n in ingredients]
    # 2nd arg list: no pins are HIGH yet.
    pour(ingredientList, [])
    logPath = getLogPath()
    with open(logPath, "a") as log:
        log.write(ingredients)
        log.write("\n")
    # irrelevant return value.
    return ingredients

# Opens all required valves at once and closes them when necessary.
def pour(pinDurations, highPins):
    """
    Takes two lists of ints: pinDurations, which corresponds to
    pour times of each ingredient stored with ShotBot, and
    highPins, which keeps track of which pins are currently HIGH.
    Fires up the required Arduino pins immediately,
    powering down each when its ingredient is fully poured.
    """
    # Recurse until all ingredients are completely poured.
    if any(p for p in pinDurations if p > 0):
        for p in range(len(pinDurations)):
            if pinDurations[p] > 0 and p not in highPins:
                highPins.append(p)
                #uno.setHigh(p)
                print "Writing HIGH to Pin %d" % p
        # Leave pins high until at least one ingredient is completely poured.
        pour_time = min(p for p in pinDurations if p > 0)
        sleep(pour_time)
        # Update durations.
        newDurations = [(p-pour_time) for p in pinDurations]
        # Turn off pins whose ingredients are completely poured.
        for p in range(len(newDurations)):
            if newDurations[p] == 0:
                #uno.setLow(p)
                print "Writing LOW to Pin %d" % p
        # Recurse on adjusted list.
        pour(newDurations, highPins)
    else:
        return

@app.route('/qchart')
def quantity_chart():
    """
    Tallies ingredient quantities and passes array to /templates/chart.html.
    """
    drinkTotals = [0,0,0,0,0,0,0,0]
    ingrs = getIngredients()
    qChartList = [['Drink', 'Total Seconds Poured']]
    drinkData = getLog()
    for i in range(len(drinkTotals)):
        for drink in drinkData:
            drinkTotals[i] += int(drink[i])
        qChartList += [[ingrs[i], drinkTotals[i]]]
    
    return render_template('qchart.html', qChartList=qChartList)

@app.route('/dchart')
def drink_chart():
    """
    Tallies types of drinks consumed.
    """
    drinkInfo = getDrinkInfo()
    log = getLog()
    for ingrs in log:
        # Check for custom drinks.
        if not any([ingrs in [drinkInfo[drink]['ingredients'] for drink in drinkInfo]]):
            drinkInfo['Custom Drinks']['count'] += 1
        # Otherwise increment the appropriate count.
        else:
            for drink in drinkInfo:
                if ingrs == drinkInfo[drink]['ingredients']:
                    drinkInfo[drink]['count'] += 1
    drinkNames = [drink for drink in drinkInfo]
    # Create counts list and send it to JS.
    counts = [drinkInfo[drink]['count'] for drink in drinkInfo]
    return render_template('dchart.html', drinkNames=drinkNames, counts=counts)
    
@app.route('/statuschart')
def status_chart():
    """
    Draws a bar chart showing your remaining ingredient quantities.
    """
    
    ## need calibration here: Not all ingredients pour at equal speeds.
    ## also: 100 is an arbitrary placeholder.
    quantitiesLeft = [100,100,100,100,100,100,100,100]
    ingrs = getIngredients()
    log = getLog()
    for i in range(len(quantitiesLeft)):
        for drink in log:
            quantitiesLeft[i] -= int(drink[i])
    return render_template('statuschart.html', ingrs=ingrs, quantitiesLeft=quantitiesLeft)

@app.route('/drinkinfo')
def show_drinks():
    return str(getDrinkInfo())

@app.route('/log')
def log():
    return str(getLog())

@app.route('/clear')
def clear():
    clearLog()
    return 'Log cleared!'
    

if __name__ == '__main__':
    app.run()
