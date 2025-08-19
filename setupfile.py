import os

folders = ["src", "tests"]
files = [
    "src/redactor.py",
    "tests/test_redactor.py",
    "README.md",
    "requirements.txt",
    ".gitignore"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, "w") as f:
        f.write("")  # creates empty files
