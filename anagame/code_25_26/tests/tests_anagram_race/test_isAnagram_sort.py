import py_compile
import unittest
from anagram_race import is_anagram_sort_hash

class TestEx1(unittest.TestCase):

  def test_1(self):
      """is_anagram_sort_hash -  Basic True"""
      val = is_anagram_sort_hash("baste", "beast")
      self.assertEqual(val, True)


  def test_2(self):
      """is_anagram_sort_hash -  Basic True with mixed Capitalization"""
      val = is_anagram_sort_hash("Allergy", "reGaLLy")
      self.assertEqual(val, True)


  def test_3(self):
      """is_anagram_sort_hash -  Basic False"""
      val = is_anagram_sort_hash("baste", "beaft")
      self.assertEqual(val, False)


  def test_4(self):
      """is_anagram_sort_hash -  Identical Words"""
      val = is_anagram_sort_hash("road", "road")
      self.assertEqual(val, False)


  def test_5(self):
     """is_anagram_sort_hash -  Identical Words with Mixed Capitalization"""
     val = is_anagram_sort_hash("road", "Road")
     self.assertEqual(val, False)


  def test_6(self):
        """is_anagram_sort_hash -  Nearly Identical Words"""
        val = is_anagram_sort_hash("abed", "abet")
        self.assertEqual(val, False)


  def test_7(self):
        """is_anagram_sort_hash -  Nearly Anagrams: repeated letter"""
        val = is_anagram_sort_hash("odd", "do")
        self.assertEqual(val, False)


  def test_8(self):
        """is_anagram_sort_hash -  1 letter words"""
        val = is_anagram_sort_hash("a", "a")
        self.assertEqual(val, False)


  def test_9(self):
        """is_anagram_sort_hash -  Almost Anagrams: Plural"""
        val = is_anagram_sort_hash("castor", "costars")
        self.assertEqual(val, False)


  def test_10(self):
        """is_anagram_sort_hash -  Two Empty Strings"""
        val = is_anagram_sort_hash("", "")
        self.assertEqual(val, False)


  def test_11(self):
        """is_anagram_sort_hash -  Almost Anagrams: Plural, swapped order"""
        val = is_anagram_sort_hash("costars", "castor")
        self.assertEqual(val, False)

 
  def test_12(self):
      """is_anagram_sort_hash -  Characters other than A-Z, a-z"""
      val = is_anagram_sort_hash("ra3t", "tar4")
      self.assertEqual(val, True)


  def test_13(self):
      """is_anagram_sort_hash - 2 near-anagrams"""
      val = is_anagram_sort_hash("rattles", "realist")
      self.assertEqual(val, False)

 
  def test_14(self):
      """is_anagram_sort_hash -  Characters other than A-Z, a-z"""
      val = is_anagram_sort_hash("s!tar", "start")
      self.assertEqual(val, False)

if __name__ == '__main__':
    unittest.main() 