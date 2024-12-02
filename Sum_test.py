import unittest
from Sum import sum

class TestArithmeticProgression(unittest.TestCase):
    def test_sum_of_first_5_terms(self):
        self.assertEqual(sum(5), 75)
    
    def test_sum_of_first_10_terms(self):
        self.assertEqual(sum(10), 275)

    def test_sum_of_first_0_terms(self):
        self.assertEqual(sum(0), 0)

if __name__ == '__main__':
    unittest.main()
