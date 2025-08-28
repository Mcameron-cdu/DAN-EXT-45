# HIT137 Assignment 2 - Q1
# Starter: reads raw_text.txt and writes it back out

with open("assignment_files/raw_text.txt", "r") as f:
    text = f.read()

print("Raw text from file:")
print(text)

with open("assignment_files/encrypted_text.txt", "w") as f:
    f.write(text)

print("Text copied to encrypted_text.txt")
