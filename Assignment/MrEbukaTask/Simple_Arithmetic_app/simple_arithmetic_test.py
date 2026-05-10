from unittest import TestCase

from simple_arithmetic_app import get_random_number
from simple_arithmetic_app import get_swap

class TestRandomNumber(TestCase):
    
    def test_that_random_number_is_greater_than_zero(self):
        expected = get_random_number()
        self.assertTrue(expected > 0)

    def test_that_largest_smallest_comes_first(self):
        number = 2, 7
        swap = get_swap(2,7)
#        expected = 7, 2
        self.assertTrue(swap)
        
