import unittest
from data_protector import mask_data

class TestDataProtector(unittest.TestCase):
    def test_email_masking(self):
        masked = mask_data({"email": "test@example.com"})
        self.assertIn("***", masked["email"])

    def test_phone_masking(self):
        masked = mask_data({"phone": "+33612345678"})
        self.assertTrue(masked["phone"].startswith("+33"))

    def test_card_masking(self):
        masked = mask_data({"card": "1234567812345678"})
        self.assertIn("****", masked["card"])

if __name__ == "__main__":
    unittest.main()
