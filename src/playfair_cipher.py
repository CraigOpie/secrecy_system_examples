#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string

def create_key(key):
    """Create a 5x5 key matrix for a Playfair Cipher."""
    alphabet = string.ascii_lowercase.replace('j', '')
    key = key.lower().replace('j', 'i')
    key = ''.join([c for c in key if c in alphabet])
    key += alphabet[len(key):]
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return matrix

def get_positions(matrix, c):
    """Get the row and column positions of a character in a Playfair Cipher key matrix."""
    for i, row in enumerate(matrix):
        if c in row:
            return i, row.index(c)

def encrypt(plaintext, key):
    """Encrypt a plaintext using a Playfair Cipher."""
    matrix = create_key(key)
    alphabet = string.ascii_lowercase.replace('j', '')
    plaintext = plaintext.lower().replace('j', 'i')
    plaintext = ''.join([c for c in plaintext if c in alphabet])
    if len(plaintext) % 2 == 1:
        plaintext += 'x'
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        c1, c2 = plaintext[i], plaintext[i+1]
        r1, c1 = get_positions(matrix, c1)
        r2, c2 = get_positions(matrix, c2)
        if r1 == r2:
            ciphertext += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            ciphertext += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
    return ciphertext

def decrypt(ciphertext, key):
    """Decrypt a ciphertext using a Playfair Cipher."""
    matrix = create_key(key)
    alphabet = string.ascii_lowercase.replace('j', '')
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        c1, c2 = ciphertext[i], ciphertext[i+1]
        r1, c1 = get_positions(matrix, c1)
        r2, c2 = get_positions(matrix, c2)
        if r1 == r2:
            plaintext += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            plaintext += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            plaintext += matrix[r1][c2] + matrix[r2][c1]
    return plaintext.replace('x', '')

# Example usage
plaintext = "the quick brown fox jumps over the lazy dog"
key = "keyword"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")
