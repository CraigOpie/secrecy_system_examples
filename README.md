# Secrecy System Examples as Described by C.E. Shannon in "Communication Theory of Secrecy Systems"

This document provides a summary of our discussions on various classical ciphers and includes Python applications that implement those ciphers.

## Ciphers

The ciphers that we discussed include:

- Autokey Cipher
- Fractional Cipher
- Matrix System Cipher
- Multiple Mixed Alphabet Substitution Cipher
- N-gram Substitution Cipher
- Playfair Cipher
- Single Mixed Alphabet Vigenere Cipher
- Substitution Cipher
- Transposition Cipher
- Vigenere Cipher

## Python Applications

Here are the Python applications that I wrote for each of the ciphers:

### Autokey Cipher

A basic Python program that performs an Autokey Cipher can be found [here]().

This program defines two functions: `autokey_encrypt()`, which encrypts a plaintext string using an Autokey Cipher with a given key; and `autokey_decrypt()`, which decrypts a ciphertext string using the same key.

The Autokey Cipher is a polyalphabetic substitution cipher that uses a keyword to generate a keystream that is combined with the plaintext to produce the ciphertext. It was invented by Blaise de Vigenère in the 16th century, and was later improved by Giovan Battista Bellaso and others. The Autokey Cipher is a generalization of the Vigenere Cipher, in which the key is extended by appending the plaintext itself to the end of the key.

The encryption process proceeds as follows:
- Choose a keyword and remove any spaces or punctuation from it.
- Append the plaintext to the keyword, removing any spaces or punctuation from it as well.
- For each letter in the resulting string:
    - Find the corresponding letter in the alphabet, using 'a' for 0, 'b' for 1, and so on.
    - Find the corresponding letter in the keystream, using the same method.
    - Add the two letters together (mod 26) to get the ciphertext letter.
    - Append the ciphertext letter to the ciphertext.
    - Append the plaintext letter to the keystream.

The decryption process is similar, except that the keystream is generated from the ciphertext instead of the plaintext.

Note that this implementation only supports lowercase letters and ignores spaces and punctuation. It could be easily extended to support other characters and handle these cases in a more sophisticated way.

### Fractional Cipher

A basic Python program that performs a Fractional Cipher can be found [here]().

This program defines three functions: `fractionate()`, which breaks a plaintext into blocks of a given size; `fractional_encrypt()`, which encrypts a plaintext string using a Fractional Cipher with a given key; and `fractional_decrypt()`, which decrypts a ciphertext string using the same key.

The Fractional Cipher is a polygraphic substitution cipher that encrypts pairs of letters using a matrix of fractions. It was invented by Leon Battista Alberti in the 15th century, and was later improved by Johannes Trithemius and others. The matrix consists of a set of fractions, which are used to encode pairs of letters. The plaintext is divided into pairs of letters, which are then encoded using the matrix. The ciphertext consists of the pairs of encoded letters.

The encryption process proceeds as follows:
- Choose a key, which is a sequence of numbers between 0 and 25, and remove any duplicates.
- Generate a matrix of fractions by assigning each number from 0 to 25 to a unique fraction, with the numerator and denominator both less than or equal to the size of the key.
- Divide the plaintext into pairs of letters.
- For each pair of letters:
    - Find the corresponding fractions in the matrix, using the position of the letters in the alphabet.
    - Multiply the fractions together to get the encoded fraction.
    - Find the corresponding letter in the alphabet, using the encoded fraction.
    - Append the encoded letter to the ciphertext.

The decryption process is similar, except that the matrix is generated from the key, and the fractions are inverted before they are multiplied.

Note that this implementation only supports lowercase letters and ignores spaces and punctuation. It could be easily extended to support other characters and handle these cases in a more sophisticated way.

### Matrix System Cipher

A basic Python program that performs a Matrix System Cipher can be found [here]().

This program defines two functions: `create_key()`, which generates a key for a Matrix System Cipher from a given keyword string; `encrypt()`, which uses the key to encrypt a plaintext string using the cipher; and `decrypt()`, which uses the key to decrypt a ciphertext string using the same cipher.

