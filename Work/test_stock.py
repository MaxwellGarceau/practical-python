# test_stock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    # Make sure the s.cost property returns the correct value (49010.0)
    def test_cost(self):
        s = stock.Stock('GOOG', 100, 490.1)
        cost = s.cost
        self.assertEqual(cost, 49010.0)

    # Make sure the s.sell() method works correctly. It should decrement the value of s.shares accordingly.
    def test_sell(self):
        s = stock.Stock('GOOG', 100, 490.1)
        s.sell(1)
        self.assertEqual(s.shares, 99)

    # Make sure that the s.shares attribute can’t be set to a non-integer value.
    def test_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = 'non int value'

if __name__ == '__main__':
    unittest.main()
