__doc__ = "sample file how to handle json file read/write"

"""Provide sample python statements to handle json files

"""

import json
import argparse

#ideas see:
#https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

mass = 1
velocity = 2
friction = 0.5

params = [mass, velocity, friction]

params_dict = {}
params_dict["mass"] = mass
params_dict["velocity"] = velocity
params_dict["friction"] = friction

#to json format
json_object = json.dumps(params)

#to json format
json_object_dict = json.dumps(params_dict)

#setup arg parser
arg_parser_ = argparse.ArgumentParser(
    description="simple example to showcase json handling")
arg_parser_.add_argument("jsonpath", type=str, help="path to json file")
cmd_call_args_ = arg_parser_.parse_args()

# Writing to sample.json
with open(cmd_call_args_.jsonpath, "w", encoding="UTF-8") as outfile:
    outfile.write(json_object)

# Writing to sample.json

filename = (cmd_call_args_.jsonpath).split(".")
new_filename = filename[0] + "_dict." + filename[1]
with open(new_filename, "w", encoding="UTF-8") as outfile:
    outfile.write(json_object_dict)

# Load the data
with open(cmd_call_args_.jsonpath, "r", encoding="UTF-8") as json_in:
    loaded_params = json.load(json_in)

print (loaded_params)

mass_config,velocity_config,friction_config = loaded_params

print(f" \
    mass={mass_config}\n \
    velocity={velocity_config}\n \
    friction={friction_config:0.2f}")