The Matrix System Cipher is a polygraphic substitution cipher that encrypts pairs of letters using a matrix of numbers. It was invented by Félix Delastelle in the late 19th century, and was used by the French Army during World War I. The matrix consists of a set of numbers, which are used to encode pairs of letters. The plaintext is divided into pairs of letters, which are then encoded using the matrix. The ciphertext consists of the pairs of encoded letters.

The encryption process proceeds as follows:
- Choose a key, which is a sequence of numbers between 0 and 25, and remove any duplicates.
- Generate a matrix of numbers by filling a square grid with the key, and then reading off the columns in a specific order.
- Divide the plaintext into pairs of letters.
- For each pair of letters:
    - Find the corresponding numbers in the matrix, using the position of the letters in the alphabet.
    - Add the numbers together (mod 26) to get the encoded number.
    - Find the corresponding letter in the alphabet, using the encoded number.
    - Append the encoded letter to the ciphertext.

The decryption process is similar, except that the matrix is generated from the key, and the numbers are subtracted instead of added.

Note that this implementation only supports lowercase letters and ignores spaces and punctuation. It could be easily extended to support other characters and handle these cases in a more sophisticated way.


### Multiple Mixed Alphabet Substitution Cipher

A basic Python program that performs a Multiple Mixed Alphabet Substitution Cipher can be found [here]().

This program defines three functions: `create_key()`, which generates a random key for a Multiple Mixed Alphabet Substitution Cipher with a given number of alphabets; `encrypt()`, which uses the key to encrypt a plaintext string; and `decrypt()`, which uses the key to decrypt a ciphertext string.

The Multiple Mixed Alphabet Substitution Cipher is a polyalphabetic substitution cipher that uses multiple substitution alphabets. It was invented by Giovan Battista Bellaso in the 16th century, and was later improved by Blaise de Vigenère and others. The cipher uses a series of substitution alphabets, which are repeated cyclically to encrypt the plaintext. Each alphabet is generated from a keyword, using a simple algorithm to map the letters of the alphabet to the letters of the keyword. The plaintext is divided into blocks, which are then encrypted using the substitution alphabets. The ciphertext consists of the encrypted blocks.

The encryption process proceeds as follows:
- Choose a series of keywords, which are used to generate the substitution alphabets. The number of keywords determines the length of the repeating cycle.
- Generate a substitution alphabet for each keyword, using a simple algorithm to map the letters of the alphabet to the letters of the keyword.
- Divide the plaintext into blocks, each of the same length as the keyword.
- For each block of plaintext:
    - Find the corresponding substitution alphabet, using the position of the block in the repeating cycle.
    - Replace each letter in the block with the corresponding letter in the substitution alphabet.
    - Append the encrypted block to the ciphertext.

The decryption process is similar, except that the substitution alphabets are used in reverse order.

Note that this implementation only supports lowercase letters and ignores spaces and punctuation. It could be easily extended to support other characters and handle these cases in a more sophisticated way.

### N-gram Substitution Cipher

A basic Python program that performs an N-gram Substitution Cipher can be found [here]().

This program defines three functions: `create_key()`, which generates a random key for an N-gram Substitution Cipher with a given n-gram size; `encrypt()`, which uses the key to encrypt a plaintext string by replacing each n-gram with its corresponding substitution; and `decrypt()`, which uses the key to decrypt a ciphertext string by reversing the substitutions.

The N-gram Substitution Cipher is a polygraphic substitution cipher that encrypts sequences of letters using a set of substitution rules. It was invented by the German Enigma machine during World War II, and was used by the German military to encrypt their communications. The cipher works by dividing the plaintext into sequences of a fixed length, called n-grams, and then replacing each n-gram with a corresponding sequence of letters, using a set of substitution rules that are generated from a key. The ciphertext consists of the substituted n-grams.

