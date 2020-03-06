from codecs import encode, decode
from base64 import b64encode

def hex_decode_64_encode(to_encode):
    return b64encode(decode(to_encode, 'hex'))
