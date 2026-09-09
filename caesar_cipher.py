import random

# Key will be an integer randomized
# Key represents the number of letters to shift in the alphabet (our 27 character alphabet)
KEY = 0


def enc(message: str) -> str:
    '''
    Function is used to encrypt a string of text using the Caesar cipher method.
    Accepts: String of text to be encrypted
    Returns: Encrypted string
    '''
    for letter in message:
        letter = letter + KEY
    pass

def dec(message_enc: str) -> str:
    '''
    Function is used to decrypt a string of text using the Caesar cipher method.
    Accepts: String of text to be decrypted
    Returns: Decrypted string
    '''
    for letter in message_enc:
        letter = letter - KEY
    pass

def gen():
    '''
    Function randomly generates the key
    '''
    global KEY
    KEY = random.randint(0, 27)
    


message = "Hello World"
print(message)

message_enc = enc(message)
print(message_enc)

message_dec = dec(message_enc)
print(message_dec)