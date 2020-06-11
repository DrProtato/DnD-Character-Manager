#main script file to start the program
import tkinter as tk

mainWindow = tk.Tk()

def startFrame(window):
    workingFrame = tk.Frame(width=400, height=400, background="#FFFFFF")
    workingFrame.pack()
    title = tk.Label(window, text="Welcome to the D&D Character Creator")
    title.pack()
    startB = tk.Button(window, text="Create a new character", command=lambda : preStart(workingFrame, window))
    startB.pack()
    startB.place()
    window.mainloop()

def preStart(aFrame, workingwindow):
    aFrame.pack_forget()
    aFrame.destroy()
    bFrame = tk.Frame(width=400, height=400, background="#AAAAAA")
    hey = tk.Label(workingwindow, text="Hellow there")
    hey.pack()
    hey.place()
    workingwindow.mainloop()

startFrame(mainWindow)