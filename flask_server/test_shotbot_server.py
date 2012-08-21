from arduino import Arduino
from flask import Flask, render_template
from time import sleep
from utils import *
import os

###########################
###    Arduino setup    ###
###########################

# Specify the Uno's port as an argument
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

# Route takes drink requests
@app.route('/pour/<ingredients>')
def prepare_request(ingredients):
    """
    Takes the URL string and passes it to the recursive 'pour' function
    as a list of ints.
    """
    # The ingredient list is a numerical representation of how long
    # each ingredient's corresponding pin will be HIGH (open valve).
    ingredientList = [int(n) for n in ingredients]
    # pass list to pour() function, 2nd arg: no pins are high.
    pour(ingredientList, [])
    # log the drink
    logPath = getLogPath()
    with open(logPath, "a") as log:
        log.write(ingredients)
        log.write("\n")
    # unnecessary return statement
    return ingredients

# Opens all required valves at once and closes them when necessary.
def pour(pinDurations, highPins):
    """
    Takes two lists of ints: pinDurations, which corresponds to
    pour times of each ingredient stored in ShotBot, and
    highPins, which keeps track of which pins are currently high.
    Fires up the required Arduino pins immediately,
    powering down each when the ingredient is fully poured.
    """
    # Recurse until all ingredients are completely poured.
    if any(p for p in pinDurations if p > 0):
        for p in range(len(pinDurations)):
            if pinDurations[p] > 0 and p not in highPins:
                highPins.append(p)
                print "Writing HIGH to Pin %d" % p
        # Leave pins high until at least one ingredient is completely poured.
        pour_time = min(p for p in pinDurations if p > 0)
        sleep(pour_time)
        # Update durations
        newDurations = [(p-pour_time) for p in pinDurations]
        # Turn off pins whose ingredients are completely poured.
        for p in range(len(newDurations)):
            if newDurations[p] == 0:
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
    drinkData = getLog()
    for i in range(len(drinkTotals)):
        for drink in drinkData:
            drinkTotals[i] += int(drink[i])
    return render_template('chart.html', drinkTotals=drinkTotals)


@app.route('/dchart')
def drink_chart():
    """
    Tallies types of drinks consumed.
    """
    drinkDict = getDrinkInfo()
    # Read log file.
    log = getLog()
    for ingrs in log:
        # Check for custom drinks (not in drinkInfo).
        if not any([ingrs in [drinkDict[drink]['ingredients'] for drink in drinkDict]]):
            drinkDict['Custom Drinks']['count'] += 1
        # Otherwise increment the appropriate count.
        else:
            for drink in drinkDict:
                if ingrs == drinkDict[drink]['ingredients']:
                    drinkDict[drink]['count'] += 1
            
    #return render_template('drink_chart.html', drinkCount=drinkCount)
    
    ## placeholder return:
    return str(drinkDict)
    
@app.route('/status')
def show_status():
    """
    Draws a bar chart showing your remaining ingredient quantities.
    """
    ## need calibration here: Not all ingredients pour at equal speeds.
    ## also: 100 is an arbitrary placeholder, need to estimate this.
    quantitiesLeft = [100,100,100,100,100,100,100,100]

    # read log file
    log = getLog()
    for i in range(len(quantitiesLeft)):
        for drink in log:
            quantitiesLeft[i] -= int(drink[i])
    #render_template('status.html', quantitiesLeft=quantitiesLeft)
    
    ## placeholder return:
    return str(quantitiesLeft)

@app.route('/drinklist')
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
