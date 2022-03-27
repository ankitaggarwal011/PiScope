# PiScope [![Badge Python]][Python] [![Badge License]][License]
*Turn your Raspberry Pi into an Oscilloscope / XY Plotter*

---

**⸢ [Dependencies] ⸥ ⸢ [Usage] ⸥ ⸢ [API] ⸥ ⸢ [Dry Test] ⸥**

---

This library allows you to easily interface your **Raspberry Pi** <br>
with the to it connected **Analog To Digital Converter**.

![Preview]

*[Raspberry Pi with ADS1015][ADS1015 Preview]*

---

An **Oscilloscope** is an instrument that can be used <br>
to display / analyze the waveform of electric signals.

In effect, the device draws a graph of <br>
the signal voltage as a function of time.

A **XY Plotter** is an instrument that plots <br>
two voltage with respect to one another.

---

## Supported Boards

- **[ADS1015 | Adafruit Breakout Board][ADS1015]**

---

## Motivation

I wanted to monitor analog sensors with my Raspberry Pi <br>
but I didn't have an actual oscilloscope, not to mention <br>
how costly they are as well as the space they take up.

While it isn't very precise, it may come <br>in handy in a multitude of applications.

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

[Preview]: Resources/Preview.png

[Badge License]: https://img.shields.io/badge/License-MIT-yellow.svg
[Badge Python]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white

[Python]: https://www.python.org/

[ADS1015]: http://www.adafruit.com/product/1083
[ADS1015 Preview]: https://learn.adafruit.com/system/guides/images/000/000/195/medium800/summary.jpg
