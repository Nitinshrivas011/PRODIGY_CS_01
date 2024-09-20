def encrypt(text, shift):
    result = ""
    
    # traverse through each character in the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Leave non-alphabet characters unchanged
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


if __name__ == "__main__":
    print("Caesar Cipher Program")
    
    # Get user input for the operation
    choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()

    # Get user input for the message and shift value
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
