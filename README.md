# 🔒 Sensitive Data Redaction Tool

This tool automatically detects and redacts sensitive information from text, such as:

- Email addresses
- IP addresses
- Access tokens
- Usernames

It’s designed for use in cybersecurity workflows, log sanitization, and multi-agent communication systems where privacy and data protection are critical.

---

## Features

- Regex-based detection of common sensitive patterns
- Modular design for easy extension
- Unit-tested for reliability
- Colab-compatible for lightweight experimentation

---

## Installation

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
