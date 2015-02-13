import easygui
from csvmergev1_0 import getHeaders, combineFiles

def modifyDefaults():
    easygui.msgbox("Not ready yet(MD)")

def selectFolder():
    easygui.msgbox("Please select folder")
    return easygui.diropenbox("Please select folder with files to merge")

def displayHelp():
    easygui.msgbox("Not ready yet (HE)")

def execute(folder, settings=[True]):

    if settings[0]:
        combined, message = combineFiles(folder)
        if combined:
            easygui.msgbox("Merge complete. The following files could not be merged as they did not match to headers:\n"+message)
        else:
            easygui.msgbox("No header file exists. Please try again.")
             





  
def introduction():
    choice = easygui.buttonbox("""Welcome to CSV Merge.

    This program will merge all CSV files in a single file. Default settings require a headers.csv file, and will create a combined.csv file, encoding in UTF-8

    To proceed using default settings hit "Default". To modify settings hit "Modify". If you are unsure, hit "Help"
    """, "CSV Merge Launcher", ["Default", "Modify", "Help"])
   

    if choice == "Default":
        folder = selectFolder()
        execute(folder)

        
        



print(introduction())


