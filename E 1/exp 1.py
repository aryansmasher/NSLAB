def ceaser_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shiftbase = 65 if char.isupper() else 97
            result += char((ord(char)-shiftbase + shift) % 26 + shiftbase)
        else:
            result += char
        return result


def ceaser_decrypt(cipher, shift):
    return ceaser_encrypt(cipher, -shift)


def vignere_encrypt(text, key):
    result = ""
    key = key.upper()
    j = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[j % len(key)])-65
            shiftbase = 65 if char.isupper() else 97
            result += char((ord(char)-shiftbase+shift) % 26+shiftbase)
            j += 1
        else:
            result += char
        return result


def vignere_decrypt(cipher, key):
    result = ""
    key = key.upper()
    j = 0
    for char in cipher:
        if char.isalpha():
            shift = ord(key[j % len(key)])-65
            shiftbase = 65 if char.isupper() else 97
            result += char((ord(char)-shiftbase-shift) % 26+shiftbase)
            j += 1
        else:
            result += char
        return result


