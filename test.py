import unittest
from utils.masking import mask_credit_card, mask_phone_number, mask_ip_address


class TestMaskingFunctions(unittest.TestCase):

	def test_mask_credit_card(self):
		self.assertEqual(mask_credit_card("My credit card number is 1234567891011120"), "My credit card number is ***")

	def test_mask_phone_number(self):
		self.assertEqual(mask_phone_number("Call me at 123456789"), "Call me at ***")

	def test_mask_email(self):
		self.assertEqual(mask_ip_address("My IP is 192.180.1.1"), "My IP is ***")


if __name__ == '__main__':
	unittest.main()
