import py_compile
import unittest
from tests_anagram_race.anagram_race import is_anagram_checkoff

class TestEx1(unittest.TestCase):

  def test_1(self):
      """is_anagram_checkoff -  Basic True"""
      val = is_anagram_checkoff("baste", "beast")
      self.assertEqual(val, True)


  def test_2(self):
      """is_anagram_checkoff -  Basic True with mixed Capitalization"""
      val = is_anagram_checkoff("Allergy", "reGaLLy")
      self.assertEqual(val, True)


  def test_3(self):
      """is_anagram_checkoff -  Basic False"""
      val = is_anagram_checkoff("baste", "beaft")
      self.assertEqual(val, False)


  def test_4(self):
      """is_anagram_checkoff -  Identical Words"""
      val = is_anagram_checkoff("road", "road")
      self.assertEqual(val, False)


  def test_5(self):
     """is_anagram_checkoff -  Identical Words with Mixed Capitalization"""
     val = is_anagram_checkoff("road", "Road")
     self.assertEqual(val, False)


  def test_6(self):
        """is_anagram_checkoff -  Nearly Identical Words"""
        val = is_anagram_checkoff("abed", "abet")
        self.assertEqual(val, False)


  def test_7(self):
        """is_anagram_checkoff -  Nearly Anagrams: repeated letter"""
        val = is_anagram_checkoff("odd", "do")
        self.assertEqual(val, False)


  def test_8(self):
        """is_anagram_checkoff -  1 letter words"""
        val = is_anagram_checkoff("a", "a")
        self.assertEqual(val, False)


  def test_9(self):
        """is_anagram_checkoff -  Almost Anagrams: Plural"""
        val = is_anagram_checkoff("castor", "costars")
        self.assertEqual(val, False)


  def test_10(self):
        """is_anagram_checkoff -  Two Empty Strings"""
        val = is_anagram_checkoff("", "")
        self.assertEqual(val, False)


  def test_11(self):
        """is_anagram_checkoff -  Almost Anagrams: Plural, swapped order"""
        val = is_anagram_checkoff("costars", "castor")
        self.assertEqual(val, False)


  def test_12(self):
      """is_anagram_checkoff -  Characters other than A-Z, a-z"""
      val = is_anagram_checkoff("ra3t", "tar4")
      self.assertEqual(val, True)


  def test_13(self):
      """is_anagram_checkoff - 2 near-anagrams"""
      val = is_anagram_checkoff("rattles", "realist")
      self.assertEqual(val, False)

  def test_14(self):
      """is_anagram_checkoff -  Characters other than A-Z, a-z"""
      val = is_anagram_checkoff("s!tar", "start")
      self.assertEqual(val, False)

if __name__ == '__main__':
    unittest.main() 