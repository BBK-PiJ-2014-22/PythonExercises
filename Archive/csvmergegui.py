import easygui
import tkinter
import os
from csvmergev1_0 import getHeaders, combineFiles

class Application(tkinter.Frame):
    
    def __init__(self, master):
        super(Application, self).__init__(master)

        self.settings= {"encoding": "UTF-8"       ,
                        "headers" : "headers.csv" ,
                        "output"  : "combined.csv"}
   
        self.grid()
        self.create_widgets()
                    

    def create_widgets(self):
        
        self.label = tkinter.Label(self, text="Welcome to CSV Merger")
        self.label.grid(columnspan = 2, sticky="W")

        #Settings buttons
        self.encoding = tkinter.Button(self, text=self.settings["encoding"])
        self.encoding.grid(row = 3, column = 0)
        self.header = tkinter.Button(self, text=self.settings["headers"])
        self.header.grid(row = 3, column = 1)
        self.output = tkinter.Button(self, text=self.settings["output"])
        self.output.grid(row = 3, column = 2)
        self.location = tkinter.Button(self, text="Select Location of CSVs to merge",
                                       command = lambda: self.selectFolder("Please select location of CSVs to merge"))
        self.location.grid(row = 4, column = 0, columnspan = 3, sticky = "S")
     
        self.merge = tkinter.Button(self, text="Merge CSVs"
                                    command = lambda: self.execute())
        self.merge.grid(row = 5, column = 1)
        self.help= tkinter.Button(self, text="Help")
        self.help.grid(row = 0, column = 3)

    def selectFolder(self, message):
        self.settings["Location"] = easygui.diropenbox(message)
        self.location["text"]  = self.settings["Location"]


    def execute(self):
        

   




##Begin old code

def modifyDefaults():
    easygui.msgbox("Not ready yet(MD)")



def displayHelp():
    easygui.msgbox("Not ready yet (HE)")

     
 
def introduction():
    choice = easygui.buttonbox("""Welcome to CSV Merge.

    This program will merge all CSV files in a single file. Default settings require a headers.csv file, and will create a combined.csv file, encoding in UTF-8

    To proceed using default settings hit "Default". To modify settings hit "Modify". If you are unsure, hit "Help"
    """, "CSV Merge Launcher", ["Default", "Modify", "Help"])
   

    if choice == "Default":
        folder = selectFolder()
        execute(folder)

##End old code        



#main

root = tkinter.Tk()
root.title("CSV Merger")
root.geometry("320x120")
application = Application(root)
root.mainloop()

