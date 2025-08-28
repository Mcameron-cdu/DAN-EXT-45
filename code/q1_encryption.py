# HIT137 Assignment 2 - Q1
# Two-shift Caesar cipher

def shift_char(ch, shift):
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch

def encrypt_two_shifts(text, s1, s2):
    out = []
    for i, ch in enumerate(text):
        use = s1 if (i % 2 == 0) else s2  # even index -> shift1, odd -> shift2
        out.append(shift_char(ch, use))
    return "".join(out)

def decrypt_two_shifts(text, s1, s2):
    out = []
    for i, ch in enumerate(text):
        use = s1 if (i % 2 == 0) else s2
        out.append(shift_char(ch, -use))   # reverse the shift
    return "".join(out)

try:
    shift1 = int(input("Enter shift1 (1..25): ").strip())
except:
    shift1 = 1
try:
    shift2 = int(input("Enter shift2 (1..25): ").strip())
except:
    shift2 = 1

# --- read input file ---
with open("assignment_files/raw_text.txt", "r") as f:
    original = f.read()

# --- encrypt ---
encrypted = encrypt_two_shifts(original, shift1, shift2)
with open("assignment_files/encrypted_text.txt", "w") as f:
    f.write(encrypted)

# --- decrypt ---
decrypted = decrypt_two_shifts(encrypted, shift1, shift2)
with open("assignment_files/decrypted_text.txt", "w") as f:
    f.write(decrypted)

# --- verify ---
ok = (decrypted == original)
print("Verification:", "MATCH" if ok else "DOES NOT MATCH")

