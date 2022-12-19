from tkinter import *
import os               
import re
import pandas as pd
import openpyxl

from tkinter import filedialog as fd

from Timeline import Timeline

class initTimetable:
    def __init__(self, root):
        

        self.master = root
        self.master.title("Timetable settings")

# labels
        self.lblDate = Label(self.master, text="Filename")
        self.lblDate.grid(row=0,column=0, sticky=W, padx=5)
# entryboxes
        self.eboxFilename = Text(self.master,width=20,height=1, font=('Chirp 14'))
        self.eboxFilename.grid(row=1, column=0, padx=5)
# buttons
        self.btnStart = Button(self.master, text="Start", command=self.bStart)
        self.btnStart.grid(row=2,column=0, sticky=E, padx=5)
        self.btnStart = Button(self.master, text="Open a File", command=self.bOpenFile)
        self.btnStart.grid(row=2,column=0, padx=5)
        self.btnQuit = Button(self.master, text="Quit", command=self.bQuit)
        self.btnQuit.grid(row=2,column=0, sticky=W, padx=5)

    def bStart(self):
        tk = Timeline(myTkRoot)
        tk.__init__(self)
    def bOpenFile(self):
        filename = fd.askopenfilename()
    def bQuit(self):
        pass

if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = initTimetable(myTkRoot)

    myTkRoot.mainloop()