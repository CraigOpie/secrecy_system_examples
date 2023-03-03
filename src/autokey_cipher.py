#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string

def autokey_encrypt(plaintext, key):
    """Encrypt a plaintext using an Autokey Cipher."""
    alphabet = string.ascii_lowercase
    ciphertext = ''
    for i, c in enumerate(plaintext):
        if c in alphabet:
            p = alphabet.index(c)
            k = alphabet.index(key[i]) if i < len(key) else alphabet.index(plaintext[i-len(key)])
            ciphertext += alphabet[(p + k) % len(alphabet)]
        else:
            ciphertext += c
    return ciphertext

def autokey_decrypt(ciphertext, key):
    """Decrypt a ciphertext using an Autokey Cipher."""
    alphabet = string.ascii_lowercase
    plaintext = ''
    for i, c in enumerate(ciphertext):
        if c in alphabet:
            p = alphabet.index(c)
            k = alphabet.index(key[i]) if i < len(key) else alphabet.index(plaintext[i-len(key)])
            plaintext += alphabet[(p - k) % len(alphabet)]
        else:
            plaintext += c
    return plaintext

# Example usage
plaintext = "attackatdawn"
key = "lemon"
ciphertext = autokey_encrypt(plaintext, key)
decrypted_text = autokey_decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")