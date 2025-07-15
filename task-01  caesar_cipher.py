def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift  # Reverse shift for decryption
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    message = input("Enter the message: ")
    while True:
        try:
            shift = int(input("Enter shift value (e.g. 3): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
        if choice in ['E', 'D']:
            break
        else:
            print("Invalid choice. Please enter E or D.")

    if choice == 'E':
        result = caesar_cipher(message, shift, mode='encrypt')
        print("Encrypted message:", result)
    else:
        result = caesar_cipher(message, shift, mode='decrypt')
        print("Decrypted message:", result)

if __name__== "__main__":
    main()