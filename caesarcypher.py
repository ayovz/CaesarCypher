alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, key):
    text = text.lower()
    encrypted_text = ""

    for letter in text:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            new_index = (current_index + key) % 26  # wrap around using modulo
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += letter  # keep punctuation, spaces, etc.

    print(f"Your encrypted message is '{encrypted_text}'\n<<<<<<<<<!!!!!!!!!!!!!!!!!>>>>>>>>>>>>>\n")


def decrypt(text, key):
    text = text.lower()
    decrypted_text = ""

    for letter in text:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            new_index = (current_index - key) % 26
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += letter

    print(f"Your decrypted message is '{decrypted_text}'\n<<<<<<<<<!!!!!!!!!!!!!!!!!>>>>>>>>>>>>>\n")


print('''
 ██████  █████  ███████ ███████  █████  ██████   
██      ██   ██ ██      ██      ██   ██ ██   ██  
██      ███████ █████   ███████ ███████ ██████   
██      ██   ██ ██           ██ ██   ██ ██   ██  
 ██████ ██   ██ ███████ ███████ ██   ██ ██   ██  
                                                 
                                                 
 ██████ ██    ██ ██████  ██   ██ ███████ ██████  
██       ██  ██  ██   ██ ██   ██ ██      ██   ██ 
██        ████   ██████  ███████ █████   ██████  
██         ██    ██      ██   ██ ██      ██   ██ 
 ██████    ██    ██      ██   ██ ███████ ██   ██ 
                                                 
''')
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            result += chr(shifted)
        else:
            result += char
    print(f"Encrypted message: {result}")

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - ord('a') - shift) % 26 + ord('a')
            result += chr(shifted)
        else:
            result += char
    print(f"Decrypted message: {result}")


program_on = True

while program_on:
    direction = input("Type 'encode' to Encrypt, 'decode' to Decrypt, 'exit' to Exit: \n").lower()

    if direction == 'encode' or direction == 'decode':
        text = input("Type your message: \n").lower()

        # Validate shift input
        while True:
            shift_input = input("Type the shift number: \n")
            if shift_input.isdigit():
                shift = int(shift_input)
                break
            else:
                print("Please enter a valid number for the shift.")

        if direction == 'encode':
            encrypt(text, shift)
        else:
            decrypt(text, shift)

    elif direction == 'exit':
        print("Thank you for using Caesar Cipher!")
        program_on = False
    else:
        print("Invalid command. Please type 'encode', 'decode', or 'exit'.")

