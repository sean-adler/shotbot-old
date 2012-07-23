from arduino import Arduino
from flask import Flask

import time

###########################
###    Arduino setup    ###
###########################

# Specify the Uno's port as an argument
#uno = Arduino('/dev/tty.usbmodem621')

# Define which pin is connected to each ingredient
# (We don't actually use these vars, included solely for documentation.)
whiskey = 1
tequila = 2
vodka = 3
gin = 4
orange_juice = 5
pineapple_juice = 6
cranberry_juice = 7
sour_mix = 8

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
    drinkList = list([int(e) for e in ingredients])
    conc_helper(drinkList)
    return ""

# Helper function: Allows concurrent pouring
# Open all required valves at once and close when necessary
def conc_helper(L):
    if any([e for e in L if e > 0]):
        for e in range(len(L)):
            if L[e] > 0:
                # if uno.getState(e+1) != 'HIGH":
                print "Starting pin %d" % (e+1)
        sleep_time = min([e for e in L if e > 0])
        time.sleep(sleep_time)
        newL = [(e-sleep_time) for e in L]
        for e in range(len(newL)):
            if newL[e] == 0:
                print "Stopping pin %d" % (e+1)
        conc_helper(newL)
    else:
        return

if __name__ == '__main__':
    app.run()
