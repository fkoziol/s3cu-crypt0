from binascii import unhexlify

with open(file) as data_file:
    ciphertext_list = []
    for line in data_file:
        ciphertext_list.append(unhexlify(line.strip()))
    
candidates = list()
for (line_nb, ciphertext) in enumerate(ciphertext_list):
    try:
        message = attack_single_byte_xor(ciphertext)['message']
    except InvalidMessageException:
        pass
    else:
        candidates.append({
            'line_nb': line_nb,
            'ciphertext': ciphertext,
            'message': message
        })
        
if len(candidates) > 1:
    print("Error: more than one candidate")
else:
    for (key, value) in candidates[0].items():
        print(f'{key}: {value}')
