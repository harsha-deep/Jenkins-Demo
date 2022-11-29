import unittest
from adder import add
from mult import multiply


class Test(unittest.TestCase):
    def test_addition(self):
        lst = [1, 2]
        result = 3
        self.assertEqual(add(lst[0], lst[1]), result)

    def test_multiplication(self):
        lst = [7, 7]
        result = 49
        self.assertEqual(multiply(lst[0], lst[1]), result)


if __name__ == '__main__':
    unittest.main()
