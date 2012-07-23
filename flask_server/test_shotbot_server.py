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

whiskey = 1
tequila = 2
vodka = 3
gin = 4
orange_juice = 5
pineapple_juice = 6
cranberry_juice = 7
sour_mix = 8
"""

# Declare all output pins

#uno.output([1,2,3,4,5,6,7,8])

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
    drinkList = list([int(e) for e in ingredients])
    conc_helper(drinkList)
    return ""

# Helper function: Allows concurrent pouring
# Open all required valves at once and close when necessary
def conc_helper(L):
    """
    This helper function enables concurrent pouring.
    Opens all required valves immediately and closes each when necessary.
    """
    # Recurse until all ingredients are completely poured
    if any([e for e in L if e > 0]):
        for e in range(len(L)):
            if L[e] > 0:
                # Arduino pins are not zero-offset
                # Add 1 to the list index to access correct pin
                print "Starting pin %d" % (e+1)
        sleep_time = min([e for e in L if e > 0])
        time.sleep(sleep_time)
        # Subtract time elapsed from all ingredients
        newL = [(e-sleep_time) for e in L]
        # Turn off pins whose ingredients are completely poured
        for e in range(len(newL)):
            if newL[e] == 0:
                print "Stopping pin %d" % (e+1)
        # Recurse on adjusted list
        conc_helper(newL)
    else:
        return

if __name__ == '__main__':
    app.run()
