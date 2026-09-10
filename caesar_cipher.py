import random

# Key will be an integer randomized
# Key represents the number of letters to shift in the alphabet (our 27 character alphabet)
KEY = 1


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
    


message = "MESSAGZ"
#print(message)

#message_enc = enc(message)
#print(message_enc)

#message_dec = dec(message_enc)
#print(message_dec)

# This will be the encryption function
enc_message = ""
for i, letter in enumerate(message):
    if letter.isalpha():
        num = ord(letter)
        if num + KEY > 90:
            #print("Rollover handling")
            #print(num)
            new_char_ascii = (num + KEY - 90) + 63
            #print(new_char_ascii)
        elif num == 20:
            new_char_ascii = 63 + KEY
        else:
            new_char_ascii = num + KEY

        if new_char_ascii == 64:
            new_char_ascii = 32
        enc_letter = chr(new_char_ascii)
        enc_message = enc_message + enc_letter



print(message)
print(enc_message)

# Now we can do the decryption function
