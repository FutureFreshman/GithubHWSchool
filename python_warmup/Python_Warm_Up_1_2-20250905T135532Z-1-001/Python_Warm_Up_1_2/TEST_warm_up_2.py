import py_compile
import unittest
from warm_up_2 import calculate_circumference
from warm_up_2 import calculate_area
from warm_up_2 import calculate_distance

class TestEx1(unittest.TestCase):

  def test_0(self):
      """calculate_area -  Radius = 1"""
      actual = calculate_area(1)
      expected = 3.14159
      self.assertLess(abs(expected - actual), 0.001)
      
  def test_1(self):
      
      """calculate_area -  Radius = 4"""
      actual = calculate_area(4)
      expected = 50.26548
      self.assertLess(abs(expected - actual), 0.001)

  def test_2(self):
      """calculate_area -  Radius = 2.5"""
      actual = calculate_area(2.5)
      expected = 19.63495
      self.assertLess(abs(expected - actual), 0.001)

  def test_3(self):
      """calculate_area -  Radius = 10"""
      actual = calculate_area(10)
      expected = 314.15927
      self.assertLess(abs(expected - actual), 0.001)

  def test_4(self):
      """calculate_circumference -  Radius = 1"""
      actual = calculate_circumference(1)
      expected = 6.28318
      self.assertLess(abs(expected - actual), 0.001)
      
  def test_5(self):
      """calculate_circumference -  Radius = 4"""
      actual = calculate_circumference(4)
      expected = 25.13274
      self.assertLess(abs(expected - actual), 0.001)

  def test_6(self):
      """calculate_circumference -  Radius = 1.5"""
      actual = calculate_circumference(1.5)
      expected = 9.42478
      self.assertLess(abs(expected - actual), 0.001)

  def test_7(self):
      """calculate_circumference -  Radius = 10"""
      actual = calculate_circumference(10)
      expected = 62.83185
      self.assertLess(abs(expected - actual), 0.001)

  def test_8(self):
      """calculate_distance -  (0, 0) --> (3, 4)"""
      actual = calculate_distance(0, 0, 3, 4)
      expected = 5
      self.assertLess(abs(expected - actual), 0.001)

  def test_9(self):
      """calculate_distance -  (0, 0) --> (-3, 4)"""
      actual = calculate_distance(0, 0, -3, 4)
      expected = 5
      self.assertLess(abs(expected - actual), 0.001)

  def test_10(self):
      """calculate_distance -  (-4, 3) --> (0, 0)"""
      actual = calculate_distance(-4, 3, 0, 0)
      expected = 5
      self.assertLess(abs(expected - actual), 0.001)

  def test_11(self):
      """calculate_distance -  (1, 2) --> (1, 2)"""
      actual = calculate_distance(1, 2, 1, 2)
      expected = 0
      self.assertLess(abs(expected - actual), 0.001)

  def test_12(self):
      """calculate_distance -  (1, 1) --> (2, 2)"""
      actual = calculate_distance(1, 1, 2, 2)
      expected = 1.41421356
      self.assertLess(abs(expected - actual), 0.001)

if __name__ == '__main__':
    unittest.main() 