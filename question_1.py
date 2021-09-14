#Factorial of a number
from functools import lru_cache

@lru_cache(maxsize=300)
def factorial(n):
    if n == 0:
        return 1
    return n* factorial(n-1)

#Sum of the first n even numbers
def sum_first_even(n):
    return (n*(n+1))


#alterate

#part 1
def factorial(a) :
    b=1
    while(a!=0) :
        b*=a
        a-=1
    return b

a=int(input("Enter a number : "))
c=factorial(a)
print("Required factorial is = ",c)

#part 2
def sum_of_even(n) :
    w=0
    x=0
    while(w<n) :
        x+=2*w
        w+=1
    return x

n=int(input("Enter a number : "))
y=sum_of_even(n)
print("Sum of first ",n," even numbers is = ",y)
