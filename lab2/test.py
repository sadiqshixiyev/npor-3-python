import unittest
from lab2 import two_sum  # Импортируем функцию из соседнего файла

class TestTwoSum(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_example_3(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
        
    def test_no_solution(self):
        self.assertEqual(two_sum([1, 2, 3], 10), [])

if __name__ == '__main__':
    unittest.main()