from arduino import Arduino
from flask import Flask, render_template
import time
from utils import *
import os
import json
import threading

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

## Declare all output pins

## uno.output([0,1,2,3,4,5,6,7])

##
pouring = {}
for i in range(8):
    pouring[i] = False

################################
###    Flask server setup    ###
################################

# Create server
app = Flask(__name__)

# Called if exception is raised
##@app.teardown_request
##def teardown_request(exception):
    #uno.turnOff()
    # placeholder return statement.
    ##return ''

@app.route('/pour/<ingredients>')
def log_and_prep_request(ingredients):
    logPath = getLogPath()
    with open(logPath, 'a') as log:
        log.write(ingredients)
        log.write("\n")
        
    L = [int(i) for i in ingredients]
    pour_all(L)
    return '%s now pouring.' % ingredients

def pour_valve(valve, duration):
    print 'Turning valve %d ON.\n' % valve
    # uno.setHigh(p)
    pouring[valve] = True
    time.sleep(duration)
    print 'Turning valve %d OFF.\n' % valve
    # uno.setLow(p)
    pouring[valve] = False
    
##def write_serial(pin):
    ##do stuff with serial module

def pour_all(ingredients):
    if shotbot_is_pouring():
        print 'Still pouring something.\nWait your turn yo!!!'
        return
    else:
        for i in range(len(ingredients)):
            if ingredients[i] > 0:
                thread = threading.Thread(target=pour_valve,
                                          args=(i, ingredients[i]))
                thread.start()
                time.sleep(0.1)
        return 'MAIN FUNCTION ENDING...'

def shotbot_is_pouring():
    return any(pouring.values())

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
