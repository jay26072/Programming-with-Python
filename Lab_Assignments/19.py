# 19.Write a program to process CSV file using CSV module.


import csv

with open('student.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)