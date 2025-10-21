Caesar Cipher Encryption/Decryption Tool

🛡️ Project Overview

This project is a beginner-level Python command-line utility designed to perform encryption and decryption using the Caesar Cipher. It serves as a practical demonstration of fundamental cryptographic concepts and core Python programming skills.

Skills Demonstrated

Cryptography Fundamentals: Practical understanding of a basic substitution cipher and the role of a secret key (shift value).

Python Programming: Application of functions, conditional logic (if/else), loop control, and user input validation.

Modular Arithmetic: Effective use of the modulo operator (%) to handle alphabet wrap-around (e.g., shifting 'Z' forward).

ASCII Manipulation: Conversion between characters and their ASCII values (ord() and chr()) to perform numerical shifts.

🚀 Getting Started

Prerequisites

You need to have Python installed on your system.

Python 3.x

How to Run

Clone or download this repository to your local machine:

git clone [Your GitHub URL Here]
cd Caesar_Cipher_Tool


Run the script from your terminal:

python caesar_cipher.py


The program will then prompt you to choose between (E)ncrypt or (D)ecrypt and to enter the message and the shift key.

⚙️ How the Cipher Works

The Caesar Cipher is one of the simplest and most well-known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

Concept

Implementation

Key

The fixed shift value (1-25) provided by the user.

Encryption

new_position = (original_position + shift) % 26

Decryption

new_position = (original_position + (26 - shift)) % 26

Non-Alphabetic

Spaces, numbers, and punctuation are preserved without shifting.

💡 Example Usage

Input:

Do you want to (E)ncrypt or (D)ecrypt? E
Enter your message: HELLO WORLD
Enter the shift key (1-25): 3


Output:

Original Message: HELLO WORLD
Shift Key: 3
Encrypted Message: KHOOR ZRUOG


🛠️ Future Enhancements

Potential future improvements for this project include:

Brute-Force Decryption: Add a function to automatically test all 25 possible shift keys when decrypting text without a known key.

Vigenere Cipher: Upgrade the cipher implementation from a monoalphabetic (Caesar) to a polyalphabetic substitution cipher (Vigenere) for increased complexity.

GUI: Implement a simple graphical user interface (GUI) using Tkinter or another library instead of relying solely on the command line.
