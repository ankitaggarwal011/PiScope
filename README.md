# PiScope [![Badge Python]][Python] [![Badge License]][License]
*Turn your Raspberry Pi into an Oscilloscope / XY Plotter*

---

**⸢ [Dependencies] ⸥ ⸢ [Usage] ⸥ ⸢ [API] ⸥ ⸢ [Dry Test] ⸥**

---

An **oscilloscope** is a laboratory instrument commonly used to display and analyze the waveform of electronic signals. In effect, the device draws a graph of the instantaneous signal voltage as a function of time.

A **XY Plotter** is an instrument to plot a voltage variable with respect to another voltage variable. This is in contrast to the oscilloscope which plots a voltage variable with respect to time.

This python library can turn your **Raspberry Pi** into an Oscilloscope or XY plotter. Simply, interface an **Analog to Digital Converter** with your Raspberry Pi and use the library to view the analog signals on your Raspberry Pi. Currently, the library supports Adafruit ADS1015 breakout board.


![Preview]
*Raspberry Pi with ADS1015*

## Motivation
Oscilloscope are costly, bulky. I wanted to monitor analog sensors on Raspberry Pi and I didn't had an actual oscilloscope. Not exactly precise, but it could be very helpful for most applications.



---

## Contribute

If you wish to contribute to this library, simply fork the <br>
repository and open a pull-request once you are ready.


<!----------------------------------------------------------------------------->

[Dependencies]: Documentation/Dependencies.md
[Dry Test]: Documentation/Test.md
[License]: ./LICENSE
[Usage]: Documentation/Usage.md
[API]: Documentation/API.md

[Badge License]: https://img.shields.io/badge/License-MIT-yellow.svg
[Badge Python]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white

[Python]: https://www.python.org/

[Raspberry Pi & Python]: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code
[ADC Breakouts]: https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/
[Configuring I2C]: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
[ADS1015]: http://www.adafruit.com/product/1083
[Preview]: https://learn.adafruit.com/system/guides/images/000/000/195/medium800/summary.jpg
