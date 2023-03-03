#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string
import random

def create_cipher(alphabet):
    """Create a random substitution cipher."""
    cipher = {}
    chars = list(alphabet)
    random.shuffle(chars)
    for i, c in enumerate(alphabet):
        cipher[c] = chars[i]
    return cipher

def encrypt(plaintext, cipher):
    """Encrypt a plaintext using a substitution cipher."""
    ciphertext = ''
    for c in plaintext:
        if c in cipher:
            ciphertext += cipher[c]
        else:
            ciphertext += c
    return ciphertext

def decrypt(ciphertext, cipher):
    """Decrypt a ciphertext using a substitution cipher."""
    plaintext = ''
    for c in ciphertext:
        if c in cipher.values():
            for k, v in cipher.items():
                if v == c:
                    plaintext += k
        else:
            plaintext += c
    return plaintext

# Example usage
alphabet = string.ascii_lowercase
cipher = create_cipher(alphabet)
plaintext = "hello world"
ciphertext = encrypt(plaintext, cipher)
decrypted_text = decrypt(ciphertext, cipher)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")