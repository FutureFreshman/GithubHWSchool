import math
def get_factors(n: int) -> list:
    '''Generates a sorted list of unique integer factors for a given natural number

        Args:
            n (int): The natural number which should be factored

        Returns:
            list: a list of unique integer factors in sorted order

        Examples:
            >>> get_factors(6)
            [1, 2, 3, 6]
            >>> get_factors(17)
            [1, 17]
            >>> get_factors(36)
            [1, 2, 3, 4, 6, 9, 12, 18, 36]
            >>> get_factors(-2)
            []
    '''
    ### BEGIN SOLUTION
    listoffactors = []
    sqr = int((math.sqrt(n)))
    for i in range (1, sqr+1):
        if n % i == 0:
            listoffactors.append(i)
    return listoffactors
    ### END SOLUTION

def is_prime(n: int) -> bool:
    '''Determines whether a given integer is prime

       Args:
            n (int): The integer which should be tested

       Returns:
            bool: True if n is prime, False if n is not prime

       Examples:
            >>> is_prime(6)
            False
            >>> is_prime(11)
            True
    '''
    ### BEGIN SOLUTION
    listoffactors1 = []
    for i in range (1, n+1):
        if n % i == 0:
            listoffactors1.append(i)
            
    if len(listoffactors1) == 2:
        return True
    else:
        return False

    ### END SOLUTION 

def largest_prime_factor(n: int) -> int:
    '''Determines the largest prime factor of a given whole number > 1.

       Args:
            n (int): The whole number which should be considered
    
       Returns:
            int: The largest prime factor of n
                 If the given integer isn't a whole number > 1, returns 0

       Examples:
            >>> largest_prime_factor(6)
            3
            >>> largest_prime_factor(100)
            5
    '''
    ### BEGIN SOLUTION
    all_factors = get_factors(n)
    prime_list = []
    for i in all_factors: 
        if is_prime(i):
            prime_list.append(i)
    return max(prime_list)
        ### END SOLUTION    

if __name__ == "__main__":
    print("get_factors(25): ", get_factors(25))
    print("is_prime(17): ", is_prime(17))
    print("largest_prime_factor(35): ", largest_prime_factor(35))
    print("largest_prime_factor(num)", largest_prime_factor(600851475143))