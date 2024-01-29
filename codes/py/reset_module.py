import sys
import os
from tools import *

# ------------------------------------------------------------------------------------------------------------

def splitter(module_name):
    pages = ""
    insert = ""
    index_start = 0
    index_end = 0
    print('../codes-'+(module_name)+'/codes-'+(module_name)+'.html')
    with open('../codes-'+(module_name)+'/codes-'+(module_name)+'.html', 'r') as file:
        # Read the lines of the file into a list, where each element is a line
        pages = file.readlines()
        print("successfully readed html file")
    
    index_start = find_tag_line(pages, '<main class="code"><!--123456789-->')
    index_end = find_tag_line(pages, '</main><!--987654321-->')

    print(index_start,", ",index_end)

    if index_start != None and index_end != None:
        pages = pages[:index_start+1] + ["\n"] + pages[index_end:]

        with open('../codes-'+(module_name)+'/codes-'+(module_name)+'.html', 'w') as files:
            files.writelines(pages)

# ----------------------------------------------------------------------------------------------------------

# start of the main program

if len(sys.argv) == 2:
    splitter(transformStrToPc(sys.argv[1]))

else:
    print("number of arguments incorrect. ( update_module.py module_name )")