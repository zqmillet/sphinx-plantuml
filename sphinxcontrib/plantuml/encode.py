from string import digits
from string import ascii_lowercase
from string import ascii_uppercase
from zlib import compress
from base64 import b64encode

PLANTUML_ALPHABET = digits + ascii_uppercase + ascii_lowercase + '-_'
BASE64_ALPHABET = ascii_uppercase + ascii_lowercase + digits + '+/'
BASE64_TO_PLANTUML = bytes.maketrans(BASE64_ALPHABET.encode('utf8'), PLANTUML_ALPHABET.encode('utf8'))

def encode(text: str) -> str:
    compressed_bytes = compress(text.encode('utf8'))
    return b64encode(compressed_bytes[2:-4]).translate(BASE64_TO_PLANTUML).decode('utf8')
