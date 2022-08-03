from PiScope import Plotter

# Create oscilloscope
piscope = Plotter()

# Setup channels
piscope.setup([0])

# Start plotting
piscope.plot()
