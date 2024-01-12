__doc__ = "sample file for a main methode"

#import system libs
import argparse
import sys

#own modules
from examples.plot_example import exec_sample_plot_
from examples.plot_concarve_hul import plot_concarve_

print("Hello world\n")

#setup arg parser
arg_parser_ = argparse.ArgumentParser(description="Process some integers.")
arg_parser_.add_argument("--pdf_file_out", type=str, help="filename to plot")
arg_parser_.add_argument("sec", type=str, help="sec_argument")
cmd_call_args_ = arg_parser_.parse_args()
if cmd_call_args_.pdf_file_out != None:
  print (cmd_call_args_.pdf_file_out)
else:
  cmd_call_args_.pdf_file_out = "out.pdf"
if cmd_call_args_.sec != 0:
  print (cmd_call_args_.sec)

#===============
# a method
def main_method():
  main_method.__doc__ = "sample main method"
  #exec_sample_plot_(cmd_call_args_.pdf_file_out)
  plot_concarve_(cmd_call_args_.pdf_file_out)

#===============
# do work and call a methode
main_method()

#terminate program
sys.exit()
