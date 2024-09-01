import unittest
from mock.generator import NumberListGenerator
from algorithms.quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):

    def test_ramdom(self):
        numbers = NumberListGenerator.generate_random_numbers(100, 1)[0]
        expected = sorted(numbers)
        quick_sort(numbers)
        self.assertEqual(numbers, expected)
    
    def test_sorted(self):
        numbers = NumberListGenerator.generate_sorted_numbers(100)
        expected = sorted(numbers)
        quick_sort(numbers)
        self.assertEqual(numbers, expected)
    
    def test_reversed(self):
        numbers = NumberListGenerator.generate_reversed_numbers(100)
        expected = sorted(numbers)
        quick_sort(numbers)
        self.assertEqual(numbers, expected)
    
    def test_almost_sorted(self):
        numbers = NumberListGenerator.generate_almost_sorted_numbers(100)
        expected = sorted(numbers)
        quick_sort(numbers)
        self.assertEqual(numbers, expected)
