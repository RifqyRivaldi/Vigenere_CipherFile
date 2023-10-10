#!/usr/bin/env python
# coding: utf-8

# In[2]:


def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_len = len(key)

    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            # Mendapatkan indeks dari huruf dalam alfabet (0-25)
            plain_char_idx = ord(char.lower()) - ord('a')
            key_char = key[i % key_len].lower()
            key_char_idx = ord(key_char) - ord('a')

            # Enkripsi karakter
            encrypted_char_idx = (plain_char_idx + key_char_idx) % 26
            encrypted_char = chr(encrypted_char_idx + ord('a'))

            # Mengatur huruf besar atau kecil sesuai dengan huruf aslinya
            if char.isupper():
                encrypted_char = encrypted_char.upper()

            encrypted_text += encrypted_char
        else:
            # Karakter non-alfabet ditambahkan tanpa enkripsi
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_len = len(key)

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            # Mendapatkan indeks dari huruf dalam alfabet (0-25)
            encrypted_char_idx = ord(char.lower()) - ord('a')
            key_char = key[i % key_len].lower()
            key_char_idx = ord(key_char) - ord('a')

            # Dekripsi karakter
            decrypted_char_idx = (encrypted_char_idx - key_char_idx) % 26
            decrypted_char = chr(decrypted_char_idx + ord('a'))

            # Mengatur huruf besar atau kecil sesuai dengan huruf aslinya
            if char.isupper():
                decrypted_char = decrypted_char.upper()

            decrypted_text += decrypted_char
        else:
            # Karakter non-alfabet ditambahkan tanpa dekripsi
            decrypted_text += char

    return decrypted_text

# Contoh penggunaan:
plaintext = "Rifqy Rivaldi"
kunci = "Madiun"

# Enkripsi
ciphertext = vigenere_encrypt(plaintext, kunci)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi
decrypted_text = vigenere_decrypt(ciphertext, kunci)
print("Decrypted Text:", decrypted_text)


# In[ ]:




