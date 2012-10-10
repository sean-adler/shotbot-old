###iPad talks to Arduino, makes you drinks!

To test the interface without a microcontroller, start the Flask server:

`$ python flask_server/test_shotbot_server.py`

Then open the .xcodeproj and click Run.

Choose a drink and tap the button to send a drink request to the Flask server, which simulates writing to some pins.

![Choosing a drink](https://github.com/sean-adler/ShotBot/raw/master/sample/shotbot.png)

_The Flask server `shotbot_server.py` uses the [Hashnuke Python to Arduino](https://github.com/HashNuke/Python-Arduino-Prototyping-API) library._

_COMING SOON: A short hardware component list and tutorial._