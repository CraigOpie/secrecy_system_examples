#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string

def create_key(keyword, alphabet=string.ascii_lowercase):
    """Create a mixed alphabet key for a Single Mixed Alphabet Vigenere Cipher."""
    keyword = keyword.lower().replace(' ', '')
    key = list(alphabet)
    for c in keyword:
        if c not in key:
            key.append(c)
    return ''.join(key)

def encrypt(plaintext, keyword):
    """Encrypt a plaintext using a Single Mixed Alphabet Vigenere Cipher."""
    alphabet = string.ascii_lowercase
    key = create_key(keyword)
    ciphertext = ''
    for i, c in enumerate(plaintext):
        k = key[i % len(key)]
        p = alphabet.index(c)
        c = key[(p + alphabet.index(k)) % len(alphabet)]
        ciphertext += c
    return ciphertext

def decrypt(ciphertext, keyword):
    """Decrypt a ciphertext using a Single Mixed Alphabet Vigenere Cipher."""
    alphabet = string.ascii_lowercase
    key = create_key(keyword)
    plaintext = ''
    for i, c in enumerate(ciphertext):
        k = key[i % len(key)]
        c = key.index(c)
        p = (c - alphabet.index(k)) % len(alphabet)
        plaintext += alphabet[p]
    return plaintext

# Example usage
plaintext = "the quick brown fox jumps over the lazy dog"
keyword = "keyword"
ciphertext = encrypt(plaintext, keyword)
decrypted_text = decrypt(ciphertext, keyword)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")
