import random

# Key will be an integer randomized
# Key represents the number of letters to shift in the alphabet (our 27 character alphabet)
KEY = None

# Z = 90 (ascii)
# A = 65 (ascii)
# ' ' = 32 (ascii)
# Going to always pretend " " is 64 for these cases, will do handling as needed

# Key can be optionally passed in for test cases
# Key defaults to global key that is generated in gen()
def enc(message: str, key: int = None) -> str:
    '''
    Function is used to encrypt a string of text using the Caesar cipher method.
    Accepts: String of text to be encrypted
    Returns: Encrypted string
    '''
    if key is None:
        key = KEY
    enc_message = ""
    for letter in message:
        num = ord(letter)
        # Assign the new character with ascii number
        if num == 32:
            new_char_ascii = 64 + key
        else:
            new_char_ascii = num + key

        # Check for overflow cases
        if new_char_ascii > 90:
            #print("Rollover handling")
            #print(num)
            offset = new_char_ascii - 90
            new_char_ascii = 63 + offset
            #print(new_char_ascii)

        # Reset for space
        if new_char_ascii == 64:
            new_char_ascii = 32
                
        # Build the encrypted string
        enc_letter = chr(new_char_ascii)
        enc_message = enc_message + enc_letter

    return enc_message

# Key can be optionally passed in for test cases
# Key defaults to global key that is generated in gen()
def dec(enc_message: str, key: int = None) -> str:
    '''
    Function is used to decrypt a string of text using the Caesar cipher method.
    Accepts: String of text to be decrypted
    Returns: Decrypted string
    '''
    if key is None:
        key = KEY
    dec_message = ""
    for letter in enc_message:
        
        num = ord(letter)
        #print(num)
        # Assign the new character (decrypted) as its ascii value
        if num == 32:
            #print("hit space")
            new_char_ascii = 64 - KEY
        else:
            new_char_ascii = num - KEY

        # Check the overflow condition
        if new_char_ascii < 64:
            offset = new_char_ascii - 64
            offset = -(offset)
            new_char_ascii = 91 - offset

        # Reset for space
        if new_char_ascii == 64:
            #print('hit this case')
            new_char_ascii = 32

        dec_letter = chr(new_char_ascii)
        dec_message = dec_message + dec_letter

    return dec_message

def gen():
    '''
    Function randomly generates the key
    '''
    global KEY
    KEY = random.randint(0, 26)
    print(KEY)

# Example run:    
message = "ATTACK DEFEND"
gen()
enc_message = enc(message)
print("Original Message:", message)
print("Message encrypted:", enc_message)
print("Decrypting Message...")
dec_message = dec(enc_message)
print("Decrypted Message:", dec_message)

message = "MESSAGZ"
#print(message)

#message_enc = enc(message)
#print(message_enc)

#message_dec = dec(message_enc)
#print(message_dec)


print(message)
enc_message = enc(message)
print(enc_message)

# Now we can do the decryption function
dec_message = dec(enc_message)
print(dec_message)
        
