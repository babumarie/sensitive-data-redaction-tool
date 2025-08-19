import unittest
from src.redactor import Redactor

class TestRedactor(unittest.TestCase):
    def setUp(self):
        self.redactor = Redactor()

    def test_email_redaction(self):
        text = "Contact: alice@example.com"
        result = self.redactor.redact(text)
        self.assertIn("[REDACTED_EMAIL]", result)

    def test_ip_redaction(self):
        text = "Server IP: 192.168.1.1"
        result = self.redactor.redact(text)
        self.assertIn("[REDACTED_IP]", result)

    def test_token_redaction(self):
        text = "Token: abcdef1234567890abcdef1234567890"
        result = self.redactor.redact(text)
        self.assertIn("[REDACTED_TOKEN]", result)

    def test_username_redaction(self):
        text = "Logged in as user_admin123"
        result = self.redactor.redact(text)
        self.assertIn("[REDACTED_USERNAME]", result)

if __name__ == "__main__":
    unittest.main()
