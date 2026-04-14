import py_compile
import unittest
from tests_anagram_race.anagram_race import is_anagram_lettercount

class TestEx1(unittest.TestCase):

  def test_1(self):
      """is_anagram_lettercount -  Basic True"""
      val = is_anagram_lettercount("baste", "beast")
      self.assertEqual(val, True)


  def test_2(self):
      """is_anagram_lettercount -  Basic True with mixed Capitalization"""
      val = is_anagram_lettercount("Allergy", "reGaLLy")
      self.assertEqual(val, True)


  def test_3(self):
      """is_anagram_lettercount -  Basic False"""
      val = is_anagram_lettercount("baste", "beaft")
      self.assertEqual(val, False)


  def test_4(self):
      """is_anagram_lettercount -  Identical Words"""
      val = is_anagram_lettercount("road", "road")
      self.assertEqual(val, False)


  def test_5(self):
     """is_anagram_lettercount -  Identical Words with Mixed Capitalization"""
     val = is_anagram_lettercount("road", "Road")
     self.assertEqual(val, False)


  def test_6(self):
        """is_anagram_lettercount -  Nearly Identical Words"""
        val = is_anagram_lettercount("abed", "abet")
        self.assertEqual(val, False)


  def test_7(self):
        """is_anagram_lettercount -  Nearly Anagrams: repeated letter"""
        val = is_anagram_lettercount("odd", "do")
        self.assertEqual(val, False)


  def test_8(self):
        """is_anagram_lettercount -  1 letter words"""
        val = is_anagram_lettercount("a", "a")
        self.assertEqual(val, False)


  def test_9(self):
        """is_anagram_lettercount -  Almost Anagrams: Plural"""
        val = is_anagram_lettercount("castor", "costars")
        self.assertEqual(val, False)


  def test_10(self):
        """is_anagram_lettercount -  Two Empty Strings"""
        val = is_anagram_lettercount("", "")
        self.assertEqual(val, False)


  def test_11(self):
        """is_anagram_lettercount -  Almost Anagrams: Plural, swapped order"""
        val = is_anagram_lettercount("costars", "castor")
        self.assertEqual(val, False)


  def test_12(self):
      """is_anagram_lettercount -  Characters other than A-Z, a-z"""
      val = is_anagram_lettercount("ra3t", "tar4")
      self.assertEqual(val, True)


  def test_13(self):
      """is_anagram_lettercount - 2 near-anagrams"""
      val = is_anagram_lettercount("rattles", "realist")
      self.assertEqual(val, False)


  def test_14(self):
      """is_anagram_lettercount -  Characters other than A-Z, a-z"""
      val = is_anagram_lettercount("s!tar", "start")
      self.assertEqual(val, False)

if __name__ == '__main__':
    unittest.main() 