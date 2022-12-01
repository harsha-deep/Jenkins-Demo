import unittest
from adder import add
from mult import multiply


class Test(unittest.TestCase):
    def test_addition_1(self):
        lst = [1, 2]
        result = 3
        self.assertEqual(add(lst[0], lst[1]), result)
    
    def test_addition_2(self):
        lst = [2, 3]
        result = 5
        self.assertEqual(add(lst[0], lst[1]), result)

    def test_multiplication_1(self):
        lst = [7, 7]
        result = 49
        self.assertEqual(multiply(lst[0], lst[1]), result)
    
    def test_multiplication_2(self):
        lst = [8, 8]
        result = 72
        self.assertEqual(multiply(lst[0], lst[1]), result)
        
    def test_multiplication_2(self):
        lst = [10, 9]
        result = 100
        self.assertEqual(multiply(lst[0], lst[1]), result)


if __name__ == '__main__':
    unittest.main()
