# HIT137 Assignment 2 - Q1
# Caesar Cipher (shift by 3)

# open the input file
with open("assignment_files/raw_text.txt", "r") as f:
    text = f.read()

# encryption function
def encrypt(message, shift):
    result = ""
    for ch in message:
        if ch.isalpha():  # only shift letters
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

# decryption function
def decrypt(message, shift):
    return encrypt(message, -shift)

# run the cipher
encrypted = encrypt(text, 3)
decrypted = decrypt(encrypted, 3)

# save results
with open("assignment_files/encrypted_text.txt", "w") as f:
    f.write(encrypted)

with open("assignment_files/decrypted_text.txt", "w") as f:
    f.write(decrypted)

print("Encryption and decryption done.")
