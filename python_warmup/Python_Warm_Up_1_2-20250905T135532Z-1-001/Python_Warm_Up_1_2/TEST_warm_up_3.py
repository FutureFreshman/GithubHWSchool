import py_compile
import unittest

from warm_up_3 import classify_triangle


class TestEx1(unittest.TestCase):

    def test_0(self):
        """Right - Increasing Order"""
        actual = classify_triangle(3, 4, 5)
        expected = "right"
        self.assertEqual(actual, expected)

    def test_1(self):
        """Right- Mixed Order 1"""
        actual =  classify_triangle(3, 5, 4)
        expected = "right"
        self.assertEqual(actual, expected)

    def test_2(self):
        """Right- Mixed Order 2"""
        actual =  classify_triangle(4, 3, 5)
        expected = "right"
        self.assertEqual(actual, expected)

    def test_3(self):
        """Right- Mixed Order 3"""
        actual =  classify_triangle(4, 5, 3)
        expected = "right"
        self.assertEqual(actual, expected)

    def test_4(self):
        """Right- Mixed Order 4"""
        actual =  classify_triangle(5, 3, 4)
        expected = "right"
        self.assertEqual(actual, expected)

    def test_5(self):
        """Right- Mixed Order 5"""
        actual =  classify_triangle(5, 4, 3)
        expected = "right"
        self.assertEqual(actual, expected)

    def test_6(self):
        """Right- General"""
        actual =  classify_triangle(5, 12, 13)
        expected = "right"
        self.assertEqual(actual, expected)

    def test_7(self):
        """Obtuse- Isosceles 1"""
        actual = classify_triangle(7,4,4)
        expected = "obtuse"
        self.assertEqual(actual, expected)

    def test_8(self):
        """Obtuse- Isosceles 2"""
        actual = classify_triangle(4,7,4)
        expected = "obtuse"
        self.assertEqual(actual, expected)

    def test_9(self):
        """Obtuse- Isosceles 3"""
        actual = classify_triangle(4,4,7)
        expected = "obtuse"
        self.assertEqual(actual, expected)

    def test_10(self):
        """Obtuse- General"""
        actual = classify_triangle(3, 4, 6)
        expected = "obtuse"
        self.assertEqual(actual, expected)

    def test_11(self):
        """Acute- Equilateral"""
        actual = classify_triangle(3,3,3)
        expected = "acute"
        self.assertEqual(actual, expected)

    def test_12(self):
        """Acute- Isosceles"""
        actual = classify_triangle(3,3,4)
        expected = "acute"
        self.assertEqual(actual, expected)

    def test_13(self):
        """Acute- Decimal Side Lengths"""
        actual = classify_triangle(.5,.5,.5)
        expected = "acute"
        self.assertEqual(actual, expected)

    def test_14(self):
        """Acute- General"""
        actual = classify_triangle(4, 5, 6)
        expected = "acute"
        self.assertEqual(actual, expected)

    def test_15(self):
        """Does Not Exist- Negative Side Length 1"""
        actual = classify_triangle(5, -4, 3)
        expected = "does not exist"
        self.assertEqual(actual, expected, "Did you check for negative side lengths?")

    def test_16(self):
        """Does Not Exist- Negative Side Length 2"""
        actual = classify_triangle(-3, -8, -4)
        expected = "does not exist"
        self.assertEqual(actual, expected, "Did you check for multiple negative side lengths?")

    def test_17(self):
        """Does Not Exist- Sides Too Small 1"""
        actual = classify_triangle(1, 2, 3)
        expected = "does not exist"
        self.assertEqual(actual, expected, "Did you check for the sum of two side lengths that aren't > the third side?")

    def test_18(self):
        """Does Not Exist- Sides Too Small 2"""
        actual = classify_triangle(1, 1, 4)
        expected = "does not exist"
        self.assertEqual(actual, expected, "Did you assume all iscoceles triangles are valid?")

    def test_19(self):
        """Does Not Exist- Sides Too Small 3"""
        actual = classify_triangle(3, 3, 6)
        expected = "does not exist"
        self.assertEqual(actual, expected, "Did you assume all iscoceles triangles are valid?")

    def test_20(self):
        """Does Not Exist- Side length 0"""
        actual = classify_triangle(0, 0, 0)
        expected = "does not exist"
        self.assertEqual(actual,expected, "Did you assume that 'not positive' and 'negative' are synonyms?")

if __name__ == '__main__':
    unittest.main()