# Password Cracker GUI

A password strength testing tool built with Python that simulates brute-force and dictionary attacks in real time. The application features an intuitive GUI built with CustomTkinter, showcasing how passwords can be guessed using common attack methods. Designed for **educational** and **security-awareness** purposes.

---

## Features

- Brute-Force Attack Simulation – Tries all possible character combinations to guess the password.
- Dictionary Attack – Attempts guesses using a wordlist with added leetspeak substitutions (e.g., `@` for `a`, `0` for `o`).
- Adaptive Character Set – Automatically detects if the password includes uppercase, digits, or symbols and adjusts the guessing set accordingly.
- Real-Time Guess Display – Watch guesses live as they happen.
- Stop Button – Immediately stops the cracking process.
- Show/Hide Password Toggle – Easily view or mask your input.
- Case Sensitive Handling – Fully respects upper/lowercase characters in passwords.

---

## How It Works

The tool uses two core attack methods:

- **Brute-Force Attack:** Tries every possible character combination based on the password's character set.
- **Dictionary Attack:** Uses a wordlist of common passwords and applies leetspeak variations like `p@ssw0rd`, `admin123!`, etc.

These methods help demonstrate why complex, uncommon passwords are more secure.

---

## Technologies Used

- Python 3.x
- CustomTkinter
- `time`, `random` – For performance tracking and guessing logic
- `string` – To manage character sets

---

## GUI Preview

![Password Cracker GUI Screenshot](screenshot.png)  
*Add a screenshot of the GUI interface above.*

---

## Installation

```bash
git clone https://github.com/m0-3n/Password-Cracker-GUI.git
cd Password-Cracker-GUI
pip install customtkinter
python main_gui.py
