import caesar_cipher

message_1 = "HEY THIS IS JOE"
enc_message = caesar_cipher.enc(message_1, 1)
dec_message = caesar_cipher.dec(enc_message, 1)
assert dec_message == message_1


message_2 = "THIS IS THE CAESAR CIPHER EXCERCISE"
enc_message = caesar_cipher.enc(message_2, 2)
dec_message = caesar_cipher.dec(enc_message, 2)
assert dec_message == message_2

message_3 = "THIS IS THE CAESAR CIPHER EXCERCISE"
enc_message = caesar_cipher.enc(message_3, 13)
dec_message = caesar_cipher.dec(enc_message, 13)
assert dec_message == message_3