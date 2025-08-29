# Program: Two-shift Caesar cipher (encrypts and decrypts alternating characters)
# Author: Michael Cameron
# Date: YYYY-MM-DD

# Function to shift a single character by 'shift' positions
# If character is a letter, it rotates within A-Z or a-z
# Non-letters (spaces, punctuation, numbers) are returned unchanged
def shift_char(ch, shift):
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch

# Encrypt text by alternating between two shifts (s1 and s2)
# Even indices use shift1, odd indices use shift2
def encrypt_two_shifts(text, s1, s2):
    out = []
    for i, ch in enumerate(text):
        use = s1 if (i % 2 == 0) else s2  # decide which shift to apply
        out.append(shift_char(ch, use))
    return "".join(out)

# Decrypt text by reversing the shifts
# Same alternating pattern is used, but shift values are negated
def decrypt_two_shifts(text, s1, s2):
    out = []
    for i, ch in enumerate(text):
        use = s1 if (i % 2 == 0) else s2
        out.append(shift_char(ch, -use))   # negative shift = reverse
    return "".join(out)

# --- Input section ---
# Ask user for shift values (1–25).
# Defaults to 1 if invalid input is given.
try:
    shift1 = int(input("Enter shift1 (1..25): ").strip())
except:
    shift1 = 1
try:
    shift2 = int(input("Enter shift2 (1..25): ").strip())
except:
    shift2 = 1

# --- File I/O section ---
# Read the raw input text from a file
with open("assignment_files/raw_text.txt", "r") as f:
    original = f.read()

# Encrypt the original text and save to a new file
encrypted = encrypt_two_shifts(original, shift1, shift2)
with open("assignment_files/encrypted_text.txt", "w") as f:
    f.write(encrypted)

# Decrypt the encrypted text and save to a file
decrypted = decrypt_two_shifts(encrypted, shift1, shift2)
with open("assignment_files/decrypted_text.txt", "w") as f:
    f.write(decrypted)

# --- Verification step ---
# Check if decrypted text matches the original
ok = (decrypted == original)
print("Verification:", "MATCH" if ok else "DOES NOT MATCH")