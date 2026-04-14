import unittest
from valid_anagame_words import get_valid_word_list
from AnagramLookup import AnagramLookup


class TestBuildWordBank(unittest.TestCase):
    def setUp(self):
        self.letters1 = ["a", "b", "e", "d", "l"]
        self.letters2 = ["p", "o", "o", "l"]
        self.letters3 = ["x", "y", "z"]
        self.letters4 = ["a", "p", "p", "l", "e", "s", "t"]

    def test_0_type(self):
        """build_word_bank - return type should be a set"""
        corpus = ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
        explorer = AnagramLookup(corpus, self.letters1)
        val = explorer.word_bank
        self.assertIsInstance(
            val, set, "build_word_bank should set as its return type")

    def test_1_basic_example(self):
        """build_word_bank - basic example from docstring"""
        corpus = ["rat", "tar", "art", "bat", "tab", "cat", "at", "tart"]
        expected = {"rat", "tar", "art"}
        explorer = AnagramLookup(corpus, ["a", "r", "t"])
        actual = explorer.word_bank
        self.assertEqual(actual, expected,
                         f"Expected {expected} but got {actual}")

    def test_2_excludes_short_words_and_respects_counts(self):
        """build_word_bank - excludes words shorter than 3 and respects letter counts"""
        corpus = ["at", "to", "a", "be", "bed", "bee", "ebb"]
        # letters have only one 'e', so "bee" (needs two e's) should be excluded
        explorer = AnagramLookup(corpus, ["b", "e", "d"])
        expected = {"bed"}
        actual = explorer.word_bank
        self.assertEqual(actual, expected,
                         f"Expected {expected} but got {actual}")

    def test_3_duplicate_letters_allowed_when_provided(self):
        """build_word_bank - words requiring duplicate letters allowed only when letters include duplicates"""
        corpus = ["pool", "loop", "polo", "pol", "lop", "pools", "spool"]
        explorer = AnagramLookup(corpus, self.letters2)
        expected = {"pool", "loop", "polo", "pol", "lop"}
        actual = explorer.word_bank
        self.assertEqual(actual, expected,
                         f"Expected {expected} but got {actual}")

    def test_4_no_valid_words(self):
        """build_word_bank - when no words can be formed, return empty set"""
        corpus = ["cat", "dog", "fish"]
        explorer = AnagramLookup(corpus, self.letters3)
        expected = set()
        actual = explorer.word_bank
        self.assertEqual(actual, expected,
                         f"Expected empty set but got {actual}")

    def test_5_integration_with_valid_word_list(self):
        """build_word_bank - integration with actual valid word list: membership checks"""
        word_list = get_valid_word_list()
        explorer = AnagramLookup(word_list, self.letters4)
        bank = explorer.word_bank
        # Known words that should be possible with letters4 = ["a","p","p","l","e","s","t"]
        for w in ("apples", "apple", "pale", "leap"):
            self.assertIn(w, bank, f"Expected '{w}' to be in the word bank")
        # Words that require letters not present should not be included
        for w in ("rat", "mouse", "zoo", "papal", "pplae", "at"):
            self.assertNotIn(
                w, bank, f"Did not expect '{w}' to be in the word bank")


if __name__ == "__main__":
    unittest.main()
