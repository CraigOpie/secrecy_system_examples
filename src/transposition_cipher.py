#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string

def create_key(key):
    """Create a list of column indices for a Transposition Cipher."""
    key = key.lower().replace(' ', '')
    key = ''.join([c for c in key if c in string.ascii_lowercase])
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    return key_order

def encrypt(plaintext, key):
    """Encrypt a plaintext using a Transposition Cipher."""
    key_order = create_key(key)
    num_cols = len(key)
    num_rows = (len(plaintext) + num_cols - 1) // num_cols
    plaintext += ' ' * (num_rows * num_cols - len(plaintext))
    ciphertext = ''
    for i in range(num_cols):
        for j in range(num_rows):
            idx = j * num_cols + key_order[i]
            ciphertext += plaintext[idx]
    return ciphertext

def decrypt(ciphertext, key):
    """Decrypt a ciphertext using a Transposition Cipher."""
    key_order = create_key(key)
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    plaintext = ''
    for i in range(num_cols):
        for j in range(num_rows):
            idx = j * len(key_order) + key_order.index(i)
            plaintext += ciphertext[idx]
    return plaintext.rstrip()

# Example usage
plaintext = "the quick brown fox jumps over the lazy dog"
key = "crypto"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")
