"""
Write a Python program to copy the contents of above file “Medicine.csv” into “Temp.csv”, but with a
different delimiter.
"""
import csv
with open("Medicine.csv", "r") as fh:
    creader = csv.reader(fh)
    with open("Temp.csv", "w", newline='') as new_file:
        cwriter = csv.writer(new_file, delimiter='\t')
        cwriter.writerows(creader)
