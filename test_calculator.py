import unittest
from calculator import add
class CalculatorTests(unittest.TestCase):
    def test_add(self):self.assertEqual(add(2,3),5)
    def test_reject_string(self):
        with self.assertRaises(TypeError):add('2',3)
    def test_reject_bool(self):
        with self.assertRaises(TypeError):add(True,3)
if __name__=='__main__':unittest.main()
