import unittest


def add(a,b):
    return a+b


class TestAddNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        result=add(2,3)
        self.assertEqual(result,5)

    def test_negative_Numbers(self):
        self.assertEqual(add(1,2), 3)

    def test_zero_with_positive(self):
        self.assertEqual(add(0, 2), 2)

    def test_zero_with_negative(self):
        self.assertEqual(add(0, -2), -2)

    def test_zero_input(self):
        self.assertEqual(add(0, 0), 0)

