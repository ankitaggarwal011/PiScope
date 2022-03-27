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

channels is the channels of ADS1015 which are to be used, Type: List/Array of 1 or 2 Integers.

e.g. In case of an oscilloscope, channels is a list with one element representing the active ADS1015 channel (channels = [channel_number]).

e.g. In case of an oscilloscope, channels is a list with two elements representing the active ADS1015 channels (channels = [channel_number_X, channel_number_Y]).

#### piscope.plot()
Plot the analog values on the oscilloscope/XY Plotter.