The encryption process proceeds as follows:
- Choose a key, which is a set of substitution rules that map n-grams to sequences of letters.
- Divide the plaintext into n-grams of a fixed length.
- For each n-gram of plaintext:
    - Find the corresponding sequence of letters, using the substitution rules from the key.
    - Append the sequence of letters to the ciphertext.

The decryption process is the inverse of the encryption process.

Note that this implementation only supports lowercase letters and ignores spaces and punctuation. It could be easily extended to support other characters and handle these cases in a more sophisticated way.

### Playfair Cipher

A basic Python program that performs a Playfair Cipher can be found [here]().

This program defines two functions: `create_key()`, which generates a 5x5 key matrix for a Playfair Cipher from a given key string; `encrypt()`, which uses the key matrix to encrypt a plaintext string using the Playfair Cipher; and `decrypt()`, which uses the key matrix to decrypt a ciphertext string using the same cipher.

The Playfair Cipher is a polygraphic substitution cipher that encrypts pairs of letters instead of individual letters. It was invented by Charles Wheatstone in 1854, but was named after Lord Playfair, who promoted its use during the Crimean War. The cipher uses a 5x5 grid of letters, which can be filled with any 25 letters (excluding J) in any order. The plaintext is divided into pairs of letters, which are then encrypted using a set of rules based on their positions in the grid. The ciphertext consists of the pairs of encrypted letters.

The encryption process proceeds as follows:

- If a pair of letters are the same, insert an 'X' between them.
- If the plaintext has an odd length, append an 'X' to the end.
- Divide the plaintext into pairs of letters.
- For each pair of letters:
    - If the letters are in the same row of the grid, replace them with the letters to their right, wrapping around to the left if necessary.
    - If the letters are in the same column of the grid, replace them with the letters below them, wrapping around to the top if necessary.
    - If the letters are not in the same row or column, replace them with the letters at the opposite corners of their rectangle in the grid.

The decryption process is the inverse of the encryption process.

Note that this implementation only supports lowercase letters and ignores spaces and punctuation. It could be easily extended to support other characters and handle these cases in a more sophisticated way.

### Simple Substitution Cipher

A basic Python program that performs a Simple Substitution Cipher can be found [here]().

This program defines three functions: `create_cipher()`, which generates a random substitution cipher using the letters of the alphabet provided as an argument; `encrypt()`, which uses the cipher to encrypt a plaintext string; and `decrypt()`, which uses the cipher to decrypt a ciphertext string.

The Simple Substitution Cipher is a monoalphabetic substitution cipher that replaces each letter in the plaintext with a corresponding letter in the ciphertext. It was one of the earliest known encryption methods, and was used by the ancient Greeks and Romans. The cipher uses a substitution table, which can be any permutation of the 26 letters in the alphabet. The plaintext is encrypted by replacing each letter with its corresponding letter in the substitution table. The ciphertext consists of the substituted letters.

The encryption process proceeds as follows:
- Choose a substitution table, which is a permutation of the 26 letters in the alphabet.
- Divide the plaintext into individual letters.
- For each letter of plaintext:
    - Find the corresponding letter in the substitution table.
    - Append the substituted letter to the ciphertext.

The decryption process is the inverse of the encryption process.

Note that this implementation only supports lowercase letters and ignores spaces and punctuation. It could be easily extended to support other characters and handle these cases in a more sophisticated way.

### Single Mixed Alphabet Vigenere Cipher

A basic Python program that performs a Single Mixed Alphabet Vigenere Cipher can be found [here]().

This program defines two functions: `create_key()`, which generates a mixed alphabet key for a Single Mixed Alphabet Vigenere Cipher from a given keyword string; `encrypt()`, which uses the key to encrypt a plaintext string using the cipher; and `decrypt()`, which uses the key to decrypt a ciphertext string using the same cipher.

The Single Mixed Alphabet Vigenere Cipher is a polyalphabetic substitution cipher that uses a mixed alphabet key to encrypt the plaintext. It was invented by Blaise de Vigenère in the 16th century, and was later improved by Giovan Battista Bellaso and others. The key consists of a sequence of letters, which are used to generate a mixed alphabet for each letter of the plaintext. The plaintext is divided into individual letters, which are then encrypted using the mixed alphabets. The ciphertext consists of the substituted letters.

