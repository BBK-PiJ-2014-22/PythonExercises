"""Todo List:

1) Refactor so this uses functions
2) Change to use a separate header file
3) Ignore files that don't match to the headers
4) Create command line user interface
5) Allow deviation from default file names and encoding

"""


import csv
import os

directory = "C:\\Users\Jamie\Downloads\Companies House Data"
files = os.listdir(directory)


#Assign the headings

filepath = directory + '\\' + files[0]
newfilepath = directory  + '\combined.csv'

with open(filepath, 'r', newline = '', encoding="utf8") as csvfile:
    with open(newfilepath,'w', newline = '') as newfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(newfile)
        writer.writerow(next(reader))


#Combine files
for file in files:
    filepath = directory + '\\' + file
    with open(filepath, 'r', newline = '', encoding="utf8") as oldfile:
        with open(newfilepath, 'a', newline = '') as newfile:
            reader = csv.reader(oldfile, delimiter= ",")
            writer = csv.writer(newfile, delimiter= ",")
            next(reader) #skips heading
            data = [row for row in reader]
            writer.writerows(data)

print('done')

