def xor(string_1, string_2):
    return bytes([i ^ n for i, n in zip(bytes.fromhex(string_1), bytes.fromhex(string_2))])
