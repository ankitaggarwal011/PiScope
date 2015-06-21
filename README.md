# PiScope: Turn your Raspberry Pi into an Oscilloscope/XY Plotter

An **oscilloscope** is a laboratory instrument commonly used to display and analyze the waveform of electronic signals. In effect, the device draws a graph of the instantaneous signal voltage as a function of time.

A **XY Plotter** is an instrument to plot a voltage variable with respect to another voltage variable. This is in contrast to the oscilloscope which plots a voltage variable with respect to time.

This python library can turn your **Raspberry Pi** into an Oscilloscope or XY plotter. Simply, interface an **Analog to Digital Converter** with your Raspberry Pi and use the library to view the analog signals on your Raspberry Pi. Currently, the library supports Adafruit ADS1015 breakout board. 

![alt text](https://learn.adafruit.com/system/guides/images/000/000/195/medium800/summary.jpg "Raspberry Pi with ADS1015")

## Motivation
Oscilloscope are costly, bulky. I wanted to monitor analog sensors on Raspberry Pi and I didn't had an actual oscilloscope. Not exactly precise, but it could be very helpful for most applications.

## Dependencies
*Hardware*
1. Raspberry Pi B/B+/2
2. [ADS1015 Breakout board Analog to Digital converter](http://www.adafruit.com/product/1083)

*Software*
1. Python 2.7

The following python modules are needed in order to use this library:

```
pylab
matplotlib
Tkinter
```

## Interfacing ADS1015 with Raspberry Pi

1. Connect Adafruit ADS1015 to Raspberry Pi
> GND to GND, 5V to 5V, SDL to SDL, SCL to SCL, ADDR to GND (I2C address 0x48)
2. Check the devices connected to the I2C bus using the command below
> The Adafruit ADS1015 should be shown at: 
```sh
$ sudo i2cdetect -y 1
```

If you need help in interfacing, check out the official documentation from Adafruit:
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/
https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code 

## Usage

To turn your Raspberry Pi into an *Oscilloscope* using this library, just clone the repository and use the following code:

```python
from PiScope import Plotter

piscope = Plotter()

piscope.setup([0]) # Here, the channel used on ADS1015 is channel 0.

piscope.plot()
```

#### OR

Use example_oscilloscope.py available with the repository.
```sh
$ python example_oscilloscope.py
```

To turn your Raspberry Pi into an *XY Plotter* using this library, just clone the repository and use the following code:

```python
from PiScope import Plotter

piscope = Plotter()

piscope.setup([0, 1]) # Here, the channels used on ADS1015 are channel 0 (X) and channel 1 (Y).

piscope.plot()
```

#### OR

Use example_xyplotter.py available with the repository.
```sh
$ python example_xyplotter.py
```

# Dry Test

In case you don't own a Raspberry Pi or ADS1015 yet, but want to see the library in action, I have included a dry test example, which doesn't require any hardware. You can simply run it on any Linux/Windows platform.

Use example_drytest.py available with the repository.

```sh
$ python example_drytest.py
```

## Example results

![](https://raw.githubusercontent.com/ankitaggarwal011/PiScope/master/example_oscilloscope.png)
*Oscilloscope*


![](https://raw.githubusercontent.com/ankitaggarwal011/PiScope/master/example_xyplotter.png)
*XY Plotter*

## API
```python
from PiScope import Plotter
```
Import the module in your main file.

```python
piscope = Plotter()
```
Create oscilloscope/XY Plotter

#### piscope.setup(channels)
Setup the channels of ADS1015 being used for oscilloscope/XY Plotter.

**
channels is the channels of ADS1015 which are to be used, Type: List/Array of 1 or 2 Integers.
e.g. In case of an oscilloscope, channels is a list with one element representing the active ADS1015 channel (channels = [channel_number]).
e.g. In case of an oscilloscope, channels is a list with two elements representing the active ADS1015 channels (channels = [channel_number_X, channel_number_Y]).
**

#### piscope.plot()
Plot the analog values on the oscilloscope/XY Plotter.

## Contributors

#### Author: Ankit Aggarwal

If anybody is interested in working on developing this library, fork and feel free to get in touch with me.

## License

[MIT License](https://github.com/ankitaggarwal011/PiScope/blob/master/LICENSE)