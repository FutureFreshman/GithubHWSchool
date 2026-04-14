import py_compile
import unittest
from tests_anagram_race.anagram_race import is_anagram_exhaustive

class TestEx1(unittest.TestCase):

  def test_1(self):
      """is_anagram_exhaustive -  Basic True"""
      val = is_anagram_exhaustive("baste", "beast")
      self.assertEqual(val, True)


  def test_2(self):
      """is_anagram_exhaustive -  Basic True with mixed Capitalization"""
      val = is_anagram_exhaustive("Allergy", "reGaLLy")
      self.assertEqual(val, True)


  def test_3(self):
      """is_anagram_exhaustive -  Basic False"""
      val = is_anagram_exhaustive("baste", "beaft")
      self.assertEqual(val, False)


  def test_4(self):
      """is_anagram_exhaustive -  Identical Words"""
      val = is_anagram_exhaustive("road", "road")
      self.assertEqual(val, False)

  def test_5(self):
     """is_anagram_exhaustive -  Identical Words with Mixed Capitalization"""
     val = is_anagram_exhaustive("road", "Road")
     self.assertEqual(val, False)


  def test_6(self):
        """is_anagram_exhaustive -  Nearly Identical Words"""
        val = is_anagram_exhaustive("abed", "abet")
        self.assertEqual(val, False)


  def test_7(self):
        """is_anagram_exhaustive -  Nearly Anagrams: repeated letter"""
        val = is_anagram_exhaustive("odd", "do")
        self.assertEqual(val, False)


  def test_8(self):
        """is_anagram_exhaustive -  1 letter words"""
        val = is_anagram_exhaustive("a", "a")
        self.assertEqual(val, False)


  def test_9(self):
        """is_anagram_exhaustive -  Almost Anagrams: Plural"""
        val = is_anagram_exhaustive("castor", "costars")
        self.assertEqual(val, False)

  def test_10(self):
        """is_anagram_exhaustive -  Two Empty Strings"""
        val = is_anagram_exhaustive("", "")
        self.assertEqual(val, False)


  def test_11(self):
        """is_anagram_exhaustive -  Almost Anagrams: Plural, swapped order"""
        val = is_anagram_exhaustive("costars", "castor")
        self.assertEqual(val, False)


  def test_12(self):
      """is_anagram_exhaustive -  Characters other than A-Z, a-z"""
      val = is_anagram_exhaustive("ra3t", "tar4")
      self.assertEqual(val, True)


  def test_13(self):
      """is_anagram_exhaustive - 2 near-anagrams"""
      val = is_anagram_exhaustive("rattles", "realist")
      self.assertEqual(val, False)


  def test_14(self):
      """is_anagram_exhaustive -  Characters other than A-Z, a-z"""
      val = is_anagram_exhaustive("s!tar", "start")
      self.assertEqual(val, False)

if __name__ == '__main__':
    unittest.main() 