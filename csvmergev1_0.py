"""Todo List:

1) Refactor so this uses functions
2) Change to use a separate header file
3) Ignore files that don't match to the headers
4) Create command line user interface
5) Allow deviation from default file names and encoding

"""


import csv
import os
import shutil


#Assign the headings
def getHeaders(directory, file, result="headers.csv"):
    filepath = directory + '\\' + file
    newfilepath = directory  + '\\'+result

    with open(filepath, 'r', newline = '', encoding="utf8") as csvfile:
        with open(newfilepath,'w', newline = '', encoding="utf8") as newfile:
            reader = csv.reader(csvfile)
            writer = csv.writer(newfile)
            writer.writerow(next(reader))


#Combine files
def combineFiles(directory, headers="headers.csv", encoding="utf8", output="combined.csv"):
    files = os.listdir(directory)
    files.remove(headers)
    headers = directory+'\\'+headers
    output = directory+'\\'+output
    shutil.copyfile(headers, output)
    failed = []
    validheaders = ""
    
    with open(headers,'r', newline = '', encoding=encoding) as headerfile:
        headerreader = csv.reader(headerfile)
        validheaders = next(headerreader)
   
    for file in files:
        filepath = directory + '\\' + file
 
        with open(filepath, 'r', newline = '', encoding=encoding) as oldfile:
            with open(output, 'a', newline = '') as newfile:
                reader = csv.reader(oldfile, delimiter= ",")
                writer = csv.writer(newfile, delimiter= ",")
                fileheaders = next(reader)
                if fileheaders == validheaders:
                    data = [row for row in reader]
                    writer.writerows(data)
                else:
                    failed.append(file)
    return failed            

directory = "C:\\Programming\Examples\CSVMerge\\No Header Match"

print(getHeaders(directory, "File 0.csv"))
print(getHeaders(directory, "File 0.csv", result="otherHeaders.csv"))

print(combineFiles(directory))
print(combineFiles(directory, headers="otherHeaders.csv", output="combined2.csv"))

    
print('done')

