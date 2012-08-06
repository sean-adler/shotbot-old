from arduino import Arduino
from flask import Flask, request, session, url_for, render_template

import time

###########################
###    Arduino setup    ###
###########################

# Specify the Uno's port as an argument
#uno = Arduino('/dev/tty.usbmodem621')

"""
PIN ASSOCIATIONS

Purely for documentation (these vars are never used)

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
def pass_req(ingredients):
    """
    Take the URL string and pass it to recursive 'pour' function
    as a list of ints.
    """
    # The ingredient list is just a numerical representation of how long
    # each ingredient's corresponding pin will be HIGH to open its valve
    ingredientList = list([int(n) for n in ingredients])
    pour(ingredientList, [])
    with open("log.txt", "a") as log:
        log.write(ingredients)
        log.write("\n")
    return ingredients

# Helper function: Allows concurrent pouring
# Opens all required valves at once and closes them when necessary
def pour(pinDurations, highPins):
    """
    This function fires up all required Arduino pins immediately,
    and powers down each when its ingredient is fully poured.
    """
    # Recurse until all ingredients are completely poured
    if any([p for p in pinDurations if p > 0]):
        for p in range(len(pinDurations)):
            if pinDurations[p] > 0 and p not in highPins:
                highPins.append(p)
                print "Writing HIGH to Pin %d" % p
        # Leave pins high until at least one ingredient is completely poured
        pour_time = min([p for p in pinDurations if p > 0])
        time.sleep(pour_time)
        # Subtract time elapsed from all ingredients
        newDurations = [(p-pour_time) for p in pinDurations]
        # Turn off pins whose ingredients are completely poured
        for p in range(len(newDurations)):
            if newDurations[p] == 0:
                print "Writing LOW to Pin %d" % p
        # Recurse on adjusted list
        pour(newDurations, highPins)
    else:
        return

@app.route('/chart')
def draw_chart():
    drinkTotals = [0,0,0,0,0,0,0,0]
    with open('/Users/SDA/shotbot/flask_server/log.txt') as log:
        drinkData = log.readlines()
    for i in range(len(drinkTotals)):
        for drink in drinkData:
            drinkTotals[i] += int(drink[i])
    return render_template('chart.html', drinkTotals=drinkTotals)

if __name__ == '__main__':
    app.run()
