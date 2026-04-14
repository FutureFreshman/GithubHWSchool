import py_compile
import unittest
from anagram_race import basic_checks

class TestEx1(unittest.TestCase):

  def test_0(self):
      """basic_checks -  Data Types"""
      val, w1, w2 = basic_checks("baste", "beast")
      self.assertEqual(isinstance(val, bool), True, "The first value returned be a bool")
      self.assertEqual(isinstance(w1,str), True, "The second value returned should be a string")
      self.assertEqual(isinstance(w2,str), True, "The third value returned should be a string")


  def test_1(self):
      """basic_checks -  Basic True"""
      val, w1, w2 = basic_checks("baste", "beast")
      self.assertEqual(val, True)
      self.assertEqual(w1, "baste")
      self.assertEqual(w2, "beast")


  def test_2(self):
      """basic_checks -  Basic True with mixed Capitalization"""
      val, w1, w2 = basic_checks("Allergy", "reGaLLy")
      self.assertEqual(val, True)
      self.assertEqual(w1, "allergy")
      self.assertEqual(w2, "regally")


  def test_3(self):
      """basic_checks -  Basic False"""
      val, w1, w2 = basic_checks("baste", "beaft")
      self.assertEqual(val, True)
      self.assertEqual(w1, "baste")
      self.assertEqual(w2, "beaft")


  def test_4(self):
      """basic_checks -  Identical Words"""
      val, w1, w2 = basic_checks("road", "road")
      self.assertEqual(val, False)
      self.assertEqual(w1, "road")
      self.assertEqual(w2, "road")


  def test_5(self):
     """basic_checks -  Identical Words with Mixed Capitalization"""
     val, w1, w2 = basic_checks("road", "Road")
     self.assertEqual(val, False, "Identical words can't be anagrams.")
     self.assertEqual(w1, "road")
     self.assertEqual(w2, "road")


  def test_6(self):
        """basic_checks -  Nearly Identical Words"""
        val, w1, w2 = basic_checks("abed", "abet")
        self.assertEqual(val, True)
        self.assertEqual(w1, "abed")
        self.assertEqual(w2, "abet")


  def test_7(self):
        """basic_checks -  Nearly Anagrams: repeated letter"""
        val, w1, w2 = basic_checks("odd", "do")
        self.assertEqual(val, False)
        self.assertEqual(w1, "odd")
        self.assertEqual(w2, "do")


  def test_8(self):
        """basic_checks -  1 letter words"""
        val, w1, w2 = basic_checks("a", "a")
        self.assertEqual(val, False)
        self.assertEqual(w1, "a")
        self.assertEqual(w2, "a")


  def test_9(self):
        """basic_checks -  Almost Anagrams: Plural"""
        val, w1, w2 = basic_checks("castor", "costars")
        self.assertEqual(val, False)
        self.assertEqual(w1, "castor")
        self.assertEqual(w2, "costars")


  def test_10(self):
        """basic_checks -  Two Empty Strings"""
        val, w1, w2 = basic_checks("", "")
        self.assertEqual(val, False)
        self.assertEqual(w1, "")
        self.assertEqual(w2, "")


  def test_11(self):
        """basic_checks -  Almost Anagrams: Plural, swapped order"""
        val, w1, w2 = basic_checks("costars", "castor")
        self.assertEqual(val, False)
        self.assertEqual(w1, "costars")
        self.assertEqual(w2, "castor")


  def test_12(self):
      """basic_checks -  Characters other than A-Z, a-z"""
      val, w1, w2 = basic_checks("ra3t", "tar4")
      self.assertEqual(val, True)
      self.assertEqual(w1, "rat")
      self.assertEqual(w2, "tar")

  def test_13(self):
      """basic_checks - 2 near-anagrams"""
      val, w1, w2 = basic_checks("rattles", "realist")
      self.assertEqual(val, True)
      self.assertEqual(w1, "rattles")
      self.assertEqual(w2, "realist")

  def test_14(self):
      """basic_checks -  Characters other than A-Z, a-z"""
      val, w1, w2 = basic_checks("s!tar", "start")
      self.assertEqual(val, False, "words should have the same length only considering A-Z, a-z characters")
      self.assertEqual(w1, "star")
      self.assertEqual(w2, "start")

if __name__ == '__main__':
    unittest.main() 