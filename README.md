# Rasperry Pi oscilloscope

This repository contains python script to turn your raspberry pi into an oscilloscope. 

## Dependencies
*Hardware*
1. Raspberry Pi
2. ADS1015 Breakout board Analog to Digital converter
*Software*
1. Python 2.7
The python modules are needed in order to use this library.
```
pylab
matplotlib
Tkinter
```
## Usage
Clone the repository and use the following code.

Run the command directly from the console with command line arguments to the file fb_image.py. The command line arguments are explained as:

For example,

```sh
$ python Plotter.py
$ python Plotterxy.py
```

Run Plotter.py to plot real time the input wave on channel 0 with time.
Run Plotterxy.py to plot real time between signals on channel 0 and channel 1 of ADS1015.

## Contributors

#### Author: Ankit Aggarwal

If anybody is interested in working on developing this library, fork and feel free to get in touch with me.

## License

[MIT License](https://github.com/ankitaggarwal011/pi-oscilloscope/blob/master/LICENSE)