#main script file to start the program
import tkinter as tk

mainWindow = tk.Tk()
currentFrame = tk.Frame(width=200, height=200, background="#D3D3D3")

def startFrame(currentFrame, window):
    currentFrame.destroy()
    currentFrame = tk.Frame(width=400, height=400, background="#FFFFFF")
    title = tk.Label(window, text="Welcome to the D&D Character Creator")
    title.pack()
    startB = tk.Button(window, text="Create a new character", command=preStart(currentFrame, window))
    startB.pack()
    startB.place()
    window.mainloop()

def preStart(currentFrame, workingwindow):
    currentFrame.destroy()
    currentFrame = tk.Frame(width=400, height=400, background="#AAAAAA")
    hey = tk.Label(workingwindow, text="Hellow there")
    hey.pack()
    hey.place()
    workingwindow.mainloop()



startFrame(currentFrame, mainWindow)