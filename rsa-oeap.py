from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from generate_key import Key

m = b'You can attack now'
encryption_key = Key()
encryption_public_key = encryption_key.public_key()
encryption_private_key = encryption_key.private_key()

signing_key = Key()
signing_public_key = signing_key.public_key()
signing_private_key = signing_key.private_key()

def encrypt_message(m, k):

    key = RSA.importKey(k)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(m)
    
    return ciphertext

def sign_ciphertext(c, k):

    key = RSA.importKey(k)
    hash = SHA256.new(c)
    signer = pkcs1_15.new(key)
    signature = signer.sign(hash)

    return signature


def decrypt_message(c, k):

    key = RSA.import_key(k)
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(c)

    print(message.decode())

def verify_message(s, c, k):

    signature = s
    key = RSA.import_key(k)
    hash = SHA256.new(c)

    try:
        pkcs1_15.new(key).verify(hash, signature)
        print("Signature is valid.")
        decrypt_message(c, encryption_private_key)
    except(ValueError, TypeError):
        print("Message has been tampered")

ciphertext = encrypt_message(m, encryption_public_key)
signature = sign_ciphertext(ciphertext, signing_private_key)
verify_message(signature, ciphertext, signing_public_key)