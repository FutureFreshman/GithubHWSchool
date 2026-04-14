import itertools

# BEGIN SOLUTION

# END SOLUTION


def basic_checks(word1: str, word2: str) -> tuple[bool, str, str]:
    '''Performs checks and processing needed by each is_anagram() approach.

       Removes non-alphabetical characters and converts both words to lower-case,
       then performs basic checks to ensure that the two words:
        - are not the same word
        - are at least 3 letters long
        - have the same length

       Args:
         word1: The first word
         word2: The second word

       Returns:
         bool: False if the two words fail a basic check, True otherwise
         str: A lowercase version of word1 only containing A-Z, a-z
         str: A lowercase version of word2 only containing A-Z, a-z

       Examples:
        >>> basic_checks("baste2", "Beast")
        True, baste, beast
        >>> basic_checks("baste", "beasts")
        False, baste, beasts
    '''
    word1 = clean_word(word1)
    word2 = clean_word(word2)
    # BEGIN SOLUTION

    # END SOLUTION
    return (None, None, None)


def is_anagram_exhaustive(word1: str, word2: str) -> bool:
    '''Check if two words are anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    passed_checks, word1, word2 = basic_checks(word1, word2)

    if not passed_checks:
        return False
    # BEGIN SOLUTION

    # END SOLUTION


def is_anagram_checkoff(word1: str, word2: str) -> bool:
    '''Check if two words are anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    # BEGIN SOLUTION

    # END SOLUTION


def is_anagram_lettercount(word1: str, word2: str) -> bool:
    '''Check if two words are anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    # BEGIN SOLUTION

    # END SOLUTION


def is_anagram_sort_hash(word1: str, word2: str) -> bool:
    '''Check if two words are anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    # BEGIN SOLUTION

    # END SOLUTION


ch_to_prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
               'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
               'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
               'w': 83, 'x': 89, 'y': 97, 'z': 101}


def is_anagram_prime_hash(word1: str, word2: str) -> bool:
    '''Check if two words are anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    # BEGIN SOLUTION

    # END SOLUTION


if __name__ == "__main__":
    algorithms = [is_anagram_exhaustive, is_anagram_checkoff,
                  is_anagram_lettercount, is_anagram_sort_hash, is_anagram_prime_hash]
    word1 = "beast"
    word2 = "baste"

    for algorithm in algorithms:
        print(f"== {algorithm.__name__} ==")
        print("beast, baste: ", algorithm("beast", "baste"))
        # Add your own additional tests...

        print()
