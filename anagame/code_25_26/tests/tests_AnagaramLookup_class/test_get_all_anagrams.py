import unittest

from valid_anagame_words import get_valid_word_list
from AnagramLookup import AnagramLookup


class TestEx1(unittest.TestCase):
    def setUp(self):
        # Runs before every test
        self.letters1 = ["a", "b", "e", "d", "l"]
        self.letters2 = ["p", "o", "t", "s", "r", "i", "a"]
        self.letters3 = ["p", "o", "l", "s", "r", "i", "o"]
        self.entire_alphbet = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ] * 3

    def test_0(self):
        """explorer.get_all_anagrams -  Data Types"""
        corpus = ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
        student_explorer = AnagramLookup(corpus, self.letters1)
        val = student_explorer.get_all_anagrams()
        self.assertIsInstance(val, set, "get_all_anagrams should return a set")

    def test_1(self):
        """explorer.get_all_anagrams -  Basic Example in function comments"""
        corpus = ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
        expected = {"abed",  "abled", "baled", "bead", "blade"}

        student_explorer = AnagramLookup(corpus, self.letters1)
        actual = student_explorer.get_all_anagrams()

        self.assertEqual(
            actual, expected, f"Words that were in your set but not the expected set {actual.difference(expected)}\n Words that were in the expected set but not your set {expected.difference(actual)}")

    def test_2(self):
        """explorer.get_all_anagrams - No anagrams in corpus"""
        corpus = ["abed", "mouse", "rat", "cat", "tiger", "elephant", "stork"]
        expected = set()

        student_explorer = AnagramLookup(corpus, self.letters1)
        actual = student_explorer.get_all_anagrams()

        self.assertEqual(
            actual, expected, f"Words that were in your set but not the expected set {actual.difference(expected)}\n Words that were in the expected set but not your set {expected.difference(actual)}")

    def test_3(self):
        """explorer.get_all_anagrams - Corpus with 6 anagrams from 2 anagram families"""
        corpus = ["abed", "bead", "baled", "bade", "blade", "abled"]
        expected = {"abed", "abled", "bade", "baled", "bead", "blade"}

        student_explorer = AnagramLookup(corpus, self.letters1)
        actual = student_explorer.get_all_anagrams()

        self.assertEqual(
            actual, expected, f"Words that were in your set but not the expected set {actual.difference(expected)}\n Words that were in the expected set but not your set {expected.difference(actual)}")

    def test_4(self):
        """explorer.get_all_anagrams - Variety of word lengths, some anagrams not in letters"""
        corpus = ["bad", "abed", "mouse", "bead", "baled",
                  "abled", "rat", "art", "blade", "dab"]
        expected = {"abed",  "abled", "bad", "baled", "bead", "blade", "dab"}

        student_explorer = AnagramLookup(corpus, self.letters1)
        actual = student_explorer.get_all_anagrams()

        self.assertEqual(
            actual, expected, f"Words that were in your set but not the expected set {actual.difference(expected)}\n Words that were in the expected set but not your set {expected.difference(actual)}")

    def test_5(self):
        """explorer.get_all_anagrams - Actual wordlist from valid_word_list, letter combo #1"""
        expected = {'bead', 'dab', 'bade', 'lade', 'lead', 'bad', 'ale', 'dal', 'bed', 'bale',
                    'deal', 'lad', 'deb', 'abel', 'able', 'dale', 'abed', 'elba', 'lea'}
        student_explorer = AnagramLookup(get_valid_word_list(), self.letters1)
        actual = student_explorer.get_all_anagrams()

        self.assertEqual(
            actual, expected, f"Words that were in your set but not the expected set {actual.difference(expected)}\n Words that were in the expected set but not your set {expected.difference(actual)}")

    def test_6(self):
        """explorer.get_all_anagrams - Actual wordlist from valid_word_list, letter combo #2"""

        expected = {'part', 'pat', 'rats', 'riot', 'rapt', 'astir', 'pot', 'rasp', 'opts', 'tars', 'taro',
                    'sprat', 'patios', 'star', 'spot', 'rots', 'trio', 'opt', 'rota', 'trips', 'ports', 'tar',
                    'parts', 'ira', 'stop', 'pris', 'past', 'taos', 'pairs', 'riots', 'trios', 'stair', 'tip',
                    'rap', 'tips', 'apt', 'asp', 'pit', 'taps', 'strop', 'strap', 'pots', 'oars', 'traps',
                    'sari', 'pits', 'trap', 'strip', 'air', 'spat', 'spa', 'sort', 'prat', 'patois', 'raps',
                    'pats', 'sap', 'tap', 'rips', 'spit', 'soar', 'spar', 'its', 'rat', 'post', 'arts',
                    'paris', 'oats', 'art', 'sport', 'tops', 'top', 'airs', 'par', 'sit'}
        student_explorer = AnagramLookup(get_valid_word_list(), self.letters2)
        actual = student_explorer.get_all_anagrams()
        self.assertEqual(
            actual, expected, f"Words that were in your set but not the expected set {actual.difference(expected)}\n Words that were in the expected set but not your set {expected.difference(actual)}")

    def test_7(self):
        """explorer.get_all_anagrams - Actual wordlist from valid_word_list, letter combo #3 (double letter)"""

        expected = {'slip', 'spool', 'slop', 'sloop', 'lisp', 'ilo', 'lops', 'lips', 'oil', 'oslo', 'oils',
                    'pool', 'solo', 'pools', 'silo', 'loop', 'soil', 'pris', 'rips', 'polo', 'loops'}

        student_explorer = AnagramLookup(get_valid_word_list(), self.letters3)
        actual = student_explorer.get_all_anagrams()

        self.assertEqual(
            actual, expected, f"Words that were in your set but not the expected set {actual.difference(expected)}\n Words that were in the expected set but not your set {expected.difference(actual)}")

    def test_8(self):
        """Ensure that hash table is used for efficiency"""

        corpus = ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
        student_explorer = AnagramLookup(corpus, self.letters1)

        student_explorer.anagram_hash_table = {}

        actual = student_explorer.get_all_anagrams()  # should be empty set

        self.assertEqual(
            actual, set(), f"Expected empty set since hash table was removed, but got {actual}")

    def test_9(self):
        """explorer.get_all_anagrams - Long list of many anagram families"""
        corpus = [
            "abed",
            "abet",
            "abets",
            "abut",
            "acme",
            "acre",
            "acres",
            "actors",
            "actress",
            "airmen",
            "alert",
            "alerted",
            "ales",
            "aligned",
            "allergy",
            "alter",
            "altered",
            "amen",
            "anew",
            "angel",
            "angle",
            "antler",
            "apt",
            "bade",
            "baste",
            "bead",
            "beast",
            "beat",
            "beats",
            "beta",
            "betas",
            "came",
            "care",
            "cares",
            "casters",
            "castor",
            "costar",
            "dealing",
            "gallery",
            "glean",
            "largely",
            "later",
            "leading",
            "learnt",
            "leas",
            "mace",
            "mane",
            "marine",
            "mean",
            "name",
            "pat",
            "race",
            "races",
            "recasts",
            "regally",
            "related",
            "remain",
            "rental",
            "sale",
            "scare",
            "seal",
            "tabu",
            "tap",
            "treadle",
            "tuba",
            "wane",
            "wean",
        ]
        expected = {
            "abed", "bade", "bead", "abet", "beat", "beta",
            "abets", "baste", "beast", "beats", "betas",
            "abut", "tabu", "tuba",
            "acme", "came", "mace",
            "acre", "care", "race",
            "acres", "cares", "races", "scare",
            "actors", "castor", "costar",
            "actress", "casters", "recasts",
            "airmen", "marine", "remain",
            "alert", "alter", "later", "alerted", "altered", "related", "treadle", "ales", "leas", "sale", "seal", "aligned", "dealing", "leading", "allergy", "gallery", "largely", "regally", "amen", "mane", "mean", "name", "anew", "wane", "wean", "angel", "angle", "glean", "antler", "learnt", "rental", "apt", "pat", "tap",
        }
        student_explorer = AnagramLookup(corpus, self.entire_alphbet)
        actual = student_explorer.get_all_anagrams()
        self.assertEqual(
            actual, expected, f"Words that were in your set but not the expected set {actual.difference(expected)}\n Words that were in the expected set but not your set {expected.difference(actual)}")

    def test_10(self):
        """explorer.get_all_anagrams - Mixed corpus with many overlapping anagrams"""
        corpus = [
            "abc",
            "abcd",
            "abce",
            "abdc",
            "acb",
            "acbd",
            "acdb",
            "acc",
            "bac",
            "bacd",
            "badc",
            "bca",
            "bcad",
            "bcda",
            "cab",
            "cabd",
            "cadb",
            "cac",
            "cba",
            "cbad",
            "cbda",
            "cca",
        ]
        expected = {
            "abc", "acb", "bac", "bca", "cab", "cba",
            "abcd",
            "abdc",
            "acbd",
            "acdb",
            "bacd",
            "badc",
            "bcad",
            "bcda",
            "cabd",
            "cadb",
            "cbad",
            "cbda",
            "acc", "cac", "cca"
        }
        student_explorer = AnagramLookup(
            corpus, ["a", "b", "c", "d", "e", "c"])
        actual = student_explorer.get_all_anagrams()
        self.assertEqual(
            actual, expected, f"Words that were in your set but not the expected set {actual.difference(expected)}\n Words that were in the expected set but not your set {expected.difference(actual)}")

    def test_11(self):
        """explorer.get_all_anagrams - Corpus with single word should yield empty set"""
        corpus = ["rat"]
        expected = set()
        student_explorer = AnagramLookup(corpus, self.letters1)
        actual = student_explorer.get_all_anagrams()
        self.assertEqual(
            actual, expected, f"Expected empty set for single-word corpus, but got {actual}")


if __name__ == '__main__':
    unittest.main()
