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