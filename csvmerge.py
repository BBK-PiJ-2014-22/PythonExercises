import csv
import os

directory = "C:\\Users\Jamie\Downloads\Companies House Data"
files = os.listdir(directory)


#Assign the headings

filepath = directory + '\\' + files[0]
newfilepath = directory  + '\combined.csv'

with open(filepath, 'r') as csvfile:
    with open(newfilepath,'w') as newfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(newfile)
        writer.writerow(next(reader))

#Combine files
#for file in files:
filepath = directory + '\\' + 'BasicCompanyData-2015-02-01-part5_5.csv'
with open(filepath, 'r') as oldfile:
    with open(newfilepath, 'a') as newfile:
        reader = csv.reader(oldfile, delimiter= ",")
        writer = csv.writer(newfile, delimiter= ",")
        next(reader) #skips heading
        while reader:
            writer.writerow(next(reader))
   

print('done')
