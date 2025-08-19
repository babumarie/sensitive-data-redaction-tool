import re

class Redactor:
    def __init__(self):
        self.patterns = {
            "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "ip": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            "token": r"\b[A-Za-z0-9]{32,}\b",
            "username": r"\buser_[a-zA-Z0-9]+\b"
        }

    def redact(self, text):
        redacted_text = text
        for label, pattern in self.patterns.items():
            redacted_text = re.sub(pattern, f"[REDACTED_{label.upper()}]", redacted_text)
        return redacted_text
