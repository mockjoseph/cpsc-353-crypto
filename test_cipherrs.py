import caesar_cipher
import vigenere_cipher

def test_caesar_cipher():
    for i in range(1, 26):
        message = "HEY THIS IS JOE"
        enc_message = caesar_cipher.enc(message, i)
        dec_message = caesar_cipher.dec(enc_message, i)
        assert dec_message == message

def test_vigenere_cipher():
    alphabet = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    message = "HEY THIS IS JOE"
    key = vigenere_cipher.vigenere_generate_key(alphabet, 10)
    enc_message = vigenere_cipher.vigenere_encode(message, key)
    dec_message = vigenere_cipher.vigenere_decode(enc_message, key)
    assert dec_message == message