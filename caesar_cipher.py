# --- CAESAR CIPHER TOOL ---

def caesar_encrypt(text, shift):
    """Encrypts text using a Caesar Cipher with the given shift."""
    result = ""
    for char in text:
        if char.isalpha():
            # Set the starting point for ASCII conversion
            start = ord('A') if char.isupper() else ord('a')
            
            # 1. Convert char to a 0-25 index
            original_pos = ord(char) - start
            
            # 2. Apply the shift and wrap using modulo 26
            new_pos = (original_pos + shift) % 26
            
            # 3. Convert the new index back to a character
            new_char = chr(new_pos + start)
            
            result += new_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

def caesar_decrypt(text, shift):
    """Decrypts text by applying the reverse shift (26 - shift)."""
    # A shift of N is the same as encrypting with a shift of 26 - N
    # The modulo 26 ensures proper positive wrapping for decryption
    return caesar_encrypt(text, (26 - shift) % 26)


if __name__ == "__main__":
    print("--- Caesar Cipher Tool ---")
    
    # Get user input for action
    mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    
    if mode not in ['E', 'D']:
        print("Invalid mode selected. Exiting.")
    else:
        # Get the message
        message = input("Enter your message: ")
        
        # Get the shift key
        while True:
            try:
                # Ensure the shift is an integer between 1 and 25
                key = int(input("Enter the shift key (1-25): "))
                if 1 <= key <= 25:
                    break
                else:
                    print("Key must be between 1 and 25.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Perform the action
        if mode == 'E':
            encrypted_msg = caesar_encrypt(message, key)
            print(f"\nOriginal Message: {message}")
            print(f"Shift Key: {key}")
            print(f"Encrypted Message: {encrypted_msg}")
            
        elif mode == 'D':
            decrypted_msg = caesar_decrypt(message, key)
            print(f"\nCiphertext: {message}")
            print(f"Shift Key: {key}")
            print(f"Decrypted Message: {decrypted_msg}")