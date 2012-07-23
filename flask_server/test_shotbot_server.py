from arduino import Arduino
from flask import Flask

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

# Declare the server's only route
@app.route('/<ingredients>')

def pour(ingredients):
    """
    Take the URL string and pass it to our recursive function
    as a list of ints.
    """
    ingredientList = list([int(e) for e in ingredients])
    conc_helper(ingredientList, [])
    return ""

# Helper function: Allows concurrent pouring
# Open all required valves at once and close when necessary
def conc_helper(L, highPins):
    """
    This helper function enables concurrent pouring.
    Opens all required valves immediately and closes each when necessary.
    """
    # Recurse until all ingredients are completely poured
    if any([e for e in L if e > 0]):
        for e in range(len(L)):
            if L[e] > 0 and e not in highPins:
                highPins += [e]
                print "Starting pin %d" % (e)
        # Leave pins high until at least one ingredient is completely poured
        sleep_time = min([e for e in L if e > 0])
        time.sleep(sleep_time)
        # Subtract time elapsed from all ingredients
        newL = [(e-sleep_time) for e in L]
        # Turn off pins whose ingredients are completely poured
        for e in range(len(newL)):
            if newL[e] == 0:
                print "Stopping pin %d" % (e)
        # Recurse on adjusted list
        conc_helper(newL, highPins)
    else:
        return

if __name__ == '__main__':
    app.run()
