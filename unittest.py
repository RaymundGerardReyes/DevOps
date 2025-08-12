import unittest

from suminit import add

class unittest(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -5), -6)

    def test_add_zero(self):
        self.assertEqual(add(0, 7), 7)

if __name__ == '__main__':
    unittest.main()