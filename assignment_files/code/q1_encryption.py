# HIT137 Assignment 2 - Q1 (starter)
# Just reads raw_text.txt and prints it out

# open the input file
with open("assignment_files/raw_text.txt", "r") as f:
    text = f.read()

print("Raw text from file:")
print(text)
