"""
A binary file “STUDENT.DAT” has structure (admn_no, name, percentage).Write a function CountRec()
that would read contents of the file “STUDENT.DAT” and display the details of those students
whose percentage is above 75. Also display number of students scoring above 75%.
"""

import pickle


def CreateFile():
    """
    The function CreateFile() is to generate the binary file, do not write in your record
    """
    ch = 'y'
    with open("STUDENT.DAT", "ab") as f:
        data = {}
        while ch == 'y':
            adm_no = input("Please Admission number: ")
            name = input("Please enter the name of the student: ")
            percentage = float(input("Please enter percentage: "))
            data['admn_no'] = adm_no
            data['name'] = name
            data['percentage'] = percentage
            pickle.dump(data, f)
            ch = input("Want to add more records?(y/N): ").lower()


def CountRec():
    count = 0
    total_rec = 0
    try:
        with open("STUDENT.DAT", "rb") as f:
            while True:
                data = pickle.load(f)
                total_rec += 1
                print(data)
                if float(data['percentage']) >= 75:
                    count += 1
    except FileNotFoundError:
        print("File not found")
        print("Exiting...")
        exit(-1)
    except EOFError:
        return count, total_rec - count


# Driver Code
above_75, below_75 = CountRec()
print("Total students scoring >= 75% = {} and Total students score <= 75% = {}".format(
    above_75, below_75))
