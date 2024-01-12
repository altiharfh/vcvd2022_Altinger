__doc__ = "sample file for ploting method \
           baed on \
           https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/"

#based on
#source: https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/

#required imports
import matplotlib.pyplot as plt
import numpy as np


#================================================
def plot_concarve_(file_name_out):
  plot_concarve_.__doc__ = "concarve hul plot"

  #define figure
  fig = plt.figure()
  #add one plot
  ax1 = fig.add_subplot(111)

  #data
  t = np.arange(0,5000,1)
  s = t^2
  #define plots
  ax1.plot(t, s, color ="green", lw = 2)

  #add axis label
  ax1.set_xlabel("Density (k))")
  ax1.set_ylabel("Flow (q)")

  #add plot label
  fig.suptitle("LWR Model asupmption\n", fontweight ="bold")

  #export as PDF
  plt.savefig(file_name_out)
  