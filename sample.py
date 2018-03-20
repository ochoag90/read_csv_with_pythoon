import csv

with open('example2.txt', newline='') as f:
    reader = csv.reader(f)
    array = []
    for row in reader:
        array.extend([row])
        print(array)
        

