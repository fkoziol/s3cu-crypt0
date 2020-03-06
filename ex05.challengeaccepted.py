import onetimepad

def onetimepad_convertor(input_1, input_2, action = 'encode'):
    if action == 'encode':
        return onetimepad.encrypt(input_1, input_2)
    if action == 'decode':
        return onetimepad.decrypt(input_1, input_2)
