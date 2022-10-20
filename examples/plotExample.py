#based on 
#source: https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/
from cmath import pi
import matplotlib.pyplot as plt
import numpy as np

# make data
import numpy as np
import matplotlib.pyplot as plt

#================================================
def exec_sample_plot_(file_name_out):

       #define figure  
       fig = plt.figure()
       #add one plot
       ax1 = fig.add_subplot(111)

       #data
       t = np.arange(0.0, 1.0, 0.01)
       s = np.sin(2 * np.pi * t)
       #define plots
       line, = ax1.plot(t, s, color ="green", lw = 2)

       #add axis label
       ax1.set_xlabel("time")
       ax1.set_ylabel("sin (2 pi t)")

       #add plot label
       fig.suptitle("Plot Sample\n\n", fontweight ="bold")

       #export as PDF
       plt.savefig(file_name_out) 