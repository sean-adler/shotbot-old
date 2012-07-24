####This is a work in progress.

To test the interface without a microcontroller, start the Flask server:

    $ python flask_server/test_shotbot_server.py

Then open the .xcodeproj and click Run.

Choose a drink and tap the button to send a drink request to the Flask server, which simulates writing to some pins.

_The "production" Flask server `shotbot_server.py` uses this [Python to Arduino](https://github.com/HashNuke/Python-Arduino-Prototyping-API) library._