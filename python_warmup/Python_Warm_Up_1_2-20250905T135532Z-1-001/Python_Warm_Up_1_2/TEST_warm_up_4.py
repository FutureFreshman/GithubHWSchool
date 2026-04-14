import py_compile
import unittest

from warm_up_4 import positive_odds
from warm_up_4 import positive_multiples
from warm_up_4 import square_numbers
from warm_up_4 import triangle_numbers
from warm_up_4 import arithmetic_sequence
from warm_up_4 import fibonacci_sequence

class TestEx1(unittest.TestCase):

    def test_01(self):
        """Positive Odds- Negative Terms"""
        actual = positive_odds(-2)
        expected = []
        self.assertEqual(actual, expected, "non-positive n should return an empty list: []")

    def test_02(self):
        """Positive Odds- 0 Terms"""
        actual = positive_odds(0)
        expected = []
        self.assertEqual(actual, expected, "non-positive n should return an empty list: []")

    def test_03(self):
        """Positive Odds- 1 Term"""
        actual = positive_odds(1)
        expected = [1]
        self.assertEqual(actual, expected)

    def test_04(self):
        """Positive Odds- 2 Terms"""
        actual = positive_odds(2)
        expected = [1, 3]
        self.assertEqual(actual, expected)

    def test_05(self):
        """Positive Odds- Many Terms"""
        actual = positive_odds(5)
        expected = [1, 3, 5, 7, 9]
        self.assertEqual(actual, expected)

    def test_06(self):
        """Positive Multiples- Negative Terms"""
        actual = positive_multiples(-2, 3)
        self.assertEqual(actual, [], "non-positive n should return an empty list: []")

    def test_07(self):
        """Positive Multiples- 0 Terms"""
        actual = positive_multiples(0, 2)
        self.assertEqual(actual, [], "non-positive n should return an empty list: []")

    def test_08(self):
        """Positive Multiples- Negative Multiple"""
        actual = positive_multiples(3, -2)
        self.assertEqual(actual, [], "non-positive m should return an empty list: []")

    def test_09(self):
        """Positive Multiples- 0 Multiple"""
        actual = positive_multiples(2, 0)
        self.assertEqual(actual, [], "non-positive m should return an empty list: []")

    def test_10(self):
        """Positive Multiples- 1 Term"""
        actual = positive_multiples(1, 2)
        self.assertEqual(actual, [2])

    def test_11(self):
        """Positive Multiples- Many Terms"""
        actual = positive_multiples(4, 1)
        self.assertEqual(actual, [1, 2, 3, 4])

    def test_12(self):
        """Positive Multiples- Many Terms"""
        actual = positive_multiples(5, 3)
        self.assertEqual(actual, [3, 6, 9, 12, 15])

    def test_13(self):
        """Square Numbers- Negative Terms"""
        actual = square_numbers(-2)
        expected = []
        self.assertEqual(actual, expected, "non-positive n should return an empty list: []")

    def test_14(self):
        """Square Numbers- 0 Terms"""
        actual = square_numbers(0)
        expected = []
        self.assertEqual(actual, expected, "non-positive n should return an empty list: []")

    def test_15(self):
        """Square Numbers- 1 Term"""
        actual = square_numbers(1)
        expected = [0]
        self.assertEqual(actual, expected)

    def test_16(self):
        """Square Numbers- 4 Terms"""
        actual = square_numbers(4)
        expected = [0, 1, 4, 9]
        self.assertEqual(actual, expected)

    def test_17(self):
        """Square Numbers- 10 Terms"""
        actual = square_numbers(10)
        expected = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        self.assertEqual(actual, expected)

    def test_18(self):
        """Triangle Numbers- Negative Terms"""
        actual = triangle_numbers(-2)
        expected = []
        self.assertEqual(actual, expected, "non-positive n should return an empty list: []")

    def test_19(self):
        """Triangle Numbers- 0 Terms"""
        actual = triangle_numbers(0)
        expected = []
        self.assertEqual(actual, expected, "non-positive n should return an empty list: []")

    def test_20(self):
        """Triangle Numbers- 1 Term"""
        actual = triangle_numbers(1)
        expected = [1]
        self.assertEqual(actual, expected)
    
    def test_21(self):
        """Triangle Numbers- 4 Terms"""
        actual = triangle_numbers(4)
        expected = [1, 3, 6, 10]
        self.assertEqual(actual, expected)

    def test_22(self):
        """Triangle Numbers- 10 Terms"""
        actual = triangle_numbers(10)
        expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        self.assertEqual(actual, expected)

    def test_23(self):
        """Arithmetic Sequences- Negative Number of Terms"""
        actual = arithmetic_sequence(-1, 1, 2)
        expected = []
        self.assertEqual(actual, expected, "non-posiitve n should return an empty list: []")

    def test_24(self):
        """Arithmetic Sequences- Zero Number of Terms"""
        actual = arithmetic_sequence(0, 1, 2)
        expected = []
        self.assertEqual(actual, expected, "non-posiitve n should return an empty list: []")

    def test_25(self):
        """Arithmetic Sequences- One Term"""
        actual = arithmetic_sequence(1, 1, 2)
        expected = [1]
        self.assertEqual(actual, expected, "n=1 should return a list w/ 1 element: [t1]")

    def test_26(self):
        """Arithmetic Sequences- General"""
        actual = arithmetic_sequence(3, 1, 2)
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_27(self):
        """Arithmetic Sequences- General"""
        actual = arithmetic_sequence(5, 0, 2)
        expected = [0, 2, 4, 6, 8]
        self.assertEqual(actual, expected)

    def test_28(self):
        """Arithmetic Sequences- Two Negative Terms"""
        actual = arithmetic_sequence(5, -1, -3)
        expected = [-1, -3, -5, -7, -9]
        self.assertEqual(actual, expected)

    def test_29(self):
        """Arithmetic Sequences- One Negative Term"""
        actual = arithmetic_sequence(7, 1, -2)
        expected = [1, -2, -5, -8, -11, -14, -17]
        self.assertEqual(actual, expected)

    def test_30(self):
        """Arithmetic Sequences- Two Terms, Decreasing"""
        actual = arithmetic_sequence(2, 5, 0)
        expected = [5, 0]
        self.assertEqual(actual, expected, "n=2 should return a list w/ 2 elements: [t1, t2]")

    def test_31(self):
        """Fibonacci Sequences- Negative Terms"""
        actual = fibonacci_sequence(-2)
        expected = []
        self.assertEqual(actual, expected, "non-positive n should return an empty list: []")

    def test_32(self):
        """Fibonacci Sequences- Zero Terms"""
        actual = fibonacci_sequence(0)
        expected = []
        self.assertEqual(actual, expected, "non-positive n should return an empty list: []")

    def test_33(self):
        """Fibonacci Sequences- One Term"""
        actual = fibonacci_sequence(1)
        expected = [1]
        self.assertEqual(actual, expected)

    def test_34(self):
        """Fibonacci Sequences- Two Terms"""
        actual = fibonacci_sequence(2)
        expected = [1, 1]
        self.assertEqual(actual, expected)

    def test_35(self):
        """Fibonacci Sequences- Three Terms"""
        actual = fibonacci_sequence(3)
        expected = [1, 1, 2]
        self.assertEqual(actual, expected)

    def test_36(self):
        """Fibonacci Sequences- Many Terms"""
        actual = fibonacci_sequence(19)
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    print("TESTING NOW: 36 Tests")
    print("positive_odds: 01 - 05")
    print("positive_multiples: 06 - 12")
    print("square_numbers: 13 - 17")
    print("triangle_numbers: 18 - 22")
    print("arithmetic_sequence: 23 - 30")
    print("fibonacci_sequence: 31 - 36")
    unittest.main()