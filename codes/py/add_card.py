import sys
from tools import *

def insertOnPage(cardname, cardimg, links, uris):
    with open('../../index.html', 'r') as file:
        lines = file.readlines()
    
    index = find_tag_line(lines, "</main>")
    print(index)
    whitespaces = whitespacesCount(lines[index])-1
    data = createCard(cardname, cardimg, links, uris, whitespaces)

    lines.insert(index, data)
    with open("../../index.html", "w") as file2:
        file2.writelines(lines)
        print("succesfully added modules")

def splitter():
    print("Enter name of the new card: ", end="")
    cardname = input()
    print("Enter name of the thumbnail image ( png, jpg, etc... ): ", end="")
    cardimg = input()
    if len(cardimg) == 0:
        cardimg = "defaultcard.png"

    links = []
    uris = []
    exit = False
    print("NOW CREATING LINKS ")
    while not exit:
        print("Enter name link: ", end="")
        link = str(input())
        links.append(link)
        print("Enter url: ", end="")
        uri = str(input())
        uris.append(uri)

        print("continue? ", end="")
        if len(input()) == 0:
            exit = not exit
    
    print("Displaying new card:")
    print(cardname)
    print("./img/"+cardimg)
    i = 0
    while i < len(links):
        if len(links[i]) > 0:
            print(links[i]+" ("+uris[i]+")")
        i += 1

    correctInput = False
    while not correctInput:
        correctInput = True
        print("\nprocedign to create element in index. proceed(Y/N)? ")
        exit = input()
        if (exit == "Y" or exit == "y"):
            print("creating element")
            insertOnPage(cardname, cardimg, links, uris)

        elif (exit == "N" or exit == "n"):
            print("exiting...")
        else:
            correctInput = False


if len(sys.argv) == 1:
    splitter()

else:
    print("number of arguments incorrect. ( this script doesnt accept additional arguments )")