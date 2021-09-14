#Linear search
def linear_search(li,element):
    index=-1
    for i in li:
        index+=1
        if i==element:
            return index
            break
    else:
        return 0

#Binary search
def binary_search(li, element):
    li.sort()
    start=0
    end=len(li)
    while True:
        index=(start+end)//2
        mid=li[index]

        if mid == element:            
            return index
        if mid<element:
            start+=1
        if mid>element:
            end-=1

        if start==end:
            return -1


n=input("Enter numeric values seperated by spaces : ").split()
r=int(input("Enter value required : "))
for i in range(0,len(n)) :
    n[i]=int(n[i])
print(binary_search(n,r))
print(linear_search(n,r))
















