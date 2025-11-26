import unittest
import temperature_convert

class TestForTemperatureConversion(unittest.TestCase):
	def test_that_temperature_convert_exists(self):
		temperature_convert.temperature_converter(28, 'C', 150)


	def test_that_temperature_convert_return_celsius(self):
		actual = temperature_convert.temperature_converter(28, 'F', 15)
		expected = "Heat alert"
		self.assertEqual(actual, expected)