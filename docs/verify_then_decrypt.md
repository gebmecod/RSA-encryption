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
`c`: Encrypted Message  
`k`: Signing Public Key  
`d`: Encryption Public Key  

**Output:**  
- If Verification Succeeds: Proceeds decryption.
- Else if Verification Fails: Returns Value Error and prints the message "Message has been tampered"    

References: https://www.youtube.com/watch?v=z-EnysBSstA&t=566s

# Signing the Encrypted Message

**Function**
```
def sign_ciphertext(c, k):

    key = RSA.importKey(open(k).read())
    hash = SHA256.new(c)
    signer = pkcs1_15.new(key)
    signature = signer.sign(hash)

    return signature
```
**Parameters:**  
`c`: Ciphertext to be signed  
`k`: Signing Private Key Filename

**Output:**  
- Returns digital signature `signature`

**Code Explanation:**  

`key = RSA.importKey(open(k).read())`: opens the public key file, reads the contents of the file, then converts the content of the file into an RSA key object.  
`hash = SHA256.new(c)`: create a new SHA-256 hash object then hash the ciphertext `c`.  
`signer = pkcs1_15.new(key)`: create a new pkcs1_v1_5  signature object using the private key.  
`signature = signer.sign(hash)`: sign the hash of the ciphertext using the signature object.  

References: https://www.youtube.com/watch?v=z-EnysBSstA&t=566s
