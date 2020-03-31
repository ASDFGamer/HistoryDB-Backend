#!/usr/bin/env python3

from shutil import copyfile
import re

filename = "swagger_server/controllers/default_controller.py"
orig_filename = filename + ".orig"
copyfile(filename, orig_filename)

destination = open(filename, "w")
with open(orig_filename, "r") as file:
    functionCall = ""
    for line in file:
        if "def operations_" in line:
            match = re.match(r"def\soperations_(\w*)(\(.*\))", line)
            split = match.group(1).split("_")
            parameters = match.group(2)
            parameters = parameters.replace("=None", "")
            functionCall = "swagger_server.services." + split[0] + "." + ''.join(split[1:]) + parameters
        if "return 'do some magic!'" in line:
            line = line.replace("'do some magic!'", functionCall)
            print(line)
        destination.write(line)

destination.close()
