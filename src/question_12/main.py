"""
Write a program to create a binary file called emp.dat and write into it the employee details of in the form
of dictionaries. Write the function to increase the Salary of the employee by 5000 for the empNo “123”.
For Ex. D= {empNo:"123", ename:"Ajay”, Salary: 50000}
"""

import pickle
from random import choice, randint

names = ["Ram", "Ramesh", "Rohan", "Sai",
         "Jack", "Joe", "Oliver", "Robert", "Noah"]


"""
Create file emp.dat
"""

with open("emp.dat", "wb") as f:
    data = [{"empNo": randint(100, 999),
                  "ename": names[i],
                  "Salary": randint(10000, 99999)}
                for i in range(9)]
    data.append({"empNo":123, "ename": "Ajay", "salary":5000})
    pickle.dump(data, f)

"""
Read file emp.data
"""

with open("emp.dat", "rb+") as f:
    data = pickle.load(f)
    for i, entry in enumerate(data): #enumerate gives the index of list as first variable and the item at that index as the second variable
        if entry["empNo"] == 123: 
                data[i]["salary"] += 5000
                break
    f.seek(0)
    pickle.dump(data, f)
                

