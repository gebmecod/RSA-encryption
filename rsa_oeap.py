from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from generate_key import Key

def encrypt_message(m, k):

    key = RSA.importKey(open(k).read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(m)
    
    return ciphertext

def sign_ciphertext(c, k):

    key = RSA.importKey(open(k).read())
    hash = SHA256.new(c)
    signer = pkcs1_15.new(key)
    signature = signer.sign(hash)

    return signature


def decrypt_message(c, k):

    key = RSA.import_key(open(k).read())
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(c)

    return (message.decode())

def verify_message(s, c, k, d):

    signature = s
    key = RSA.import_key(open(k).read())
    hash = SHA256.new(c)

    try:
        pkcs1_15.new(key).verify(hash, signature)
        print("Signature is valid.")
        return decrypt_message(c, d)
    except(ValueError, TypeError):
        print("Message has been tampered")