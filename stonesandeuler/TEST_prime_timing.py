import py_compile
import unittest

from prime_timing import is_prime_exhaustive
from prime_timing import is_prime_exhaustive_escape
from prime_timing import is_prime_skip_evens
from prime_timing import is_prime_factor_fold

class TestEx1(unittest.TestCase):
    def test_01(self):
        """is_prime_exhaustive: Data Type Checks"""
        actual = isinstance(is_prime_exhaustive(12), bool)
        expected = True
        self.assertEqual(actual, expected, "is_prime_exhaustive should return a bool value.")

    def test_02(self):
        """is_prime_exhaustive: Single Even Composite Number"""
        prime = is_prime_exhaustive(12)
        self.assertEqual(prime, False)

    def test_03(self):
        """is_prime_exhaustive: Single Odd Prime Number"""
        prime = is_prime_exhaustive(17)
        self.assertEqual(prime, True)

    def test_04(self):
        """is_prime_exhaustive: Single Even Prime Number"""
        prime = is_prime_exhaustive(2)
        self.assertEqual(prime, True)

    def test_05(self):
        """is_prime_exhaustive: Single Odd Composite Number"""
        prime = is_prime_exhaustive(35)
        self.assertEqual(prime, False)

    def test_06(self):
        """is_prime_exhaustive: 0"""
        prime = is_prime_exhaustive(0)
        self.assertEqual(prime, False)

    def test_07(self):
        """is_prime_exhaustive: 1"""
        prime = is_prime_exhaustive(1)
        self.assertEqual(prime, False)

    def test_08(self):
        """is_prime_exhaustive: All primes less than 100"""
        actualPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                        37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        testPrimes = []
        for n in range(1, 101):
            if is_prime_exhaustive(n):
                testPrimes.append(n)
        prime = is_prime_exhaustive(-17)
        self.assertEqual(testPrimes, actualPrimes)

    def test_09(self):
        """is_prime_exhaustive: Negative Number"""
        prime = is_prime_exhaustive(-35)
        self.assertEqual(prime, False)

    def test_10(self):
        """is_prime_exhaustive_escape: Data Type Checks"""
        actual = isinstance(is_prime_exhaustive_escape(12), bool)
        expected = True
        self.assertEqual(actual, expected, "is_prime_exhaustive_escape should return a bool value.")


    def test_11(self):
        """is_prime_exhaustive_escape: Single Even Composite Number"""
        prime = is_prime_exhaustive_escape(12)
        self.assertEqual(prime, False)

    def test_12(self):
        """is_prime_exhaustive_escape: Single Odd Prime Number"""
        prime = is_prime_exhaustive_escape(17)
        self.assertEqual(prime, True)

    def test_13(self):
        """is_prime_exhaustive_escape: Single Even Prime Number"""
        prime = is_prime_exhaustive_escape(2)
        self.assertEqual(prime, True)

    def test_14(self):
        """is_prime_exhaustive_escape: Single Odd Composite Number"""
        prime = is_prime_exhaustive_escape(35)
        self.assertEqual(prime, False)

    def test_15(self):
        """is_prime_exhaustive_escape: 0"""
        prime = is_prime_exhaustive_escape(0)
        self.assertEqual(prime, False)

    def test_16(self):
        """is_prime_exhaustive_escape: 1"""
        prime = is_prime_exhaustive_escape(1)
        self.assertEqual(prime, False)

    def test_17(self):
        """is_prime_exhaustive_escape: All primes less than 100"""
        actualPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        testPrimes = []
        for n in range(1, 101):
            if is_prime_exhaustive_escape(n):
                testPrimes.append(n)
        prime = is_prime_exhaustive_escape(-17)
        self.assertEqual(testPrimes, actualPrimes)

    def test_18(self):
        """is_prime_exhaustive_escape: Negative Number"""
        prime = is_prime_exhaustive_escape(-35)
        self.assertEqual(prime, False)

    def test_19(self):
        """is_prime_skip_evens: Data Type Checks"""
        actual = isinstance(is_prime_skip_evens(12), bool)
        expected = True
        self.assertEqual(actual, expected, "is_prime_skip_evens should return a bool value.")

    def test_20(self):
        """is_prime_skip_evens: Single Even Composite Number"""
        prime = is_prime_skip_evens(12)
        self.assertEqual(prime, False)

    def test_21(self):
        """is_prime_skip_evens: Single Odd Prime Number"""
        prime = is_prime_skip_evens(17)
        self.assertEqual(prime, True)

    def test_22(self):
        """is_prime_skip_evens: Single Even Prime Number"""
        prime = is_prime_skip_evens(2)
        self.assertEqual(prime, True)

    def test_23(self):
        """is_prime_skip_evens: Single Odd Composite Number"""
        prime = is_prime_skip_evens(35)
        self.assertEqual(prime, False)

    def test_24(self):
        """is_prime_skip_evens: 0"""
        prime = is_prime_skip_evens(0)
        self.assertEqual(prime, False)

    def test_25(self):
        """is_prime_skip_evens: 1"""
        prime = is_prime_skip_evens(1)
        self.assertEqual(prime, False)

    def test_26(self):
        """is_prime_skip_evens: All primes less than 100"""
        actualPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        testPrimes = []
        for n in range(1, 101):
            if is_prime_skip_evens(n):
                testPrimes.append(n)
        prime = is_prime_skip_evens(-17)
        self.assertEqual(testPrimes, actualPrimes)

    def test_27(self):
        """is_prime_skip_evens: Negative Number"""
        prime = is_prime_skip_evens(-35)
        self.assertEqual(prime, False)

    def test_28(self):
        """is_prime_factor_fold: Data Type Checks"""
        actual = isinstance(is_prime_factor_fold(12), bool)
        expected = True
        self.assertEqual(actual, expected, "is_prime_factor_fold should return a bool value.")

    def test_29(self):
        """is_prime_factor_fold: Single Even Composite Number"""
        prime = is_prime_factor_fold(12)
        self.assertEqual(prime, False)

    def test_30(self):
        """is_prime_factor_fold: Single Odd Prime Number"""
        prime = is_prime_factor_fold(17)
        self.assertEqual(prime, True)

    def test_31(self):
        """is_prime_factor_fold: Single Even Prime Number"""
        prime = is_prime_factor_fold(2)
        self.assertEqual(prime, True)

    def test_32(self):
        """is_prime_factor_fold: Single Odd Composite Number"""
        prime = is_prime_factor_fold(35)
        self.assertEqual(prime, False)

    def test_33(self):
        """is_prime_factor_fold: 0"""
        prime = is_prime_factor_fold(0)
        self.assertEqual(prime, False)

    def test_34(self):
        """is_prime_factor_fold: 1"""
        prime = is_prime_factor_fold(1)
        self.assertEqual(prime, False)

    def test_35(self):
        """is_prime_factor_fold: All primes less than 100"""
        actualPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        testPrimes = []
        for n in range(1, 101):
            if is_prime_factor_fold(n):
                testPrimes.append(n)
        self.assertEqual(testPrimes, actualPrimes)

    def test_36(self):
        """is_prime_factor_fold: Negative Number"""
        prime = is_prime_factor_fold(-35)
        self.assertEqual(prime, False)


if __name__ == '__main__':  
    print("TESTING NOW: 33 Tests")
    print("is_prime_exhaustive: 01 - 09")
    print("is_prime_exhaustive_escape: 10 - 18")
    print("is_prime_skip_evens: 19 - 27")
    print("is_prime_factor_fold: 28 - 36")
    unittest.main()
 