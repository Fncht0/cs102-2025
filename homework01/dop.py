def decrypt_poly_shift(ciphertext, odd_shift, even_shift):
    alph_up = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alph_low = alph_up.lower()
    plaintext = ""
    for i, ch in enumerate(ciphertext, start=1):
        if ch in alph_up:
            alph = alph_up
            shift = odd_shift if i % 2 == 1 else even_shift
            new_index = (alph.index(ch) - shift) % len(alph)
            plaintext += alph[new_index]
        elif ch in alph_low:
            alph = alph_low
            shift = odd_shift if i % 2 == 1 else even_shift
            new_index = (alph.index(ch) - shift) % len(alph)
            plaintext += alph[new_index]
        else:
            plaintext += ch
        return plaintext
