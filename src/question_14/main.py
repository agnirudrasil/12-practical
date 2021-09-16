"""
Write a python program to create CSV file and store empno,name,salary in it. Take empno from the user
and display the corresponding name, salary from the file. Display an appropriate message if the empno is
not found.
"""
import csv


def create_csv():
    with open("employee.csv", "w", newline='') as f:
        cwriter = csv.writer(f)
        ch = "y"
        cwriter.writerow(["empno", "name", "salary"])
        while ch == 'y':
            empno = input("Please enter employee number: ")
            name = input("Please enter employee name: ")
            salary = input("Please enter employee salary: ")
            cwriter.writerow([empno, name, salary])
            ch = input("Do you want to add more records?(y/N) ").lower()


# Driver Code
create_csv()


def find_employee(empno):
    try:
        with open("employee.csv", "r") as f:
            creader = csv.reader(f)
            for rec in creader:
                if rec[0] == empno:
                    return rec[-2:]
        return
    except FileNotFoundError:
        print("File not found")
        exit()


# Driver Code
empno = input("Please enter employee number to find: ")
results = find_employee(empno)
if results is not None:
    print(
        f"Name of the employee is {results[0]} and their salary is {results[1]}")
else:
    print("Employee with than employee number not found")
