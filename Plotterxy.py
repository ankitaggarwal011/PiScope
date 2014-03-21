#!/usr/bin/env python
import pylab
from Adafruit_ADS1x15 import ADS1x15
from pylab import *
import Tkinter,time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

root = Tkinter.Tk()
root.wm_title("Plot X-Y")

xAchse=pylab.array([0]*100)
yAchse=pylab.array([0]*100)

fig = pylab.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_title("Realtime Waveform Plot")
ax.set_xlabel("Channel 2")
ax.set_ylabel("Channel 1")
ax.axis([0,3.5,0,3.5])
line1=ax.plot(xAchse,yAchse,'-')

drawing = FigureCanvasTkAgg(fig, master=root)
drawing.show()
drawing.get_tk_widget().pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

tool = NavigationToolbar2TkAgg( drawing, root )
tool.update()
drawing._tkcanvas.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

valuesy=[]
valuesx=[]
valuesx = [0 for x in range(100)]
valuesy = [0 for y in range(100)]
def generator():
  global valuesx,valuesy,scale2
  adc = ADS1x15()
  # Read channel 0 and 1 in single-ended mode (1 bit = 3mV)
  for i in range(1):
    valuesy.append(adc.readADCSingleEnded(0)*0.003)
  for j in range(1):
    valuesx.append(adc.readADCSingleEnded(1)*0.003)
  root.after(int(scale2['to'])-scale2.get(),generator)

def plotter():
  global valuesx,valuesy,scale1,scale2
  NumberSamplesy=min(len(valuesy),scale1.get())
  NumberSamplesx=min(len(valuesx),scale1.get())
  
  line1[0].set_data(pylab.array(valuesx[-NumberSamplesx:]),pylab.array(valuesy[-NumberSamplesy:]))
 
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

scale1.set(100)
scale2.set(scale2['to']-10)

root.protocol("WM_DELETE_WINDOW", _quit)  
root.after(100,generator)
root.after(100,plotter)
Tkinter.mainloop()
