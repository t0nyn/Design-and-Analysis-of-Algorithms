import unittest
from mock.generator import NumberListGenerator
from algorithms.counting_sort import counting_sort

class TestCountingSort(unittest.TestCase):

    def test_ramdom(self):
        numbers = NumberListGenerator.generate_random_numbers(100, 1)[0]
        expected = sorted(numbers)
        output = counting_sort(numbers)
        self.assertEqual(output, expected)
    
    def test_sorted(self):
        numbers = NumberListGenerator.generate_sorted_numbers(100)
        expected = sorted(numbers)
        output = counting_sort(numbers)
        self.assertEqual(output, expected)
    
    def test_reversed(self):
        numbers = NumberListGenerator.generate_reversed_numbers(100)
        expected = sorted(numbers)
        output = counting_sort(numbers)
        self.assertEqual(output, expected)
    
    def test_nearly_sorted(self):
        numbers = NumberListGenerator.generate_nearly_sorted_numbers(100)
        expected = sorted(numbers)
        output = counting_sort(numbers)
        self.assertEqual(output, expected)
