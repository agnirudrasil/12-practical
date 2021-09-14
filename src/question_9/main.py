# Find Function
def find_from_file(rollno):

    # opening file
    with open("question_9.bin","rb") as file:
        entries_list = []
        counter = 0
        entries = file.read().decode()
        entry = entries.split("\n")
        # appending data to list
        for i in entry:
            entries_list.append(str(i).split(','))
            counter += 1
        entries_list.pop()
        counter -= 1
        print(f"Number of entries: {counter}")
        # iterating over the list to find name
        a = 0
        for items in entries_list:
            if str(rollno) == items[0]:
                a = 1
                print(f"Roll.No {rollno} belongs to:{items[1]}")
        if a == 0:
            print("Roll.No not found") 

# Details
operation_enter_data = str(input("Do you want to enter data into the file? Y/N: ")).upper()
if operation_enter_data == "Y":
    rollno = int(input("Enter your roll number: "))
    name = str(input("Enter your name: "))
    marks = float(input("Enter marks: "))

    # File Operations
    try:
        with open("question_9.bin","ab") as file:
            new_entry = f"{rollno}, {name}, {marks}\n"
            convert = bytes(new_entry, 'utf-8')
            file.write(convert)
            print("File updated...")
    except Exception as e:
        print(e)

elif operation_enter_data == "N":

    # Calling Find Function
    operation_find_data = str(input("Do you want to find an entry in the file: Y/N: ")).upper()

    if operation_find_data == "Y":
        rollno = int(input("Enter roll number: "))
        find_from_file(rollno)

    elif operation_find_data == "N":
        print("Okay, exiting program now...")
        exit()

    else:
        print("Please enter a valid option")

else:
    print("Please enter a valid option")