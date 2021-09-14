#Linear search
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

#Binary search (array must be a sorted one)
def binary_search(arr,l,r,x):
    if r>=l:
        mid = l + (r-l)//2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr,l,mid-1,x)
        elif arr[mid] < x:
            return binary_search(arr,mid+1, r,x)
    return -1

#Adding a wrapper function because the question demands only list and search element to be passed in
def binary_search_main(arr, x):
    return binary_search(sorted(arr),0,len(arr)-1,x)




#alternate
def linear_search(list1,c) :
    for a in list1 :
        if a==c :
            return str(c)+" was found in the list via linear search "
            break
    else :
        return str(c) + " does not exist in list"


def binary_search(list1,c) :
    z=0
    list1.sort()
    while(z<(len(list1)/2)) :
        a=int((len(list1)/2))
        if c==list1[a] :
            return str(c)+" was found in the list via binary search "
            break
        elif (c>list1[a]) :
            list1=list1[a:len(list1)]
            binary_search(list1,c)
            z+=1
        elif (c<list1[a]) :
            list1=list1[0:a]
            binary_search(list1,c)
            z+=1
    else :
        return str(c) + " does not exist in list"

        
    
#__main__
n=input("Enter numeric values seperated by spaces : ").split()
r=int(input("Enter value required : "))
for i in range(0,len(n)) :
    n[i]=int(n[i])
print(binary_search(n,r))
print(linear_search(n,r))
















