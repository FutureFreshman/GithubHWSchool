import unittest

from valid_anagame_words import get_valid_word_list

from anagame import calc_stats
from AnagramLookup import AnagramLookup


class TestEx1(unittest.TestCase):
    def setUp(self):
        # Runs before every test
        self.letters = ["p", "o", "t", "s", "r", "i", "a"]
        self.explorer = AnagramLookup(get_valid_word_list(), self.letters)
        self.all_anagrams = {'spar', 'pat', 'sport', 'spa', 'air', 'its', 'tip', 'sari', 'pris', 'strip',
                             'airs', 'tar', 'paris', 'spot', 'trap', 'strop', 'part', 'pits', 'rots', 'arts',
                             'opt', 'rats', 'traps', 'ira', 'opts', 'astir', 'star', 'rat', 'sap', 'trio',
                             'pit', 'pots', 'tars', 'rap', 'oars', 'art', 'spit', 'tips', 'prat', 'sprat',
                             'spat', 'ports', 'post', 'apt', 'taos', 'tap', 'rips', 'rasp', 'soar', 'patois',
                             'top', 'strap', 'rapt', 'trips', 'taro', 'pairs', 'sit', 'sort', 'past', 'tops',
                             'taps', 'stop', 'riot', 'rota', 'asp', 'raps', 'par', 'riots', 'trios', 'oats',
                             'parts', 'pot', 'stair', 'patios', 'pats'}
        self.all_anagrams = {'spar', 'pat', 'sport', 'spa', 'air', 'its', 'tip', 'sari', 'pris', 'strip',
                             'airs', 'tar', 'paris', 'spot', 'trap', 'strop', 'part', 'pits', 'rots', 'arts',
                             'opt', 'rats', 'traps', 'ira', 'opts', 'astir', 'star', 'rat', 'sap', 'trio',
                             'pit', 'pots', 'tars', 'rap', 'oars', 'art', 'spit', 'tips', 'prat', 'sprat',
                             'spat', 'ports', 'post', 'apt', 'taos', 'tap', 'rips', 'rasp', 'soar', 'patois',
                             'top', 'strap', 'rapt', 'trips', 'taro', 'pairs', 'sit', 'sort', 'past', 'tops',
                             'taps', 'stop', 'riot', 'rota', 'asp', 'raps', 'par', 'riots', 'trios', 'oats',
                             'parts', 'pot', 'stair', 'patios', 'pats'}

    def test_0(self):
        """calc_stats - Data Types"""
        guesses = list()
        guesses.append(("star", "tarts"))
        guesses.append(("far", "rat"))
        guesses.append(("top", "tip"))
        print(f"Guesses: {guesses}")

        scoreDict = calc_stats(guesses, self.explorer)
        self.assertIn("score", scoreDict,
                      "The dictionary should have a 'score' key.")
        self.assertIsInstance(
            scoreDict["score"], int, "The score key should map to an integer value.")
        self.assertIn("accuracy", scoreDict,
                      "The dictionary should have an 'accuracy' key.")
        self.assertIsInstance(
            scoreDict["accuracy"], int, "The 'accuracy' key should map to an integer value.")
        self.assertIn("skill", scoreDict,
                      "The dictionary should have a 'skill' key.")
        self.assertIsInstance(
            scoreDict["skill"], int, "The 'skill' key should map to an integer value.")
        self.assertIn("valid", scoreDict,
                      "The dictionary should have a 'valid' key.")
        self.assertIsInstance(
            scoreDict["valid"], list, "The 'valid' key should map to a list value.")
        self.assertIn("invalid", scoreDict,
                      "The dictionary should have an 'invalid' key.")
        self.assertIsInstance(
            scoreDict["invalid"], list, "The 'invalid' key should map to a list value.")
        self.assertIn("guessed", scoreDict,
                      "The dictionary should have an 'guessed' key.")
        self.assertIsInstance(
            scoreDict["guessed"], set, "The 'guessed' key should map to a set value.")
        self.assertIn("not guessed", scoreDict,
                      "The dictionary should have a 'not guessed' key.")
        self.assertIsInstance(
            scoreDict["not guessed"], set, "The 'not guessed' key should map to a set value.")

    def test_1(self):
        """calc_stats - No valid guesses out of 3 guesses"""
        guesses = list()
        guesses.append(("star", "tarts"))
        guesses.append(("far", "rat"))
        guesses.append(("top", "tip"))
        print(f"Guesses: {guesses}")

        scoreDict = calc_stats(guesses, self.explorer)
        """- score should be 0"""
        self.assertEqual(scoreDict["score"], 0)
        self.assertEqual(len(scoreDict["valid"]), 0)
        self.assertEqual(len(scoreDict["invalid"]), 3)
        self.assertEqual(scoreDict["accuracy"], 0)

        guessed = sorted(["star", "tarts", "far", "rat", "top", "tip"])
        self.assertEqual(scoreDict["skill"], 0)
        self.assertEqual(len(scoreDict["guessed"]), 0)
        self.assertEqual(scoreDict["not guessed"], self.all_anagrams)

    def test_2(self):
        """calc_stats - All valid guesses with one duplicate anagram stem"""
        guesses = []
        guesses.append(("art", "rat"))
        guesses.append(("rats", "arts"))
        guesses.append(("spit", "pits"))
        guesses.append(("spit", "tips"))
        guesses.append(("stop", "pots"))
        guesses.append(("tip", "pit"))
        guesses.append(("top", "pot"))
        print(f"Guesses: {guesses}")

        # letters = ["p", "o", "t", "s", "r", "i", "a"]
        scoreDict = calc_stats(guesses, self.explorer)
        self.assertEqual(scoreDict["score"], 11)
        self.assertEqual(len(scoreDict["valid"]), 7)
        self.assertEqual(len(scoreDict["invalid"]), 0)
        self.assertEqual(scoreDict["accuracy"], 100)

        guessed = ["art", "rat", "rats", "arts", "spit", "pits",
                   "tips", "stop", "pots", "tip", "pit", "top", "pot"]
        expectedSkill = 17
        self.assertEqual(scoreDict["skill"], expectedSkill)
        self.assertEqual(len(scoreDict["guessed"]), len(guessed))
        self.assertEqual(len(scoreDict["not guessed"]), len(
            self.all_anagrams)-len(guessed))
        self.assertEqual(
            len(scoreDict["guessed"].union(guessed)), len(guessed))
        all_anagrams2 = self.all_anagrams.copy()
        for word in guessed:
            all_anagrams2.remove(word)
        self.assertEqual(scoreDict["not guessed"], all_anagrams2)

    def test_3(self):
        """calc_stats - Some valid and some invalid guesses"""
        guesses = []
        guesses.append(("star", "pair"))
        guesses.append(("fun", "rat"))
        guesses.append(("top", "tip"))
        guesses.append(("art", "rat"))  # 1
        guesses.append(("rats", "arts"))  # 2
        guesses.append(("spit", "pits"))  # 2
        guesses.append(("pits", "tips"))  # 2
        guesses.append(("stop", "pots"))  # 2
        guesses.append(("tip", "pit"))  # 1
        guesses.append(("top", "pot"))  # 1
        guesses.append(("ports", "sport"))  # 3
        guesses.append(("spot", "spit"))
        guesses.append(("sot", "spit"))
        guesses.append(("hiss", "cat"))
        guesses.append(("mouse", "rat"))
        guesses.append(("cat", "dog"))
        print(f"Guesses: {guesses}")
        scoreDict = calc_stats(guesses, self.explorer)
        print(f"Testing score... expecting 14..")
        self.assertEqual(scoreDict["score"], 14)
        print(f"Testing valid words... expecting 8 pairs of valid words")
        self.assertEqual(len(scoreDict["valid"]), 8)
        print(f"Testing invalid words... expecting 8 pairs of iinvalid words")
        self.assertEqual(len(scoreDict["invalid"]), 8)
        print(f"Testing accuracy... expecting an accuracy of 50")
        self.assertEqual(scoreDict["accuracy"], 50)

        guessed = {"art", "rat", "rats", "arts", "spit", "pits", "tips",
                   "stop", "pots", "tip", "pit", "top", "pot", "ports", "sport"}
        print(f"Testing unique words guessed... expecting {guessed}")
        self.assertEqual(scoreDict["guessed"], guessed)
        all_anagrams2 = self.all_anagrams.copy()
        for word in guessed:
            all_anagrams2.remove(word)
        print(f"Testing unique words not guessed... expecting {all_anagrams2}")
        self.assertEqual(scoreDict["not guessed"], all_anagrams2)
        expectedSkill = 20
        print(f"Testing skill... expecting a skill of 20")
        self.assertEqual(scoreDict["skill"], expectedSkill)

    def test_4(self):
        """calc_stats - No guesses"""
        guesses = []
        print(f"Guesses: {guesses}")

        scoreDict = calc_stats(guesses, self.explorer)
        self.assertEqual(scoreDict["score"], 0)
        self.assertEqual(len(scoreDict["valid"]), 0)
        self.assertEqual(len(scoreDict["invalid"]), 0)
        self.assertEqual(scoreDict["accuracy"], 0)
        self.assertEqual(scoreDict["skill"], 0)
        self.assertEqual(len(scoreDict["guessed"]), 0)
        self.assertEqual(len(scoreDict["not guessed"]), len(self.all_anagrams))

    def test_5(self):
        """calc_stats - Scoring with duplicate and invalid guesses"""
        guesses = []
        guesses.append(("star", "tarts"))  # INVALID
        guesses.append(("far", "rat"))  # INVALID
        guesses.append(("art", "rat"))
        # letters = ["p", "o", "t", "s", "r", "i", "a"]

        print(f"Guesses: {guesses}")

        scoreDict = calc_stats(guesses, self.explorer)
        print(f"Testing score... expecting 1")
        self.assertEqual(scoreDict["score"], 1, "Score is incorrect!")
        print(f"Testing valid words... expecting 1 pair of valid words")
        self.assertEqual(len(scoreDict["valid"]),
                         1, "Number of valid words is incorrect!")
        print(f"Testing invalid words... expecting 4 pairs of invalid words")
        self.assertEqual(len(scoreDict["invalid"]),
                         2, "Number of invalid words is incorrect!")
        print(f"Testing accuracy... expecting an accuracy of 20")
        self.assertEqual(scoreDict["accuracy"], 33, "Accuracy is incorrect")
        guessed = {"art", "rat"}
        print(f"Testing unique words guessed... expecting {guessed}")
        self.assertEqual(
            len(scoreDict["guessed"]), 2, "Number of unique words guessed is incorrect!")
        print(
            f"Testing unique words not guessed... expecting {len(self.all_anagrams)-2} words not guessed")
        self.assertEqual(len(scoreDict["not guessed"]), len(
            self.all_anagrams)-2, "Number of unique words not guessed is incorrect!")
        print(f"Testing skill... expecting a skill of 2")
        self.assertEqual(scoreDict["skill"], 2, "Skill is incorrect!")


if __name__ == '__main__':
    unittest.main()
