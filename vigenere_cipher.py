import random

# Now will be creating the viginere cypher
# And will be trying to decode a given cipher text? two part assignment?

# In this version going to generalize this more for our alphabet
KEY = ""
alphabet = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def vigenere_generate_key(alphabet: list, key_length: int) -> str:
    '''
        Function is used to generate a random key for the viginere cipher
        Arguments: alphabet we are considering and a key length
        Returns: A random string within the alphabet which is the key and has length of the key
    '''
    global KEY
    key = ""
    for i in range(0, key_length):
        index = random.randint(0, 26)
        key = key + alphabet[index]

    KEY = key

    return key


# Allowing key to be passed in for testing purposes
def vigenere_encode(message: str, key: str = None) -> str:
    if key is None:
        key = KEY

    # Need to mirror the key across the entire length of the message (the full key)
    # So if key is 'NO' but message is 'HELP ME', need to "extend" the key
    full_key = ""
    if len(key) != len(message):
        for i in range(len(message)):
            full_key += key[i % len(key)]
    else:
        full_key = key

    # Now can actually encrypt the message
    enc_message = ""
    for i in range(len(message)):
        enc_letter_indx = (alphabet.index(message[i]) + alphabet.index(full_key[i])) % 27
        print(enc_letter_indx)
        enc_message += alphabet[enc_letter_indx]

    return enc_message


def vigenere_decode(message_enc: str, key: str = None) -> str:
    if key is None:
        key = KEY

    # Need to remap again
    full_key = ""
    if len(key) != len(message_enc):
        for i in range(len(message_enc)):
            full_key += key[i % len(key)]
    else:
        full_key = key

    dec_message = ""
    for i in range(len(message_enc)):
        dec_letter_indx = (alphabet.index(message_enc[i]) - alphabet.index(full_key[i])) % 27
        dec_message += alphabet[dec_letter_indx]


    return dec_message

message = "HELP ME"
key = "NONONON"
enc_message = vigenere_encode(key, message)
dec_message = vigenere_decode(enc_message, key)
print(dec_message)
print(enc_message)