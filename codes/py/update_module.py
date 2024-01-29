import sys
import os
from tools import *

# ------------------------------------------------------------------------------------------------------------

def parseData(content):
    result_array = []
    current_block = []

    for line in content:
        if "@start@" in line:
            # If the current block is not empty, add it to the result array
            if current_block:
                result_array.append((False, current_block))
            current_block = [line]  # Start a new block with the current line
        elif "@end@" in line:
            current_block.append(line)  # Add the line to the current block
            result_array.append((True, current_block[1:-1]))  # Add the completed block to the result array
            current_block = []  # Reset the current block
        else:
            current_block.append(line)  # Add the line to the current block

    # If there's a block remaining after the loop, add it to the result array
    if current_block:
        result_array.append((False, current_block))

    return result_array

def addOnContent_codes(content, newData, index):
    res = content
    whitespaces = whitespacesCount((content[index].split('<'))[0]) + 2
    print("indexing level: ",whitespaces," spaces")

    for isTag, element in reversed(newData):
        if isTag:
            res.insert(index, createTextelement(element, whitespaces))
        else:
            res.insert(index, createTitle(element, whitespaces))

    return res

def splitter(module_name):
    pages = ""
    insert = ""
    info = ""

    with open('../codes-'+(module_name)+'/codes-'+(module_name)+'.html', 'r') as file:
        # Read the lines of the file into a list, where each element is a line
        pages = file.readlines()
        print("successfully readed html file")
    
    with open('../codes-'+(module_name)+'/info.txt', 'r') as file:
        info = file.readlines()
        print("succesfully readed codes")
        print("lines of content: ", len(info))

    index = find_tag_line(pages, '<main class="code"><!--123456789-->') + 1

    if index == None:
        print("not found data div. exiting")
        return
    else:
        print("<div id=\"data\"> tag found at line ",index+1)
    

    insert = parseData(info)
    pages = addOnContent_codes(pages, insert, index)

    for cont in insert:
        print(cont)


    with open('../codes-'+(module_name)+'/codes-'+(module_name)+'.html', 'w') as file:
        file.writelines(pages)
        print("updated html file")

# ----------------------------------------------------------------------------------------------------------

# start of the main program

if len(sys.argv) == 2:
    splitter(transformStrToPc(sys.argv[1]))

else:
    print("number of arguments incorrect. ( update_module.py module_name )")