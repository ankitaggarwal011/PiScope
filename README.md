# PiScope
*Turn your Raspberry Pi into an Oscilloscope / XY Plotter*

An **oscilloscope** is a laboratory instrument commonly used to display and analyze the waveform of electronic signals. In effect, the device draws a graph of the instantaneous signal voltage as a function of time.

A **XY Plotter** is an instrument to plot a voltage variable with respect to another voltage variable. This is in contrast to the oscilloscope which plots a voltage variable with respect to time.

This python library can turn your **Raspberry Pi** into an Oscilloscope or XY plotter. Simply, interface an **Analog to Digital Converter** with your Raspberry Pi and use the library to view the analog signals on your Raspberry Pi. Currently, the library supports Adafruit ADS1015 breakout board.


![Preview]
*Raspberry Pi with ADS1015*

## Motivation
Oscilloscope are costly, bulky. I wanted to monitor analog sensors on Raspberry Pi and I didn't had an actual oscilloscope. Not exactly precise, but it could be very helpful for most applications.

## Dependencies

*Hardware*

1. Raspberry Pi B/B+/2

2. [ADS1015 Breakout board Analog to Digital converter][ADS1015]

*Software*

1. Python 2.7

The following python modules are needed in order to use this library:

```
pylab
matplotlib
Tkinter
```

In order to install these dependencies on Raspberry Pi, one can use the following command:

```
sudo apt-get install python-numpy python-scipy python-matplotlib python-tk
```

## Interfacing ADS1015 with Raspberry Pi

1. Connect Adafruit ADS1015 to Raspberry Pi
> GND to GND, 5V to 5V, SDA to SDA, SCL to SCL, ADDR to GND (I2C address 0x48)
2. Check the devices connected to the I2C bus using the command below
> The Adafruit ADS1015 should be shown at: 
```sh
$ sudo i2cdetect -y 1
```

If you need help in interfacing, check out the official documentation from Adafruit:

- [Configuring I2C]

- [ADC Breakouts]

- [Raspberry Pi & Python]



## Contributors

#### Author: Ankit Aggarwal

If anybody is interested in working on developing this library, fork and feel free to get in touch with me.

## License

[MIT License][License]

<!----------------------------------------------------------------------------->

[License]: ./LICENSE

[Raspberry Pi & Python]: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code
[ADC Breakouts]: https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/
[Configuring I2C]: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
[ADS1015]: http://www.adafruit.com/product/1083
[Preview]: https://learn.adafruit.com/system/guides/images/000/000/195/medium800/summary.jpg
