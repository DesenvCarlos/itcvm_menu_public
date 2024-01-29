import sys
import os
from tools import *

# ------------------------------------------------------------------------------------------------------------


def splitter(module_name):
    codes = ""
    placeholder = ""
    with open('./codes-example.html', 'r') as file:
        # Read the lines of the file into a list, where each element is a line
        codes = file.readlines()
        print("successfully readed example file")
    with open('./placeholder.txt', 'r') as file:
        placeholder = file.readlines()
        print("successfully readed placeholder")

    if not os.path.isdir('../codes-'+(module_name)):
        os.mkdir('../codes-'+(module_name))

    with open('../codes-'+(module_name)+'/codes-'+(module_name)+'.html', 'w') as file:
        file.writelines(codes)
        print("created codes-"+(module_name))
    
    with open('../codes-'+(module_name)+'/info.txt', 'w') as file:
        file.writelines(placeholder)
        print("created placeholder")

    
# ----------------------------------------------------------------------------------------------------------

# start of the main program


if len(sys.argv) == 2:
    splitter(transformStrToPc(sys.argv[1]))

else:
    print("number of arguments incorrect. ( add_index.py module_name )")