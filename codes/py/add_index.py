import sys
from tools import *

# ------------------------------------------------------------------------------------------------------------
def createTr(name, img, whitespaces):
    res = ""
    codename = transformStrToPc(name)

    res += createLine(whitespaces, "<!--Element-->")
    res += createLine(whitespaces, "<tr >")
    res += createLine(whitespaces+1, "<td>")
    res += createLine(whitespaces+2, "<img class=\"img_ico\" src=\"../img/"+img+"\">")
    res += createLine(whitespaces+1, "</td>")
    res += createLine(whitespaces+1, "<td>")
    res += createLine(whitespaces+2, "<a href=\"codes-"+codename+"/codes-"+codename+".html\">"+name+" module</a>")
    res += createLine(whitespaces+1, "</td>")
    res += createLine(whitespaces, "</tr >")
    res += createLine(whitespaces, "<!--EndOfElement-->")
    return res

def createTrWithImg(lines, isImage):
    modulename = sys.argv[1]
    imgname = sys.argv[2] if isImage else "undefined.jpg"
    whitespaces = 0
    index = 0
    broke = False
    for line in lines:
        if line.strip() == "</table>":
            broke = True
            whitespaces = whitespacesCount(lines[index-1])-1
            break
        index = index+1
    if (broke):
        print("</table> at line ", index)
        newTr = createTr(modulename, imgname, whitespaces)
        print(newTr)
        return newTr, index
    else:
        print("something went wrong, aborting new element creation")
        return False, False
        

def splitter(num):
    lines = ""
    with open('../codes.html', 'r') as file:
        # Read the lines of the file into a list, where each element is a line
        lines = file.readlines()
        print("successfully readed example file")

    newlines, index = createTrWithImg(lines, num)
    # adding the new lines on the array
    lines.insert(index, newlines)
    '''
    for element in lines:
        print(element)
    '''
    with open("../codes.html", "w") as file2:
        file2.writelines(lines)
        print("succesfully added modules")

# ----------------------------------------------------------------------------------------------------------

# start of the main program

if len(sys.argv) == 3:
    splitter(True)

elif len(sys.argv) == 2:
    splitter(False)

else:
    print("number of arguments incorrect. ( add_index.py module_name ( img_path 'optional' ) )")