import math

def get_menu_choice()->list:
    """Prompts the use to enter a valid menu choice to indicate which sequence should be generated.
       Also prompts the user to enter how many terms they would like to see.

       Returns:
          A list consisting of two items:
            - the number of terms in the sequence
            - a single letter indicating the desired type of sequence 
    """
    print("Enter your choice:")
    print("-----------------")
    print("  (O)dd Integers")
    print("  (M)ultiples")
    print("  (S)quare numbers")
    print("  (T)riangular numbers")
    print("  (A)rithmetic Sequence")
    print("  (F)ibonacci Sequence")
    choice = input("Which sequence would you like to generate?\n")

    while choice.lower() not in ["o", "m", "s", "t", "a", "f"]:
        choice = input("Which sequence would you like to generate?\n")

    n = int(input("How many terms would you like to see?\n"))

    return [n, choice.lower()] 


def positive_odds(n: int)->list:
    """Returns a list of the first n positive odd integers. 
        
        Args:
          n: The number of terms in the sequence to generate

        Returns:
          A list of n positive odd numbers

        Example
        --------
        >>> positive_odds(4)
        [1, 3, 5, 7]
    """
    odds = []
    for i in range(0, 2*n):
        if i % 2 == 1:
            odds.append(i)
    return odds

def positive_multiples(n: int, m: int)->list:
    """Returns a list of the first n positive integer multiples of m.
 
        Args:
          n: The number of terms in the sequence to generate
          m: The positive integer multiple 

        Returns:
          A list of n positive integer multiple of m

        Example
        --------
        >>> positive_multiples(4, 6)
        [6, 12, 18, 24]
    """
    if n <= 0 or m <= 0:
        return []
    multiples = []
    for i in range(1, n+1):
        multiples.append(m * i)
    return multiples


def square_numbers(n: int)->list:
    """Returns a list of the first n non-negative square integers.
 
        Args:
          n: The number of terms in the sequence to generate

        Returns:
          A list of n square numbers
          
        Example
        --------
        >>> square_numbers(4)
        [0, 1, 4, 9]
    """
    squares = []
    for i in range(n):
        squares.append(i*i)
    return squares

def triangle_numbers(n: int)->list:
    """Returns a list of the first n triangle numbers.
 
        Args:
          n: The number of terms in the sequence to generate

        Returns:
          A list of n triangle numbers
          
        Example
        --------
        >>> triangle_numbers(6)
        [1, 3, 6, 10, 15, 21]
    """

    triangle_numbers = []
    
    sum = 0
    for i in range(1, n + 1):
        sum += i
        
        triangle_numbers.append(sum)
    
    return triangle_numbers




def arithmetic_sequence(n: int, t1: int, t2: int)->list:
    """Returns a list of the first n terms of the arithmetic sequence defined by t1 and t2.
 
        Args:
          n: The number of terms in the sequence to generate
          t1: The first term in the sequence
          t2: The second term in the sequence

        Returns:
          A list of n terms in the arithmetic sequence defined by t1 and t2
          
        Example
        --------
        >>> arithmetic_sequence(4, 3, 7)
        [3, 7, 11, 15]
    """
    if n <= 0:
        return []
    seq = [t1]
    diff = t2 - t1
    for i in range(1, n):
        seq.append(seq[-1] + diff)
    return seq

def fibonacci_sequence(n: int)->list:
    """Returns a list of the first n terms of the fibonacci sequence.
 
        Args:
          n: The number of terms in the sequence to generate

        Returns:
          A list of n fibonnaci numbers
          
        Example
        --------
        >>> fibonacci_sequence(5)
        [1, 1, 2, 3, 5]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    n, choice = get_menu_choice()
  
    match choice:
        case "o":
            seq = positive_odds(n)
            label = "Positive Odd Integers"
        case "m":
            multiple = int(input("Which multiple would you like to use?"))
            seq = positive_multiples(n, multiple)
            label = "Positive Integer Multiples"
        case "s":
            seq = square_numbers(n)
            label = "Square Numbers"
        case "t":
            seq = triangle_numbers(n)
            label = "Triangle Numbers"
        case "a":
            term_1 = int(input("What is the first term of the arithmetic sequence?"))
            term_2 = int(input("What is the second term of the arithmetic sequence?"))
            seq = arithmetic_sequence(n, term_1, term_2)
            label = "Arithmetic Sequence"
        case  "f":
            seq = fibonacci_sequence(n)
            label = "Fibonacci Numbers"
        case _:
            seq = None

    print(f"The first {n} terms of the {label}: {seq}")