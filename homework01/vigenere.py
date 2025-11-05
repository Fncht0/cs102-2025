def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    for i in range(len(plaintext)):
        p = plaintext[i]
        k = keyword[i]

        if p.isalpha():
            shift = ord(k.lower()) - ord('a')
            if p.isupper():
                ciphertext += chr((ord(p) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(p) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += p
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]

    for i in range(len(ciphertext)):
        c = ciphertext[i]
        k = keyword[i]

        if c.isalpha():
            shift = ord(k.lower()) - ord('a')
            if c.isupper():
                plaintext += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += c
    return plaintext