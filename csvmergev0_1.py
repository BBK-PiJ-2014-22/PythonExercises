import csv
import os

directory = "C:\\Users\Jamie\Downloads\Companies House Data"
files = os.listdir(directory)


#Assign the headings

filepath = directory + '\\' + files[0]
newfilepath = directory  + '\combined.csv'

with open(filepath, 'r', newline = '') as csvfile:
    with open(newfilepath,'w', newline = '') as newfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(newfile)
        writer.writerow(next(reader))


#Combine files
#for file in files:
filepath = directory + '\\' + 'BasicCompanyData-2015-02-01-part5_5.csv'
with open(filepath, 'r', newline = '') as oldfile:
    with open(newfilepath, 'a', newline = '') as newfile:
        reader = csv.reader(oldfile, delimiter= ",")
        writer = csv.writer(newfile, delimiter= ",")
        next(reader) #skips heading
        data = [row for row in reader]
        writer.writerows(data)

print('done')
