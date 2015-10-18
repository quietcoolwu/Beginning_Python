import unittest, my_math

class ProductTestCase(unittest.TestCase):

    def testIntegers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = my_math.product(x, y)
                self.assertTrue(p == x*y, 'Integer multiplication failed')

    def testFloats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x/10.0
                y = y/10.0
                p = my_math.product(x, y)
                self.assertTrue(p == x*y, 'Float multiplication failed')

if __name__ == '__main__': unittest.main()