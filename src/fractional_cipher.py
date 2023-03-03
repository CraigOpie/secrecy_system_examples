#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string
import math

def fractionate(plaintext, block_size):
    """Fractionate a plaintext into blocks of a given size."""
    plaintext = plaintext.replace(' ', '')
    blocks = []
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        if len(block) < block_size:
            block += 'x' * (block_size - len(block))
        blocks.append(block)
    return blocks

def fractional_encrypt(plaintext, key):
    """Encrypt a plaintext using a Fractional Cipher."""
    alphabet = string.ascii_lowercase
    key_length = len(key)
    blocks = fractionate(plaintext, key_length)
    ciphertext = ''
    for block in blocks:
        for i in range(key_length):
            column = key.index(str(i+1))
            for j in range(len(block)):
                if j % key_length == column:
                    p = alphabet.index(block[j])
                    c = (p * key_length + i) % len(alphabet)
                    ciphertext += alphabet[c]
    return ciphertext

def fractional_decrypt(ciphertext, key):
    """Decrypt a ciphertext using a Fractional Cipher."""
    alphabet = string.ascii_lowercase
    key_length = len(key)
    blocks = fractionate(ciphertext, key_length)
    plaintext = ''
    for block in blocks:
        for j in range(key_length):
            column = key.index(str(j+1))
            for i in range(len(block)):
                if i % key_length == column:
                    c = alphabet.index(block[i])
                    p = math.floor((c - j) / key_length) % len(alphabet)
                    plaintext += alphabet[p]
    return plaintext

# Example usage
plaintext = "the quick brown fox jumps over the lazy dog"
key = "3142"
ciphertext = fractional_encrypt(plaintext, key)
decrypted_text = fractional_decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted_text}")