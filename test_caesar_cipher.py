import caesar_cipher

def test_caesar_cipher():
    for i in range(1, 26):
        message = "HEY THIS IS JOE"
        enc_message = caesar_cipher.enc(message, i)
        dec_message = caesar_cipher.dec(enc_message, i)
        assert dec_message == message

