import csv
import os

directory = "C:\\Programming\Examples\CSVMerge"


for i in range(10):
    filepath = directory+"\\"+"File "+str(i)+".csv"
    with open(filepath, 'w', newline = '') as csvfile:
        columns = ["A","B","C","D","F","G"]
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        for j in range(100):
            writer.writerow([str(i)+c+str(j) for c in columns])

for i in range(10,12):
    filepath = directory+"\\"+"File "+str(i)+".csv"
    with open(filepath, 'w', newline = '') as csvfile:
        columns = ["AA","BB","CC","DD","FF","GG"]
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        for j in range(100):
            writer.writerow([str(i)+c+str(j) for c in columns])

for i in range(12,14):
    filepath = directory+"\\"+"File "+str(i)+".csv"
    with open(filepath, 'w', newline = '') as csvfile:
        columns = ["A","B","C","D","F"]
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        for j in range(100):
            writer.writerow([str(i)+c+str(j) for c in columns])

    
print("done")
