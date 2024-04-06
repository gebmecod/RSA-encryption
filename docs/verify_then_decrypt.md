# Verifying Message

**Function:**
```
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
```
**Parameters:**  
`s`: Signature File  
`c`: Ciphertext  
`k`: Signing Public Key  
`d`: Encryption Public Key  

**Output:**  
- If Verification Succeeds: Proceeds decryption.
- Else if Verification Fails: Returns Value Error and prints the message "Message has been tampered"

**Code Explanation**
`key = RSA.import_key(open(k).read())`: reads the signing public key, and converts its content to an RSA key object.  
`hash = SHA256.new(c)`: create a new SHA256 object and calculates the hash of the ciphertext.  
`pkcs1_15.new(key).verify(hash, signature)`: compares the hash of ciphertext with the signature.  

References: https://www.youtube.com/watch?v=z-EnysBSstA&t=566s

# Decrypting the Encrypted Message

**Function**
```
def decrypt_message(c, k):

    key = RSA.import_key(open(k).read())
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(c)

    return (message.decode())
```
**Parameters:**  
`c`: Ciphertext to be decrypted  
`k`: Encryption Public Key  

**Output:**  
- Returns the decrypted message  

**Code Explanation:**  

`key = RSA.importKey(open(k).read())`: opens the encryption public key file, reads the contents of the file, then converts the content of the file into an RSA key object.  
`cipher = PKCS1_OAEP.new(key)`: creates a new PKCS1 OAEP cipher object using the RSA key.  
`message = cipher.decrypt(c)`: decrypts the ciphertext `c` using the cipher object.  

References: https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html
