from unittest import TestCase

from temperature_converter import *


class TestTemperatureConverter(TestCase):

    def test_clecius_to_farenheit(self):
        self.assertEqual(converter(32, "C", 10), "cold advisory")

#from unittest import TestCase
#from temperature_converter import *
#
#class TestTemperatureConverter(TestCase):
#
#    def test_fahrenheit_to_celcius(self):
#        self.assertEqual(converter(32, "F", 10), "Cold advisory")
#    
#    
#    def test_celcius_to_fahrenheit(self):
#        self.assertEqual(converter(30, "C", 80), "Heat alert")
#        
#        
#    def test_that_its_celcius_when_no_unit(self):
#        self.assertEqual(converter(32, "", 10), "Heat alert")
