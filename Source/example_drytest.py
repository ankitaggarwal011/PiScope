from PiScope import Plotter
import math

class DryTest(Plotter):
	def read(self):
	    print "Reading channels..."
	    if len(self.channels) == 1:
	      for i in range(1200):
	        self.values.append(math.cos(i*3.14/180))
	    elif len(self.channels) == 2:
	      self.valuesx.append(2.5)
	      self.valuesy.append(2.0)
	    return


# Create oscilloscope
piscope = DryTest()

# Setup channels
piscope.setup([0]) # Oscilloscope
#piscope.setup([0, 1]) # XY Plotter

# Start plotting
piscope.plot()
