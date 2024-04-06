# RSA-encryption
CMSC 134 - Machine Problem 2: RSA Encryption

An implementation for encrypting and decrypting message using RSA-OAEP with authenticity. The goal is to provide secure communication between parties ensuring confidentiality, integrity, and authenticity of the exchanged messages.

Program Features:  
---
1. **Key Generation**  
            - The program can generate separate key pairs for encryption and signing. This separation ensures that different keys are used for encryption and signing, enhancing security by preventing potential attacks that exploit key reuse vulnerabilities.
2. **Encrypt-then-Sign Scheme**  
            - To achieve authenticated encryption, the program follows the encrypt-then-sign scheme. First, it encrypts the message using RSA-OAEP encryption with the provided key (k) for confidentiality. Then, it signs the encrypted ciphertext using RSA digital signatures with another provided key (k) for authenticity and integrity. This approach ensures that the recipient can verify the authenticity of the message before decryption, mitigating the risk of tampering or impersonation.
3. **Cryptographic Libraries**  
            - Rather than implementing cryptographic algorithms from scratch, the program utilizes established cryptographic libraries of Python PyCrypto and PyCryptodome (see: https://pycryptodome.readthedocs.io/en/latest/src/introduction.html for documentation). This ensures that the encryption, decryption, signing, and verification operations are performed securely and efficiently, leveraging the robustness and optimizations provided by the libraries.