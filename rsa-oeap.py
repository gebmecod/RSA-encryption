from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from generate_key import Key

m = b'You can attack now'
key_pair = Key()
public_key = key_pair.public_key()
private_key = key_pair.private_key()

def encrypt_message(m, k):

    key = RSA.importKey(k)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(m)
    
    return ciphertext


def decrypt_message(c, k):

    key = RSA.import_key(k)
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(c)

    return message

c = encrypt_message(m, public_key)
message = decrypt_message(c, private_key)

print(message)