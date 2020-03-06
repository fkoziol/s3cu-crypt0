from binascii import hexlify

def xor(input_1, input_2):
    return bytes([ x^y for (x,y) in zip(input_1, input_2)])

def imp_rep(input_1, key):
    full_key = key*(len(message)//len(key) + 1)
    return hexlify(xor(message, keystream))
