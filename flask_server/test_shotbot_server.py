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

def pour_drink(ingredients):
    """
    Takes argument 'ingredients' which is always an 8-digit string of ints.
    Each number in the string corresponds to how long a particular
    ingredient is poured (or equivalently, how long its corresponding
    pin is HIGH).
    """
    # Iterate over URL string (each ingredient)
    for pin in range(len(ingredients)):
        if ingredients[pin] != "0":
            # Determine pour time
            pour_time = float(ingredients[pin])
            print "Turning on pin %d" % (pin+1)
            # Leave pin high for appropriate time
            time.sleep(pour_time)
            print "Turning off pin %d" % (pin+1)
    # Print ingredients to browser window
    return ingredients


if __name__ == '__main__':
    app.run()
