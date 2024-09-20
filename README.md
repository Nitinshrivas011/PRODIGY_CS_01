# Caesar Cipher Encryption and Decryption

This Python program allows users to encrypt and decrypt text using the **Caesar Cipher** algorithm. Users can input a message and a shift value to perform the encryption and decryption.

## Features
- Encrypts plain text using the Caesar Cipher algorithm with a user-defined shift value.
- Decrypts encrypted text by reversing the shift.
- Handles both uppercase and lowercase characters.
- Retains spaces, punctuation, and other non-alphabetic characters without alteration.

## How the Caesar Cipher Works
The Caesar Cipher is a simple encryption technique where each letter in the text is replaced by another letter that is a fixed number of positions down (or up) the alphabet. For example, with a shift of 3, `A` would be replaced by `D`, `B` by `E`, and so on.

## Program Structure
- **`encrypt(text, shift)`**: This function takes the input message and shifts each letter by the specified amount, encrypting the message.
- **`decrypt(text, shift)`**: This function decrypts the message by shifting each letter back by the specified amount.
- **Main Program**: The program asks the user if they want to encrypt or decrypt, then takes the message and shift value as inputs and prints the result.

## Getting Started

### Prerequisites
To run this program, you'll need to have Python installed. You can download the latest version of Python from [python.org](https://www.python.org/downloads/).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/caesar-cipher.git
   cd caesar-cipher
