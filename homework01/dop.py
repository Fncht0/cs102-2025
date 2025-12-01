def decrypt_poly_shift(ciphertext: str, odd_shift: int, even_shift: int) -> str:
    alph_up = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alph_low = alph_up.lower()
    n = len(alph_up)
    plaintext = []

    for i, ch in enumerate(ciphertext, start=1):
        if ch in alph_up:
            shift = odd_shift if (i % 2 == 1) else even_shift
            new_index = (alph_up.index(ch) - shift) % n
            plaintext.append(alph_up[new_index])
        elif ch in alph_low:
            shift = odd_shift if (i % 2 == 1) else even_shift
            new_index = (alph_low.index(ch) - shift) % n
            plaintext.append(alph_low[new_index])
        else:
            plaintext.append(ch)

    return "".join(plaintext)
