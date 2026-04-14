import unittest
from AnagramLookup import AnagramLookup
from valid_anagame_words import get_valid_word_list


class TestEx1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        '''Runs once, before any tests are run'''
        pass

    def setUp(self):
        # Runs before every test
        self.letters = ["p", "o", "t", "s", "r", "i", "a"]
        self.double_letters = ["p", "o", "l", "s", "r", "i", "o"]
        # Create explorers for the letter sets used in tests
        self.explorer = AnagramLookup(get_valid_word_list(), self.letters)
        self.explorer_double = AnagramLookup(
            get_valid_word_list(), self.double_letters)

    def test_0(self):
        """explorer.is_valid_anagram_pair -  Data Type"""
        pair = ("pot", "top")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertIsInstance(val, bool)

    def test_1(self):
        """explorer.is_valid_anagram_pair -  Basic True"""
        pair = ("pot", "top")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertEqual(val, True)

    def test_2(self):
        """explorer.is_valid_anagram_pair -  Basic False"""
        pair = ("pot", "rat")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertEqual(val, False)

    def test_3(self):
        """explorer.is_valid_anagram_pair -  Identical Words with Mixed Capitalization"""
        pair = ("pot", "POT")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertEqual(val, False)

    def test_4(self):
        """explorer.is_valid_anagram_pair -  Nearly Identical Words"""
        pair = ("pot", "pit")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertEqual(val, False)

    def test_5(self):
        """explorer.is_valid_anagram_pair -  Valid anagrams, but not in letters"""
        pair = ("baste", "beast")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertEqual(val, False)

    def test_6(self):
        """explorer.is_valid_anagram_pair -  1 letter words"""
        pair = ("t", "t")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertEqual(val, False)

    def test_7(self):
        """explorer.is_valid_anagram_pair -  Almost Anagrams: Plural, all leters present in letters"""
        pair = ("pot", "pots")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertEqual(val, False)

    def test_8(self):
        """explorer.is_valid_anagram_pair -  Two Empty Strings"""
        pair = ("", "")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertEqual(val, False)

    def test_9(self):
        """explorer.is_valid_anagram_pair - Double letter in word but not letters list"""
        pair = ("loop", "pool")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertEqual(val, False)

    def test_10(self):
        """explorer.is_valid_anagram_pair - Double letter in word and also letters list"""
        pair = ("loop", "pool")
        val = self.explorer_double.is_valid_anagram_pair(pair)
        self.assertEqual(val, True)

    def test_11(self):
        """explorer.is_valid_anagram_pair -  2 letter words"""
        pair = ("on", "no")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertEqual(val, False)

    def test_12(self):
        """explorer.is_valid_anagram_pair - Anagrams, but not in valid_word_list()"""
        pair = ("sria", "airs")
        val = self.explorer.is_valid_anagram_pair(pair)
        self.assertEqual(val, False)


if __name__ == '__main__':
    unittest.main()
