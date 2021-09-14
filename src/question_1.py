#Factorial of a number

def factorial(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a
        

#Sum of the first n even numbers
def sum_first_even(n):
    return (n*(n+1))

n=int(input("Enter a number: "))
print(f"Factorial of {n} is: {factorial(n)}")

n=int(input("Enter a number : "))
y=sum_first_even(n)
print("Sum of first ",n," even numbers is = ",y)
