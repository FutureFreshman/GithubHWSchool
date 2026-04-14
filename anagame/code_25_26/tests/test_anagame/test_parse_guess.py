import unittest
from anagame import parse_guess


class TestEx1(unittest.TestCase):

    def test_1(self):
        """parse_guess -  Basic Correct"""
        guess = "eat,tea"
        val = parse_guess(guess)
        self.assertEqual(val, ("eat", "tea"))

    def test_2(self):
        """parse_guess - Correct, 1 space after comma"""
        guess = "eat, tea"
        val = parse_guess(guess)
        self.assertEqual(val, ("eat", "tea"))

    def test_3(self):
        """parse_guess - Correct, Many spaces"""
        guess = " eat , tea "
        val = parse_guess(guess)
        self.assertEqual(val, ("eat", "tea"))

    def test_4(self):
        """parse_guess - Incorrect, no comma"""
        guess = "eat tea"
        val = parse_guess(guess)
        self.assertEqual(val, ("", ""))

    def test_5(self):
        """parse_guess - Incorrect, multiple commas"""
        guess = "eat, tea,"
        val = parse_guess(guess)
        self.assertEqual(val, ("", ""))

    def test_6(self):
        """parse_guess - Incorrect, one word"""
        guess = "eattea"
        val = parse_guess(guess)
        self.assertEqual(val, ("", ""))

    def test_7(self):
        """parse_guess - Incorrect, three words"""
        guess = "eat, tea, ate"
        val = parse_guess(guess)
        self.assertEqual(val, ("", ""))

    def test_8(self):
        """parse_guess - Basic Correct 2"""
        guess = "stop, pots"
        val = parse_guess(guess)
        self.assertEqual(val, ("pots", "stop"))

    def test_9(self):
        """parse_guess - Mystery Correct 1"""
        guess = " st@op ,pots"
        val = parse_guess(guess)
        self.assertEqual(val, ("pots", "stop"))

    def test_10(self):
        """parse_guess - Mystery Correct 2"""
        guess = "stop    ,p ots   "
        val = parse_guess(guess)
        self.assertEqual(val, ("pots", "stop"))


if __name__ == '__main__':
    unittest.main()
