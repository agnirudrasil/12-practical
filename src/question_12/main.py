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
    ch = randint(0, 9)
    pickle.dump([{"empNo": "123" if i == 3 else str(randint(100, 999)),
                  "ename": "Ajay" if i == 3 else choice(names),
                  "Salary": randint(10000, 99999)}
                for i in range(10)], f)

try:
    with open("emp.dat", "rb+") as f:        
        datas = pickle.load(f)
        for data in datas:
            rpos = f.tell()
            print(data)
            if data["empNo"] == "123":
                data['Salary'] += 5000
                f.seek(rpos)
                pickle.dump(data, f)
except EOFError:
    print("")
