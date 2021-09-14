"""
Write a program to read following details of sports’ performance (sport_name, competitions, prizes_won)
of an Institution and store into a SPORTS.CSV file delimited with tab character. And also read & display the
contents of SPORTS.CSV.
"""
import csv

with open("SPORTS.CSV", "r") as f:
    creader = csv.reader(f, delimiter='\t')
    for rec in creader:
        print(rec)
