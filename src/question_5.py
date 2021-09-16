#Linear search
def linear_search(li,element):
    for i in range(len(li)):
        if li[i]==element:
            return i
    return -1

#Binary search
def binary_search(arr, x):
    arr.sort()
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1


n=input("Enter numeric values seperated by spaces : ").split()
r=int(input("Enter value required : "))
for i in range(0,len(n)) :
    n[i]=int(n[i])
print(binary_search(n,r))
print(linear_search(n,r))
