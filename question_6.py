def generate(n=5):
    import random
    a=int(input("Enter base number : "))
    b=int(input("Enter ceiling number : "))
    for i in range(0,n) :
        x=round(a+(b-a)*random.random(),2)
        list1.append(x)
    print(list1)
    global val
   
    val=float(input("Enter value to be removed: "))
    temp(val)
       

def update(pos,num) :
    list1.insert(pos-1,num)
    print(list1)

def temp(val) :
    list1.remove(val)
    print(list1)
    global num
    global pos
    num=int(input("Enter value to be inserted : "))
    pos=int(input("Enter position from start of previous value (1 onward) : "))
    update(pos,num)


n=int(input("Enter length of list : "))
list1=[]
generate(n)
