import unittest
from mock.generator import NumberListGenerator
from heap_sort import heap_sort

class TestHeapSort(unittest.TestCase):

    def test_ramdom(self):
        numbers = NumberListGenerator.generate_random_numbers(100, 1)[0]
        expected = sorted(numbers)
        heap_sort(numbers)
        self.assertEqual(numbers, expected)
    
    def test_sorted(self):
        numbers = NumberListGenerator.generate_sorted_numbers(100)
        expected = sorted(numbers)
        heap_sort(numbers)
        self.assertEqual(numbers, expected)
    
    def test_reversed(self):
        numbers = NumberListGenerator.generate_reversed_numbers(100)
        expected = sorted(numbers)
        heap_sort(numbers)
        self.assertEqual(numbers, expected)
    
    def test_almost_sorted(self):
        numbers = NumberListGenerator.generate_almost_sorted_numbers(100)
        expected = sorted(numbers)
        heap_sort(numbers)
        self.assertEqual(numbers, expected)
