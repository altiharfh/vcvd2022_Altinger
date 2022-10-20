
#import argument parser
import argparse
from examples.plotExample import exec_sample_plot_

#setup arg parser
arg_parser_ = argparse.ArgumentParser(description="Process some integers.")
arg_parser_.add_argument("pdf_file_out", type=str, help="filename to plot")
cmd_call_args_ = arg_parser_.parse_args()
print (cmd_call_args_.pdf_file_out)

exec_sample_plot_(cmd_call_args_.pdf_file_out)

exit()
