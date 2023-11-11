import unittest
from fizzbuzz import divisivel_por_3_ou_5

class TestFizzBuzz(unittest.TestCase):
    def test_divisivel_por_3(self):
        self.assertEqual(divisivel_por_3_ou_5(3), 1)
        self.assertEqual(divisivel_por_3_ou_5(9), 1)
        self.assertEqual(divisivel_por_3_ou_5(12), 1)
    
    def test_divisivel_por_5(self):
        self.assertEqual(divisivel_por_3_ou_5(5), 2)
        self.assertEqual(divisivel_por_3_ou_5(10), 2)
        self.assertEqual(divisivel_por_3_ou_5(20), 2)
    
    def test_divisivel_por_3_e_5(self):
        self.assertEqual(divisivel_por_3_ou_5(15), 3)
        self.assertEqual(divisivel_por_3_ou_5(30), 3)
        self.assertEqual(divisivel_por_3_ou_5(45), 3)
    
    def test_nao_divisivel_por_3_ou_5(self):
        self.assertEqual(divisivel_por_3_ou_5(1), 0)
        self.assertEqual(divisivel_por_3_ou_5(7), 0)
        self.assertEqual(divisivel_por_3_ou_5(11), 0)

if __name__ == '__main__':
    unittest.main()