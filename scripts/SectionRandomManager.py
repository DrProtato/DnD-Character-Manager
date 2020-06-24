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
completed = []
'''
def randSectionsFunc():
#goes up to 8 in sections
	randSections = input("Which sections do you want randomised? (x,y,z)")
	

anySecRand = input("Do you want to randomise any section? (Y/N)")
if anySecRand == "Y":
	randSectionsFunc()
else:
	manual = [1,2,3,4,5,6,7,8,9]
'''
def randomSpecific(manualArray = [], randomArray = []):
	completedArray = []
	while len(completedArray) < 8:
		print("man =" + str(manualArray))
		print("rand =" + str(randomArray))	
		print("comp =" + str(completedArray))
		try: 
			if manualArray[0] < randomArray[0]:
				manlen = len(manualArray)
				#send user to page
				#wait until completed
				i = 0
				completedArray.append(manualArray[i])
				while i < manlen - 1:
					print(manualArray)
					print(i)
					manualArray[i] = manualArray[i+1]
					i = i + 1
				del manualArray[-1] 
			else:
				randlen = len(randomArray)
				#randomise page
				i = 0
				completedArray.append(randomArray[i])
				while i < randlen - 1:
					print(randomArray)
					print(i)
					randomArray[i] = randomArray[i+1]
					i = i + 1
				del randomArray[-1]
		except:
			if len(manualArray) < len(randomArray):
				while len(randomArray) > 0:
					#randomise section
					completedArray.append(randomArray[0])
					del randomArray[0]
			else:
				while len(manualArray) > 0:
					#send user to section
					completedArray.append(manualArray[0])
					del manualArray[0] 

	print(str(completedArray) + "\nsorting is done")

randomSpecific(manual, randomising, completed)