
# Usage

<br>

## Oscilloscope

<br>

To turn your Raspberry Pi into an **Oscilloscope** <br>
using this library, just clone the repository and <br>
use the following code:

```python
from PiScope import Plotter

plotter = Plotter()

# Here, the channel used 
# on ADS1015 is channel 0

plotter.setup([ 0 ]) 

plotter.plot()
```

<br>

### OR

<br>
<br>

Use [`example_oscilloscope.py`][Example Oscilloscope] with:

```sh
python example_oscilloscope.py
```

<br>

---

<br>

## XY Plotter

<br>

To turn your Raspberry Pi into an **XY Plotter** <br>
using this library, just clone the repository <br>
and use the following code:

```python
from PiScope import Plotter

plotter = Plotter()

# Here, the channels used on A
# DS1015 are channel 0 (X) 
# and channel 1 (Y).

plotter.setup([ 0 , 1 ]) 

plotter.plot()
```

<br>

## OR

<br>
<br>

Use [`example_xyplotter.py`][Example XYPlotter] with:

```sh
python example_xyplotter.py
```

<br>

<!----------------------------------------------------------------------------->

[Example Oscilloscope]: ../Source/example_oscilloscope.py
[Example XYPlotter]: ../Source/example_xyplotter.py
