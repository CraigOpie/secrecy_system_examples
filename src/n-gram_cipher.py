#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string
import random

def create_key(n, alphabet=string.ascii_lowercase):
    """Create a random key for an N-gram Substitution Cipher."""
    keys = {}
    for i in range(len(alphabet) // n):
        ngram = alphabet[i*n:(i+1)*n]
        key = list(ngram)
        random.shuffle(key)
        keys[ngram] = ''.join(key)
    return keys

def encrypt(plaintext, n, keys):
    """Encrypt a plaintext using an N-gram Substitution Cipher."""
    alphabet = string.ascii_lowercase
    ciphertext = ''
    for i in range(0, len(plaintext), n):
        ngram = plaintext[i:i+n]
        if len(ngram) == n:
            ciphertext += keys[ngram]
        else:
            ciphertext += ngram
    return ciphertext

def decrypt(ciphertext, n, keys):
    """Decrypt a ciphertext using an N-gram Substitution Cipher."""
    alphabet = string.ascii_lowercase
    plaintext = ''
    for i in range(0, len(ciphertext), n):
        ngram = ciphertext[i:i+n]
        if len(ngram) == n:
            plaintext += keys[ngram]
        else:
            plaintext += ngram
    return plaintext

# Example usage
plaintext = "the quick brown fox jumps over the lazy dog"
n = 2
keys = create_key(n)
ciphertext = encrypt(plaintext, n, keys)
decrypted_text = decrypt(ciphertext, n, keys)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")
