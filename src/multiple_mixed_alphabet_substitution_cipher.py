#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string
import random

def create_key(n, alphabet=string.ascii_lowercase):
    """Create a random key for a Multiple Mixed Alphabet Substitution Cipher."""
    keys = []
    for i in range(n):
        key = list(alphabet)
        random.shuffle(key)
        keys.append(''.join(key))
    return keys

def encrypt(plaintext, keys):
    """Encrypt a plaintext using a Multiple Mixed Alphabet Substitution Cipher."""
    alphabet = string.ascii_lowercase
    ciphertext = ''
    for i, c in enumerate(plaintext):
        k = keys[i % len(keys)]
        if c in alphabet:
            p = alphabet.index(c)
            c = k[p]
        ciphertext += c
    return ciphertext

def decrypt(ciphertext, keys):
    """Decrypt a ciphertext using a Multiple Mixed Alphabet Substitution Cipher."""
    alphabet = string.ascii_lowercase
    plaintext = ''
    for i, c in enumerate(ciphertext):
        k = keys[i % len(keys)]
        if c in alphabet:
            p = k.index(c)
            c = alphabet[p]
        plaintext += c
    return plaintext

# Example usage
plaintext = "the quick brown fox jumps over the lazy dog"
keys = create_key(3)
ciphertext = encrypt(plaintext, keys)
decrypted_text = decrypt(ciphertext, keys)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")
