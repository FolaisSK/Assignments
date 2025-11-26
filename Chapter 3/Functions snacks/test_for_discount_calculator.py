import unittest
import discount_calculator

class TestForPromoCodeDiscount(unittest.TestCase):
	def test_that_discount_calculator_exists(self):
		discount_calculator.price_discount('pen', 100, 'BUGG')


	def test_that_discount_calculator_returns_half_off(self):
		actual = discount_calculator.price_discount('cup', 500, 'HALFOFF')
		expected = 250
		self.assertEqual(actual, expected)