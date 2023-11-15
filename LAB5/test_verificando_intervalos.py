import unittest
from verificando_intervalos import in_range

class TestInRange(unittest.TestCase):
    def test_in_range(self):
        self.assertTrue(in_range(1, 2, 3))
        self.assertTrue(in_range(1, 1, 1))
        self.assertFalse(in_range(-1, -2, 0))
        self.assertFalse(in_range(1, 3, 2))
        self.assertFalse(in_range(1, 1, 0))
        self.assertFalse(in_range(-1, 0, -2))
        self.assertFalse(in_range(0, 1, -1))
        self.assertFalse(in_range(3, 1, 2))
        self.assertTrue(in_range(1, 1, 1))

if __name__ == '__main__':
    unittest.main()