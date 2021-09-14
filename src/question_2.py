#Random n digit number
import random

def get_random_n(n):
    return random.randint(10**(n-1), 10**(n) -1)
print(get_random_n(3))
