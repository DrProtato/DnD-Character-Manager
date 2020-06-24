#main script file

#importing other functions and sections
import SectionRandomManager
'''
import Section1
import Section2
import Section5
import Section8
'''
character = []

def tryAgain():
    print("Try again, make sure you typed your response correctly.")

def lineBreak():
    print("\n---------------------------------------------------")

def startSequence():
    lineBreak()
    print("Hello there and welcome to the D%D Character creator!")
    print("This program is here to help you create a character for your next campaign.")

    while True:
        startresponse = input("Type 'start' to get started, or type 'exit' to exit the program.\n\n")
        if startresponse == "start":
            break
            #exits loop so then the next function can begin
        elif startresponse == "exit":
            exit()
        else:
            tryAgain()

def findSectionToRand(character = []):
    lineBreak()
    while True:
        print("There are 8 sections that can be randomised.")
        print("(Note: only a few sections are available in this build.)")
        print("The sections that are available are 1 (class and race), 2 (stat roll), 5 (spells) and 8 (name).")
        print("Which sections do you want to randomise?")
        response1 = input("Do you want to randomise all sections? (type 'yes' or 'no')\n\n")
        if response1 == "yes":
            #rand all sections
            randList = [1,2,3,4,5,6,7,8]
            manList = []
            SectionRandomManager.randomSpecific(manList, randList)
            break
        elif response1 == "no":
            response2 = input("Type '1,2,3,..' for certain sections that you want to be randomised.\n\n")
            randList = []
            manList = []
            for i in response2:
                if i != ",":
                    randList.append(int(i))
            j = 1
            i = 0
            while j < 9:
                while i < len(randList):
                    if int(j) == int(randList[i]):
                        j = j + 1
                        i = i + 1
                    elif j < randList[i]:
                        while j < randList[i]:
                            manList.append(j)
                            j = j + 1
                    else:
                        i = i + 1
            SectionRandomManager.randomSpecific(manList, randList, character)
            break
        else:
            tryAgain()

startSequence()
findSectionToRand(character)


