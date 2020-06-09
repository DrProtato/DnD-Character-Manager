#naming script and section
#this page includes a field where the user can enter a name
#as well as randomise the name (in case the user wants to randomise it a few times)
#will display the name and have a confirm button
#the displayed name will first be a randomised name, the user can press
#a random name button to randomise it

import tkinter as tk
import random

nameWindow = Frame()

titleText = tk.Text(text="Type a name or generate a random one.")

nameUser = tk.Entry(exportselection=0)


#randomised name there when user arrives on page
#pressing randomise button should change the name to the new name
#all of this is seperate to the user entered name section
nameText = tk.Text(text=randomName())

nameList = []

def randomName():
	randNum = random.randint(0,...)


