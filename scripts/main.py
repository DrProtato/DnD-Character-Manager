#main script file

#importing other functions and sections
import SectionRandomManager
import Section1
import Section2
import Section5
import Section8

def tryAgain():
    print("Try again, make sure you typed your response correctly.")

def lineBreak():
    print("\n---------------------------------------------------\n")

def startSequence():
    lineBreak()
    print("Hello there and welcome to the D%D Character creator!")
    print("This program is here to help you create a character for your next campaign.")

    while True:
        startresponse = input("Type 'start' to get started, or type 'exit' to exit the program")
        if startresponse == "start":
            break
            #exits loop so then the next function can begin
        elif startresponse == "exit":
            exit()
        else:
            tryAgain()

def findSectionToRand():
    lineBreak()
    while True:
        print("There are 8 sections that can be randomised.")
        print("(Note: only a few sections are available in this build.)")
        print("The sections that are available are 1 (class and race), 2 (stat roll), 5 (spells) and 8 (name).")
        print("Which sections do you want to randomise?")
        response1 = input("Do you want to randomise all sections? (type 'yes' or 'no')")
        if response1 == "yes":
            #rand all sections
        elif response1 == "no":
            repsonse2 = input("Type '1,2,3,..' for certain sections that you want to be randomised.")
            #strip and append to rand sections array
            #whatever is left needs to be append to manual list
            SectionRandomManager.randomSpecific(#need stuff in here)
            break
        else:
            tryAgain()

startSequence()
findSectionToRand()
