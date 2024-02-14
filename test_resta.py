import unittest
from resta import restar

class TestResta(unittest.TestCase):
    
        def test_resta(self):
            self.assertEqual(restar(2, 2), 0)
            self.assertEqual(restar(-1, 1), -2)
            self.assertEqual(restar(-2, -4), 2)
            self.assertEqual(restar(2, -5), 7)
            
if __name__ == '__main__':
    unittest.main()