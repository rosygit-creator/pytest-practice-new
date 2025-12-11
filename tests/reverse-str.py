import unittest


def reverse_string(a):
    reversed_str=a[::-1]
    return reversed_str


class TestAddNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        result=reverse_string("rosy")
        self.assertEqual(result,"ysor")


    def test_negative_Numbers(self):
        self.assertEqual(reverse_string("1234"), "4321")

    def test_zero_with_positive(self):
        self.assertEqual(reverse_string(""), "")

    def test_zero_with_positive1(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_zero_with_positive2(self):
        self.assertEqual(reverse_string("a abc"), "cba a")

    def test_zero_with_positive1(self):
        self.assertEqual(reverse_string("a12$%"), "%$21a")
    #
    # def test_zero_with_negative(self):
    #     self.assertEqual(add(0, -2), -2)
    #
    # def test_zero_input(self):
    #     self.assertEqual(add(0, 0), 0)
    #
