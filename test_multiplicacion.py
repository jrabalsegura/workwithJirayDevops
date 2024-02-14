import unittest
from multiplicacion import multiplicar

class TestMultiplicacion(unittest.TestCase):
        
            def test_multiplicacion(self):
                self.assertEqual(multiplicar(3, 5), 15)
                self.assertEqual(multiplicar(-1, 1), -1)
                self.assertEqual(multiplicar(-2, -4), 8)
                self.assertEqual(multiplicar(2, -5), -10)
                
if __name__ == '__main__':
    unittest.main()