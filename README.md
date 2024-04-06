# RSA-encryption
CMSC 134 - Machine Problem 2: RSA Encryption

An implementation for encrypting and decrypting message using RSA-OAEP with authenticity. The goal is to provide secure communication between parties ensuring confidentiality, integrity, and authenticity of the exchanged messages.

Key Components:  
---
1. **Key Generation**  
            - The program can generate separate key pairs for encryption and signing. This separation ensures that different keys are used for encryption and signing, enhancing security by preventing potential attacks that exploit key reuse vulnerabilities.
2. **Encrypt-then-Sign Scheme**  
            - To achieve authenticated encryption, the program follows the encrypt-then-sign scheme. First, it encrypts the message using RSA-OAEP encryption with the provided key (k) for confidentiality. Then, it signs the encrypted ciphertext using RSA digital signatures with another provided key (k) for authenticity and integrity. This approach ensures that the recipient can verify the authenticity of the message before decryption, mitigating the risk of tampering or impersonation.
3. **Cryptographic Libraries**  
            - Rather than implementing cryptographic algorithms from scratch, the program utilizes established cryptographic libraries of Python PyCrypto and PyCryptodome (see: https://pycryptodome.readthedocs.io/en/latest/src/introduction.html for documentation). This ensures that the encryption, decryption, signing, and verification operations are performed securely and efficiently, leveraging the robustness and optimizations provided by the libraries.

How It Works!
---
> Note that the purpose of this program is for educational purposes only. It is intended to demonstrate the principles of secure communication and the usage of cryptographic algorithms. While the program implements cryptographic techniques, it may not offer the same level of security as professionally audited and maintained cryptographic libraries or systems.

1. Clone the repository  
``` 
git clone https://github.com/gebmecod/RSA-encryption.git 
```
2. cd to project's directory
``` 
cd RSA-encryption
```
3. Run the program
```
python main.py
```
4. Generating Key Pairs  
    - Input `y` if you don't have an existing key pair else `n`.  
    - Input encryption-decryption key pair name.  
    - Input signing-verification key pair name.
    - Created key pairs!
> Public keys are saved with .pub extension e.g. encryption.pub, while private keys are saved without file extension e.g. encryption
5. Creating the message  
    - Input `y` if you don't have an existing message file else `n`.  
    - Enter your message  
    - Enter message filename (excluding the file extension e.g. test which will be automatically saved as test.txt)    
    - Created message file!  
> Note: Any message created outside of this program don't have a check for 140 char limit.

6. Encrypting and Signing the message  
    - Specify the message filename (without .txt)  
    - Specify the encyrption public key (e.g. encryption.pub)  
    - Specify the signing private key (e.g. signing)  
    - Successfully encrypted the message  
    - Successfully signed the encrypted message  
    - Saved the encrypted message to ciphertext file, and the digital signature to signature.pem file

7. Tampering the Message  
To simulate tampering of the encrypted message, an option will be prompted after encrypting and signing the message.  
    - Input `y` if you want to tamper the encrypted message else `n`.  
    - Enter a random content that will be appended to the encrypted message.

8. Verifying and Decrypting Message  
    - Specify the signing public key (e.g. signing.pub)
    - Specify the encryption private key (e.g. encryption)
    - Returns response for verification
    - Decrypts and prints the message

Program Functions:
--
For encryption and signing of the message see: [encrypt_then_sign.md](https://github.com/gebmecod/RSA-encryption/blob/main/docs/encrypt_then_sign.md)  
For verifying signature and decrypting ciphertext see: [verify_then_decrypt.md](https://github.com/gebmecod/RSA-encryption/blob/main/docs/verify_then_decrypt.md)  

The Importance of Digital Signatures in Asymmetric Key Encryption:
--
Read [here](https://hackmd.io/@gebmecod/rsa-encryption)
