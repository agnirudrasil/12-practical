'''
Question 10
A binary file “Book.dat” has structure [bookno, bookname, author, price]. 
Write a user defined function CreateFile() to input data for a record and add to Book.dat.
Write a function CountRec(Author) which accepts Author name as parameter, 
count and return number of books by the given Author are stored in the binary file “Book.dat”.
'''
import pickle


def CreateFile():
    ch = 'y'
    with open("Book.dat", "ab") as f:
        data = {}
        while ch == 'y':
            bookno = input("Please enter Book number: ")
            bookname = input("Please enter the name of the book: ")
            author = input("Please enter the name of the author: ")
            price = input("Please enter the price of the book: ")
            data['bookno'] = bookno
            data['bookname'] = bookname
            data['author'] = author
            data['price'] = price
            pickle.dump(data, f)
            ch = input("Want to add more records?(y/N): ").lower()


# Driver Code
print(CreateFile())


def CountRec(author: str):
    count = 0
    try:
        with open("Book.dat", 'rb') as f:
            while True:
                data = pickle.load(f)
                if data['author'] == author:
                    count += 1
    except FileNotFoundError:
        CreateFile()
        CountRec(author)
    except EOFError:
        return count


# Driver Code
author = input("Please Enter Name of the author")
print(CountRec(author))
