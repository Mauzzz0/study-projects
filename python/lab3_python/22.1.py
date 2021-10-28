def encrypt_caesar(msg: str, shift: int = 3):
    res = ""
    for i in range(len(msg)):
        c = msg[i]
        if c.isupper():
            res += chr((ord(c) + shift-65) % 26 + 65)
        else:
            res += chr((ord(c) + shift - 97) % 26 + 97)
    return res
