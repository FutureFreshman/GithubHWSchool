def find_fibonacci_numbers(n):
    fiblist = [1,2]
    count = 0
    ticker = 0
    evensum = 0
    while count < n:
        i = fiblist[ticker] + fiblist[ticker+1]
        fiblist.append(i)
        count = i
        ticker +=1
        if i % 2 == 0:
            evensum += i
    return evensum

print(find_fibonacci_numbers(4000000)+2)

def get_factors(n):
    all_factors = []
    for i in range (1, n+1):
        if n% i == 0:   
            all_factors.append(i)
    return all_factors

def is_prime(n):
    if len(get_factors(n)) == 2:
        return True
    else:
        return False

def get_largest_prime_factor(n):
    factors_n = get_factors(n)
    primefac = []
    for i in factors_n:
        if is_prime(i) == True:
            primefac.append(i)
    return max(primefac)

print(get_largest_prime_factor(35))
