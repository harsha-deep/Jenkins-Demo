import unittest
from main import add, subtract, multiply, divide, average


class Test(unittest.TestCase):
    def test_addition(self):
        lst = [1, 2]
        result = 3
        self.assertEqual(add(lst[0], lst[1]), result)

    def test_subtraction(self):
        lst = [5, 4]
        result = 1
        self.assertEqual(subtract(lst[0], lst[1]), result)

    def test_multiplication(self):
        lst = [7, 7]
        result = 49
        self.assertEqual(multiply(lst[0], lst[1]), result)

    def test_divide(self):
        lst = [4, 2]
        result = 1
        self.assertEqual(divide(lst[0], lst[1]), result)

    def test_average(self):
        lst = [1, 2, 3, 4, 5]
        result = 4
        self.assertEqual(average(lst), result)


if __name__ == '__main__':
    unittest.main()
