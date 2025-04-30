# 18.Write a program to read CSV file and generate output using HTML table. 

import csv

html = '<table border="1" style="width:100%">'
with open('student.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        html += '<tr>'
        for x in row:
            html += '<td>' + x + '</td>'
        html += '</tr>'
html += '</table>'

with open('output.html','w') as f:
    f.write(html)
    f.close()
print("HTML table generated successfully!")