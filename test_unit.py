import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    
    def test_sub(self):
        result = rpn.calculate('1 1 -')
        self.assertEqual(0, result)
    
    def test_mul(self):
        result = rpn.calculate('2 2 *')
        self.assertEqual(4, result)

    def test_div(self):
        result = rpn.calculate('6 3 /')
        self.assertEqual(2, result)

    def test_chain(self):
        result = rpn.calculate('1 1 + 2 *')
        self.assertEqual(4, result)
