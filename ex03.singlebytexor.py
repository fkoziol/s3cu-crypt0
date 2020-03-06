def xor(input_1, input_2):
    return bytes([ x^y for (x,y) in zip(a, b)])

def attack_single_byte_xor(input_1):
    # a variable to keep track of the best candidate so far
    best = None
    for i in range(2**8): # for every possible key
        # converting the key from a number to a byte
        candidate_key = i.to_bytes(1, byteorder='big')
        keystream = candidate_key*len(input_1)
        candidate_message = xor(input_1, keystream)
        nb_letters = sum([ x in list(range(97, 122)) + [32] for x in candidate_message])
        # if the obtained message has more letters than any other candidate before
        if best == None or nb_letters > best['nb_letters']:
            # store the current key and message as our best candidate so far
            best = {"message": candidate_message, 'nb_letters': nb_letters, 'key': candidate_key}
    return best
