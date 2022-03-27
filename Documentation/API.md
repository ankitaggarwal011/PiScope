
# API

## Import

The module can be imported with:

```python
from PiScope import Plotter
```

---

## Plotter

Create a **Oscilloscope** / **XY Plotter** instance with:

```python
plotter = Plotter()
```

---

## Setup
***`plotter.setup(channels)`***

Setup the channels of the breakout board used for oscilloscope / XY Plotter.

### Channels 

**Type :** `List / Array`

The list of channels to listen to.

##### Oscilloscope

In this configuration, `channels` is a list with `1` element <br>
representing the active channel on which to listen.

```python
plotter.setup([ <Channel> ])
```

##### XY Plotter

In this configuration, `channels` is a list with `2` elements <br>
representing the active channels on which to listen. 

```python
plotter.setup([ <X-Channel> , <Y-Channel> ])
```

---

## Plot
***`plotter.plot()`***

Plots the analog values on the **Oscilloscope** / **XY Plotter**.
