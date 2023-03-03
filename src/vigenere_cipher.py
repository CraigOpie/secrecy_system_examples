#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string

def create_key(keyword, n):
    """Create a key for a Vigenere Cipher."""
    key = ''
    for i in range(n):
        key += keyword[i % len(keyword)]
    return key

def encrypt(plaintext, keyword):
    """Encrypt a plaintext using a Vigenere Cipher."""
    alphabet = string.ascii_lowercase
    ciphertext = ''
    key = create_key(keyword, len(plaintext))
    for i, c in enumerate(plaintext):
        p = alphabet.index(c)
        k = alphabet.index(key[i])
        c = alphabet[(p + k) % len(alphabet)]
        ciphertext += c
    return ciphertext

def decrypt(ciphertext, keyword):
    """Decrypt a ciphertext using a Vigenere Cipher."""
    alphabet = string.ascii_lowercase
    plaintext = ''
    key = create_key(keyword, len(ciphertext))
    for i, c in enumerate(ciphertext):
        p = alphabet.index(c)
        k = alphabet.index(key[i])
        c = alphabet[(p - k) % len(alphabet)]
        plaintext += c
    return plaintext

# Example usage
plaintext = "the quick brown fox jumps over the lazy dog"
keyword = "keyword"
ciphertext = encrypt(plaintext, keyword)
decrypted_text = decrypt(ciphertext, keyword)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")
