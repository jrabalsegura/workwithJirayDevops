import unittest
from suma import sumar

class TestSuma(unittest.TestCase):
    
        def test_suma(self):
            self.assertEqual(sumar(2, 2), 4)
            self.assertEqual(sumar(-1, 1), 0)
            self.assertEqual(sumar(-2, -4), -6)
            self.assertEqual(sumar(2, -5), -3)
            
if __name__ == '__main__':
    unittest.main()