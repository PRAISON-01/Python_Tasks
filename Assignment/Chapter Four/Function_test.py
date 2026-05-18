from unittest import TestCase

from Functions import cube

class TestCubeFunction(TestCase):
    
    def test_that_cube_function_is_correct(self):

        number = 3
        actual = Functions.cube(x)
        expected = 27
        self.assertEquals(actual ,expected)
