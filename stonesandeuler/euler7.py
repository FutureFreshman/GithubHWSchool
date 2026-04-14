import math

def is_prime(n: int)-> bool:
    if n<2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    sqrty = (int(math.sqrt(n)))+1
    for i in range (3, sqrty, 2):
        if n% i == 0:
            return False
    return True

def get_nth_prime(n:int)-> int:
    ticker=1
    countprimes = 0
    still_run = True
    while still_run:
        if is_prime(ticker)==True:
            countprimes+=1
        
        if countprimes==n:
            still_run = False
            return ticker
        ticker+=1
print(get_nth_prime(10001))

def check_sqrt(n:int)->bool:
    if n<0:
        return False 
    #BEFORE YOU SQUARE ROOT BC MATH.ISQRT CANT SQRT NEGATIVE
    sqrty = (math.isqrt(n))
    
    #remember to handle edge cases!
    if sqrty ** 2 == n:
        return True
    else:
        return False

print(check_sqrt(6))
print(check_sqrt(0))
print(check_sqrt(1))
print(check_sqrt(100))
print(check_sqrt(-5))
print("Expected False, True, True, True, False")