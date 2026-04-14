import py_compile
import unittest

from stones import format_pile
from stones import is_valid_move
from stones import get_ai_guess

class TestEx1(unittest.TestCase):
    def test_01(self):
        """format_pile- 1 stone in the pile"""
        val = format_pile(1)
        self.assertEqual(val, "\n*\nThere is 1 stone in the pile.")

    def test_02(self):
        """format_pile- 2 stones in the pile"""
        val = format_pile(2)
        self.assertEqual(val, "\n**\nThere are 2 stones in the pile.")

    def test_03(self):
        """format_pile- 3 stones in the pile"""
        val = format_pile(3)
        self.assertEqual(val, "\n**\n*\nThere are 3 stones in the pile.")

    def test_04(self):
        """format_pile- 6 stones in the pile"""
        val = format_pile(6)
        self.assertEqual(val, "\n***\n***\nThere are 6 stones in the pile.")

    def test_05(self):
        """format_pile- 7 stones in the pile"""
        val = format_pile(7)
        self.assertEqual(val, "\n***\n***\n*\nThere are 7 stones in the pile.")

    def test_06(self):
        """format_pile- 9 stones in the pile"""
        val = format_pile(9)
        self.assertEqual(val, "\n***\n***\n***\nThere are 9 stones in the pile.")

    def test_07(self):
        """format_pile- 10 stones in the pile"""
        val = format_pile(10)
        self.assertEqual(val, "\n****\n****\n**\nThere are 10 stones in the pile.")

    def test_08(self):
        """format_pile- 11 stones in the pile"""
        val = format_pile(11)
        self.assertEqual(val, "\n****\n****\n***\nThere are 11 stones in the pile.")

    def test_09(self):
        """format_pile- 15 stones in the pile"""
        val = format_pile(15)
        self.assertEqual(val, "\n****\n****\n****\n***\nThere are 15 stones in the pile.")

    def test_10(self):
        """format_pile- 16 stones in the pile"""
        val = format_pile(16)
        self.assertEqual(val, "\n****\n****\n****\n****\nThere are 16 stones in the pile.")

    def test_11(self):
        """is_valid_move- 16 Stones, Guess in valid_guesses"""
        self.assertEqual(is_valid_move(1, 16, [1,2,3,4]), True)

    def test_12(self):
        """is_valid_move- 16 Stones, Guess not in valid_guesses"""
        self.assertEqual(is_valid_move(5, 16, [1,2,3,4]), False)

    def test_13(self):
        """is_valid_move- 3 Stones, Guess in valid_guesses That Takes Last Stone"""
        self.assertEqual(is_valid_move(3, 3, [1,2,3,4]), False)

    def test_14(self):
        """is_valid_move- 3 Stones, Guess not in valid_guesses"""
        self.assertEqual(is_valid_move(0, 3, [1,2,3,4]), False)

    def test_15(self):
            """is_valid_move- 3 Stones, Guess in valid_guesses, but Takes Too Many Stones"""
            self.assertEqual(is_valid_move(4, 3, [1,2,3,4]), False)

    def test_16(self):
        """is_valid_move- 11 Stones, Guess in non-standard valid_guesses"""
        self.assertEqual(is_valid_move(1, 11, [1,2]), True)

    def test_17(self):
        """is_valid_move- 11 Stones, Guess in non-standard valid_guesses"""
        self.assertEqual(is_valid_move(2, 11, [1,2]), True)

    def test_18(self):
        """is_valid_move- 11 Stones, Guess not in non-standard valid_guesses"""
        self.assertEqual(is_valid_move(3, 11, [1,2]), False)

    def test_19(self):
        """get_ai_guess- 2 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(2, [1,2,3,4])
        self.assertEqual(val, 1)

    def test_20(self):
        """get_ai_guess- 3 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(3, [1,2,3,4])
        self.assertEqual(val, 2)

    def test_21(self):
        """get_ai_guess- 4 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(4, [1,2,3,4])
        self.assertEqual(val, 3)

    def test_22(self):
        """get_ai_guess- 5 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(5, [1,2,3,4])
        self.assertEqual(val, 4)

    def test_23(self):
        """get_ai_guess- 6 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(6, [1,2,3,4])
        self.assertEqual(val, 1)

    def test_24(self):
        """get_ai_guess- 7 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(7, [1,2,3,4])
        self.assertEqual(val, 1)

    def test_25(self):
        """get_ai_guess- 8 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(8, [1,2,3,4])
        self.assertEqual(val, 2)

    def test_26(self):
        """get_ai_guess- 9 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(9, [1,2,3,4])
        self.assertEqual(val, 3)

    def test_27(self):
        """get_ai_guess- 10 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(10, [1,2,3,4])
        self.assertEqual(val, 4)

    def test_28(self):
        """get_ai_guess- 11 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(11, [1,2,3,4])
        self.assertEqual(val, 1)

    def test_29(self):
        """get_ai_guess- 12 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(12, [1,2,3,4])
        self.assertEqual(val, 1)

    def test_30(self):
        """get_ai_guess- 13 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(13, [1,2,3,4])
        self.assertEqual(val, 2)

    def test_31(self):
        """get_ai_guess- 14 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(14, [1,2,3,4])
        self.assertEqual(val, 3)

    def test_32(self):
        """get_ai_guess- 15 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(15, [1,2,3,4])
        self.assertEqual(val, 4)

    def test_33(self):
        """get_ai_guess- 16 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(16, [1,2,3,4])
        self.assertEqual(val, 1)

if __name__ == '__main__':
    print("TESTING NOW: 33 Tests")
    print("format_pile: 01 - 10")
    print("is_valid_move: 11 - 18")
    print("get_ai_guess: 19 - 33")
    unittest.main()