The encryption process proceeds as follows:
- Choose a key, which is a sequence of letters that is repeated as necessary to encrypt the plaintext.
- Generate a mixed alphabet for each letter of the plaintext, using the corresponding letter of the key and a simple algorithm to mix the letters of the alphabet.
- For each letter of plaintext:
    - Find the corresponding mixed alphabet, using the position of the letter in the plaintext.
    - Find the corresponding letter in the mixed alphabet, using the position of the plaintext letter in the alphabet.
    - Append the substituted letter to the ciphertext.

The decryption process is the inverse of the encryption process.

Note that this implementation only supports lowercase letters and ignores spaces and punctuation. It could be easily extended to support other characters and handle these cases in a more sophisticated way.

### Transposition Cipher

A basic Python program that performs a Transposition Cipher can be found [here]().

This program defines two functions: `create_key()`, which generates a list of column indices for a Transposition Cipher from a given key string; `encrypt()`, which uses the key to encrypt a plaintext string using the cipher; and `decrypt()`, which uses the key to decrypt a ciphertext string using the same cipher.

The Transposition Cipher is a permutation cipher that reorders the letters of the plaintext to form the ciphertext. It was used by the ancient Greeks and Romans, and was later used by the Union Army during the American Civil War. The cipher uses a permutation, which is a reordering of the numbers from 1 to the length of the plaintext. The plaintext is divided into rows of a fixed length, and then the rows are reordered according to the permutation. The ciphertext consists of the reordered rows of letters.

The encryption process proceeds as follows:
- Choose a permutation, which is a reordering of the numbers from 1 to the length of the plaintext.
- Divide the plaintext into rows of a fixed length.
- Reorder the rows of plaintext according to the permutation.
- Concatenate the reordered rows to form the ciphertext.

The decryption process is similar, except that the permutation is inverted and the rows are reordered accordingly.

Note that this implementation only supports lowercase letters and ignores spaces and punctuation. It could be easily extended to support other characters and handle these cases in a more sophisticated way.

### Vigenere Cipher

A basic Python program that performs a Vigenere Cipher can be found [here]().

This program defines two functions: `create_key()`, which generates a key for a Vigenere Cipher from a given keyword string and a desired key length; `encrypt()`, which uses the key to encrypt a plaintext string using the cipher; and `decrypt()`, which uses the key to decrypt a ciphertext string using the same cipher.

The Vigenere Cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt the plaintext. It was invented by Giovan Battista Bellaso in the 16th century, and was later improved by Blaise de Vigenère. The cipher uses a repeating key, which is derived from the keyword by repeating it as necessary to encrypt the plaintext. Each letter of the plaintext is encrypted using a mixed alphabet, which is generated from the corresponding letter of the key using a simple algorithm. The plaintext is divided into individual letters, which are then encrypted using the mixed alphabets. The ciphertext consists of the substituted letters.

The encryption process proceeds as follows:
- Choose a keyword, which is a sequence of letters that is repeated as necessary to encrypt the plaintext.
- Generate a mixed alphabet for each letter of the plaintext, using the corresponding letter of the key and a simple algorithm to mix the letters of the alphabet.
- For each letter of plaintext:
    - Find the corresponding mixed alphabet, using the position of the letter in the plaintext.
    - Find the corresponding letter in the mixed alphabet, using the position of the plaintext letter in the alphabet.
    - Append the substituted letter to the ciphertext.

The decryption process is the inverse of the encryption process.

Note that this implementation only supports lowercase letters and ignores spaces and punctuation. It could be easily extended to support other characters and handle these cases in a more sophisticated way.

## Conclusion

These Python applications provide basic implementations of various classical ciphers. Note that they may not be suitable for use in production systems, as they may be vulnerable to various attacks. However, they can be useful for learning about how these ciphers work and experimenting with different encryption and decryption techniques.