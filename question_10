#first part
def CreateFile():
    import pickle
    f=open('books.txt','wb')
    d={}
    ans='y'
    while ans=='y':
        book_no=input('enter book number: ')
        book_name=input('enter book name: ')
        author=input('enter author: ')
        price= input('enter price: ')
        d['book number']=book_no
        d['book name']=book_name
        d['author']=author
        d['price']=price
        pickle.dump(d,f)
        ans=input('do you wanna continue(y/n): ')

