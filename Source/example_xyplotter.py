from PiScope import Plotter

# Create XY Plotter
piscope = Plotter()

# Setup channels
piscope.setup([0, 1])

# Start plotting
piscope.plot()
