"""
The MIT License (MIT)

Copyright (c) 2014 Ankit Aggarwal <ankitaggarwal011@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

#!/usr/bin/env python
import pylab
from Adafruit_ADS1x15 import ADS1x15
from pylab import *
import Tkinter,time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

root = Tkinter.Tk()
root.wm_title("Plot with Time")

xAchse=pylab.arange(0,4000,1)
yAchse=pylab.array([0]*4000)

fig = pylab.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_title("Realtime Waveform Plot")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.axis([0,4000,0,3.5])
line1=ax.plot(xAchse,yAchse,'-')

drawing = FigureCanvasTkAgg(fig, master=root)
drawing.show()
drawing.get_tk_widget().pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

tool = NavigationToolbar2TkAgg( drawing, root )
tool.update()
drawing._tkcanvas.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

values=[]
values = [0 for x in range(4000)]

def generator():
  global values,scale2
  adc = ADS1x15()
  # Read channel 0 and 1 in single-ended mode (1 bit = 3mV)
  for i in range(1200):
    values.append(adc.readADCSingleEnded(0)*0.003)
  root.after(int(scale2['to'])-scale2.get(),generator)

def plotter():
  global values,scale1,scale2
  NumberSamples=min(len(values),scale1.get())
  CurrentXAxis=pylab.arange(len(values)-NumberSamples,len(values),1)
  line1[0].set_data(CurrentXAxis,pylab.array(values[-NumberSamples:]))
  ax.axis([CurrentXAxis.min(),CurrentXAxis.max(),0,3.5])
  drawing.draw()
  root.after(25,plotter)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Tkinter.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tkinter.BOTTOM)

scale1 = Tkinter.Scale(master=root,label="View Width:", from_=3, to=1000,sliderlength=30,length=ax.get_frame().get_window_extent().width, orient=Tkinter.HORIZONTAL)
scale2 = Tkinter.Scale(master=root,label="Generation Speed:", from_=1, to=200,sliderlength=30,length=ax.get_frame().get_window_extent().width, orient=Tkinter.HORIZONTAL)
scale2.pack(side=Tkinter.BOTTOM)
scale1.pack(side=Tkinter.BOTTOM)

scale1.set(4000)
scale2.set(scale2['to']-10)

root.protocol("WM_DELETE_WINDOW", _quit)  
root.after(4000,generator)
root.after(4000,plotter)
Tkinter.mainloop()

