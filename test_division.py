import unittest
from division import dividir

class TestDivision(unittest.TestCase):
        
    def test_division(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(-4, -2), 2)
        self.assertEqual(dividir(20, -5), -4)
    
    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)
                
if __name__ == '__main__':
    unittest.main()
