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
program_on = True

while program_on:
    direction = input("Type 'encode' to Encrypt, 'decode' to Decrypt, 'exit' to Exit: \n").lower()

    if direction == 'encode':
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))
        encrypt(text, shift)
    elif direction == 'decode':
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))
        decrypt(text, shift)
    elif direction == 'exit':
        print("Thank you for using Caesar Cipher!")
        program_on = False
    else:
        print("Please type 'encode' or 'decode' or 'exit'")
