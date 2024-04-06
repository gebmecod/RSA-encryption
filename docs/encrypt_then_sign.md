# Encrypting the Message

**Function:**
```
def encrypt_message(m, k):

    key = RSA.importKey(open(k).read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(m)
    
    return ciphertext
```
**Parameters:**  
`m`: Message to be encrypted  
`k`: Encryption Public Key Filename

**Output:**  
- Returns encrypted message `ciphertext`

**Code Explanation:**  

`key = RSA.importKey(open(k).read())`: opens the public key file, reads the contents of the file, then converts the content of the file into an RSA key object.  
`cipher = PKCS1_OAEP.new(key)`: creates a new PKCS1 OAEP cipher object using the RSA key.  
`ciphertext = cipher.encrypt(m)`: encrypts the plaintext message `m` using the cipher object.  

References: https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html

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
