#this program asks the user if they want to randomise different sections

#this will use check boxes for which sections need to randomised, for now it will operate on text and commandline
'''an idea is to use 3 lists: one for completed sections, one for sections being randomised and 
one for what the user will do manually.  each section will be numbered 1 to x, where x is maximum number of sections
and each of the lists will have their elements compared, with the lowest element of both the randomised list and manual list 
are compared and the lower one will be done in the way that the user intended.  When done it will be added to the completed list,then 
the comparison happens again until all sections are done.'''
import random

manual = []
randomising = []

def randSectionsFunc():
	randSections = input("Which sections do you want randomised? (x,y,z)")

anySecRand = input("Do you want to randomise any section? (Y/N)")
if anySecRand == "Y":
	randSectionsFunc()
else:
	manual = [1,2,3,4,...]

	