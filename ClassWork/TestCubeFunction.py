import unittest
import test_cube_functio

class TestCubeFunction(unittest.TestCase):

    def test_that_cube_function_exist(self):
        test_cube_functio.cube(10)

    def test_that_cube_function_return_correct_result(self):
        actual = test_cube_functio.cube(10)
        expected = 1000
        self.assertEqual(actual, expected)

    def test_that_cube_function_return_invalid_data_with_wrong_input(self):
        actual = test_cube_functio.cube("musa")
        expected = "invalid input"
        self.assertEqual(actual, expected)
