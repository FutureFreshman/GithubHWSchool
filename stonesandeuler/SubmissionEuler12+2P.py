#num 1
import math
def get_sum(n):
    sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum +=i
    return sum

print(get_sum(1000))

#num 2

def find_fibonacci():
    listoffib = [1, 2]
    count = 0
    var1 = 0
    while count < 4000000:
        term = listoffib[var1] + listoffib[var1+1]
        if term<4000000:
            listoffib.append(term)
        var1 +=1
        count = term 
        
    return listoffib


def sum_fib_terms(listoffib):
    sumit = 0
    for item in listoffib:
        if item % 2 == 0:
            sumit += item
    return sumit

print(sum_fib_terms(find_fibonacci()))

#num 7

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


# num 10
# HITN USE factor fold
def is_prime_factor_fold(n: int) -> bool:
    '''Determines whether a given integer is prime
    '''
    ### BEGIN SOLUTION
    if n == 2:
        return True
    if n<2 or n%2==0:   
        return False
    upperlimitthing = math.isqrt(n)
    for i in range (3, upperlimitthing+1, 2):
        if n%i == 0:
            return False
    return True

def sum_primes_below_n(n: int) -> int:
    sum = 0
    for i in range (1, n):
        if is_prime_factor_fold(i) == True:
            sum +=i
    return sum

print(sum_primes_below_n(2000000))