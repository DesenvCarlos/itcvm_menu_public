def whitespacesCount(input_string):
    count = 0
    for char in input_string:
        if char.isspace():
            count += 1
    return count

def createWhitespaces(val):
    res = ""
    while val > 0:
        val = val - 1
        res = res + " "
    return res

def createLine(spaces, content):
    return createWhitespaces(spaces) + content + "\n"

def transformStrToPc(content):
    res = ""
    for char in content:
        if char == " " or char == "\n" or char == "\t":
            res += "_"
        else:
            res += char
    return res

def cleanString(line):
    return line.strip()

def find_tag_line(content, tag):
    for i, line in enumerate(content):
        if tag in line:
            return i
    return None

def createTitle(content, whitespaces):
    res = ""
    res += createLine(whitespaces, "<div class=\"datatext\">")
    for element in content:
        res += createLine(whitespaces+2, "<h3>"+element+"</h3>")

    res += createLine(whitespaces, "</div>")
    return res

def createTextelement(content, whitespaces):
    res = ""
    res += createLine(whitespaces, "<div class=\"textelement\">")
    for element in content:
        res += createLine(whitespaces+2, element)

    res += createLine(whitespaces, "</div>")
    return res

def createCard(name, img, links, uris, whitespaces):
    res = ""
    i = 0

    res += createLine(whitespaces+2, "<!--Element-->")
    res += createLine(whitespaces+2, "<div class=\"card\">")
    res += createLine(whitespaces+4, "<img src=\"./img/"+ img +"\" alt=\"IMG Not_Found\">")
    res += createLine(whitespaces+4, "<div class=\"info\">")
    res += createLine(whitespaces+6, "<div class=\"title\">"+ name +"</div>")
    res += createLine(whitespaces+6, "<div class=\"description\">")
    while i < len(links):
        res += createLine(whitespaces+8, "<a href=\""+ uris[i] +"\">"+ links[i] +"</a>")
        i += 1
    res += createLine(whitespaces+6, "</div>")
    res += createLine(whitespaces+4, "</div>")
    res += createLine(whitespaces+2, "</div>")

    res += createLine(whitespaces+2, "<!--EndOfElement-->")

    return res
