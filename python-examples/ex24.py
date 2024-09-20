import unittest
from my_utils import sum_of_nums


class TestSumOfNums(unittest.TestCase):

    def test_for_valid_input(self):
        want = 100
        got = sum_of_nums('10, 50, vinod, kumar, 20, 15, 5')
        self.assertEqual(want, got)

    def test_for_number(self):
        want = 1234
        got = sum_of_nums(1234)
        self.assertEqual(want, got)

    def test_for_empty_str(self):
        want = 0
        got = sum_of_nums('')
        self.assertEqual(want, got)

    def test_for_invalid_types(self):
        def fn():
            sum_of_nums(True)

        self.assertRaises(ValueError, fn)


if __name__ == '__main__':
    unittest.main()
