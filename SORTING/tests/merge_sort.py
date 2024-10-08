import unittest
from mock.generator import NumberListGenerator
from algorithms.merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_ramdom(self):
        numbers = NumberListGenerator.generate_random_numbers(100, 1)[0]
        expected = sorted(numbers)
        merge_sort(numbers)
        self.assertEqual(numbers, expected)
    
    def test_sorted(self):
        numbers = NumberListGenerator.generate_sorted_numbers(100)
        expected = sorted(numbers)
        merge_sort(numbers)
        self.assertEqual(numbers, expected)
    
    def test_reversed(self):
        numbers = NumberListGenerator.generate_reversed_numbers(100)
        expected = sorted(numbers)
        merge_sort(numbers)
        self.assertEqual(numbers, expected)
    
    def test_nearly_sorted(self):
        numbers = NumberListGenerator.generate_nearly_sorted_numbers(100)
        expected = sorted(numbers)
        merge_sort(numbers)
        self.assertEqual(numbers, expected)
