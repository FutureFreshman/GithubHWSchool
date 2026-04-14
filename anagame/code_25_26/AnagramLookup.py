class AnagramLookup:
    def __init__(self, all_words: list[str], letters: list[str]):
        '''Initializes the AnagramLookup object by building a word bank and an anagram hash table.

            Args:
              all_words (list): A list of all acceptable words
              letters (list): A list of letters from which the anagrams should be created
        '''
        self.word_bank = self.build_word_bank(all_words, letters)
        self.anagram_hash_table = self.build_lookup_dict()

    def build_word_bank(self, all_words: list[str], letters: list[str]) -> set:
        '''Creates a word bank made up of all valid words that can be made from the given letters. Words with fewer than
            3 letters are excluded, and letters can only be used as many times as they appear in the letters list.

            Args:
              all_words (list): A list of all acceptable words
              letters (list): A list of letters from which the anagrams should be created

            Returns:
              set: All valid words that can be formed from the given letters

            Examples
            ----------
            >>> build_word_bank(["rat", "tar", "art", "bat", "tab", "cat", "at", "tart"], ["a", "r", "t"])
            {"rat", "tar", "art"}
        '''
        # BEGIN SOLUTION
        '''
        rearrange letters in the word first alphabetical order then when you have a word you compare it to every single one int he second word
        '''
        

        # END SOLUTION

    def build_lookup_dict(self) -> dict:
        '''Creates a hash table (dictionary) mapping letter combinations to all words in the word bank
            that can be formed from those letters (using either sorting or prime hashing for keys).

            Returns:
                dict: Returns a dictionary mapping sorted letter combinations to lists of words
                        that can be formed from those letters.
        '''
        # BEGIN SOLUTION

        # END SOLUTION

    def get_all_anagrams(self) -> set:
        '''Creates a set of all unique words in the word bank that have at least one anagram.
           Words which can't create any anagram pairs should not be included in the set.
           Uses the hash table for efficiency.

            Examples
            word_bank: ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
              -> {"abed",  "abled", "baled", "bead", "blade"}

            Returns:
              set: all unique words that form part of at least 1 anagram pair
        '''
        # BEGIN SOLUTION

        # END SOLUTION

    def is_valid_anagram_pair(self, pair: tuple[str]) -> bool:
        '''Checks whether a pair of words belong to the word bank and are anagrams of each other.

            Args:
                pair (tuple): Two strings representing the pair. Each string is a lowercase word with a-z only

            Returns:
                bool: Returns True if the word pair fulfills all validation requirements, otherwise returns False
        '''
        # BEGIN SOLUTION

        # END SOLUTION


if __name__ == "__main__":
    words1 = [
        "abed", "abet", "abets", "abut", "acme", "acre", "acres", "actors", "actress", "airmen", "alert", "alerted", "ales", "aligned", "allergy", "alter", "altered", "amen", "anew", "angel", "angle", "antler", "apt",
        "bade", "baste", "bead", "beast", "beat", "beats", "beta", "betas", "came", "care", "cares", "casters", "castor", "costar", "dealing", "gallery", "glean", "largely", "later", "leading", "learnt", "leas", "mace", "mane",
        "marine", "mean", "name", "pat", "race", "races", "recasts", "regally", "related", "remain", "rental", "sale", "scare", "seal", "tabu", "tap", "treadle", "tuba", "wane", "wean"
    ]
    words2 = ["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops"]

    letters = ["l", "o", "t", "s", "r", "i", "a"]

    lookup = AnagramLookup(words1, letters)
