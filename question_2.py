#Random n digit number
import random

def get_random_n(n):
    return random.randint(10**(n-1), 10**(n) -1)
print(get_random_n(3))



#alternate
def n_digit_number(n) :
    return int(random.random()*(10**n))

n=int(input("Enter  a number : "))
a=n_digit_number(n)
print("The number generated is : ",a)
