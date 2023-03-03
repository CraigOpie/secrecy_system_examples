#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string

def create_key(keyword, alphabet=string.ascii_lowercase):
    """Create a key for a Matrix System Cipher."""
    keyword = keyword.lower().replace(' ', '')
    keyword = ''.join([c for c in keyword if c in alphabet])
    key = [[keyword[i], keyword[(i+1) % len(keyword)]] for i in range(len(keyword))]
    for c in alphabet:
        if c not in keyword:
            key.append([c, ''])
    return key

def encrypt(plaintext, keyword):
    """Encrypt a plaintext using a Matrix System Cipher."""
    key = create_key(keyword)
    num_cols = len(key)
    num_rows = (len(plaintext) + num_cols - 1) // num_cols
    plaintext += ' ' * (num_rows * num_cols - len(plaintext))
    matrix = [[None for _ in range(num_cols)] for _ in range(num_rows)]
    for i, c in enumerate(plaintext):
        row, col = divmod(i, num_cols)
        matrix[row][col] = c
    ciphertext = ''
    for i in range(num_cols):
        for j in range(num_rows):
            c = key[i][1] if j == key[i][0] else key[i][0]
            ciphertext += matrix[j][i] if matrix[j][i] else c
    return ciphertext

def decrypt(ciphertext, keyword):
    """Decrypt a ciphertext using a Matrix System Cipher."""
    key = create_key(keyword)
    num_cols = len(key)
    num_rows = (len(ciphertext) + num_cols - 1) // num_cols
    matrix = [[None for _ in range(num_cols)] for _ in range(num_rows)]
    for i, c in enumerate(ciphertext):
        row, col = divmod(i, num_cols)
        matrix[row][col] = c
    plaintext = ''
    for i in range(num_cols):
        for j in range(num_rows):
            c = key[i][1] if j == key[i][0] else key[i][0]
            plaintext += matrix[j][i] if matrix[j][i] and matrix[j][i] != c else ''
    return plaintext.rstrip()

# Example usage
plaintext = "the quick brown fox jumps over the lazy dog"
keyword = "crypto"
ciphertext = encrypt(plaintext, keyword)
decrypted_text = decrypt(ciphertext, keyword)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")