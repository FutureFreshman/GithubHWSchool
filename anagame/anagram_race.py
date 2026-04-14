import itertools

def clean_word(word):
    wordlower = word.lower()
    wordlower = wordlower.strip()
    cleanerword = ""
    for i in wordlower:
        if i.isalpha():
            cleanerword += i
    return cleanerword


def basic_checks(word1: str, word2: str)-> tuple[bool, str, str]:
    '''Performs checks and processing needed by each is_anagram() approach.
       
       Removes non-alphabetical characters and converts both words to lower-case,
       then performs basic checks to ensure that the two words:
        - are not the same word
        - are at least 3 letters long
        - have the same length
x
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
    ### BEGIN SOLUTION
    basiccheckpass = True
    if word1 == word2:
        basiccheckpass = False
    if len(word1) != len(word2):
        basiccheckpass = False
    if len(word1) < 3 or len(word2)<3:
        basiccheckpass= False
    return (basiccheckpass, word1, word2)
    
    ### END SOLUTION 
   
def make_exhaustive_words(word1):
    endlist = []

    for i in range (0,len(word1)):
        if len(word1) == 1:
            return list(word1)
        currentletter = word1[i]
        #start stop step: start defaults to 0, stop defaults to end, so i+1 is the character in front to end and 0 to i is the frist index to i, exclusive
        currentstring = word1[:i] + word1[i+1:]

        stringtwo = make_exhaustive_words(currentstring)
        
        for j in stringtwo:
            addstrings = currentletter + j
            #Make sure that 
            endlist.append(addstrings)
        
    return endlist

def is_anagram_exhaustive(word1: str, word2: str)->bool:
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
    ### BEGIN SOLUTION

    all_permutations = make_exhaustive_words(word1)
    
    if (word2 in all_permutations):
        return True
    else:
        return False
        
    
    
    ''' Generate ALL possible arrangements, also known as permutations, of the word, using lists of strings
This also checks itself
For each permutation in the list, check if the permutation equals the word (the word you are comparing against the first word for anagram-checking) 
Keep going until you reach the second word. If you never do, simply return False (always returns boolean T/F)
'''
    ### END SOLUTION 

def is_anagram_checkoff(word1: str, word2: str)->bool:
    '''Check if two words are anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    if len(word1) != len(word2) or word1 == word2:
        return False
    
    lettersforchecking = list(word2)

    for i in word1:
        if i in lettersforchecking:
            lettersforchecking.remove(i)
        else:
            return False
    return True
    
    

    ''' Convert word2 into a list of string characters
Check each letter in word1 if that letter is in the word2 list (likely using a loop to check each letter) 
If it is, remove that letter from the word2 list to check it off
If all the letters are checked off (all letters from word1 are in word2/anagram found), return True and if not, return False (always return boolean)

'''
    ### END SOLUTION 

def is_anagram_lettercount(word1: str, word2: str)->bool:
    '''Check if two words are anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    if len(word1) != len(word2) or word1 == word2:
        return False
    
    firstcount = {}
    secondcount = {}

    for i in word1:
        if i in firstcount:
            firstcount[i] += 1
        else:
            firstcount[i] = 1
    
    for i in word2:
        if i in secondcount:
           secondcount[i] += 1
        else:
            secondcount[i] = 1
    if firstcount == secondcount:
        return True
    else:
        return False
    
    '''Create two dictionarieis and count the frequency of each character in the word/string
For each letter in the first word, increment its respective count in its respective dictionary; do the same for the second word
If the dictionaries/counts are the same for the first and second word, return True. If not, return False
'''
    ### END SOLUTION 

def is_anagram_sort_hash(word1: str, word2: str)->bool:
    '''Check if two words are anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    if len(word1) != len(word2) or word1 == word2:
        return False
    
    word1sort = sorted(word1)
    word2sort = sorted(word2)

    if word1sort == word2sort:
        return True
    else:
        return False
    ### END SOLUTION 

ch_to_prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101}

def is_anagram_prime_hash(word1:str, word2:str)->bool:
    '''Check if two words are anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    if len(word1) != len(word2) or word1 == word2:
        return False
    
    firstproduct = 1
    secondproduct = 1

    for i in word1:
        firstproduct *= ch_to_prime[i]
    
    for i in word2:
        secondproduct *= ch_to_prime[i]
    
    if firstproduct == secondproduct:
        return True
    else:
        return False
    ### END SOLUTION 

if __name__ == "__main__":
    algorithms = [is_anagram_exhaustive, is_anagram_checkoff, is_anagram_lettercount, is_anagram_sort_hash, is_anagram_prime_hash]
    word1 = "beast"
    word2 = "baste"

    for algorithm in algorithms:
        print(f"== {algorithm.__name__} ==")
        print("beast, baste: ", algorithm("beast", "baste"))
        # Add your own additional tests...

        print()