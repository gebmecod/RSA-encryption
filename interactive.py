from generate_key import Key
import rsa_oeap
from sys import platform
import os

class Interactive():

    def __init__(self):
        pass

    def clear_screen(self):
        if platform == "win32":
            os.system('cls')
        else:
            os.system('clear')

    def generate_key(self):
        is_generate = input('Do you want to generate key pair? [y/n]: ')

        if is_generate == 'y':
            self.clear_screen()
            encryption_key_filename = input('Enter filename for encryption key pair: ')
            print("Generating encryption key pair...")
            encryption_key = Key(encryption_key_filename)
            encryption_key.public_key()
            encryption_key.private_key()
            print("Done!")
            signing_key_filename = input('Enter filename for signing key pair: ')
            print("Generating signing key pair...")
            signing_key  = Key(signing_key_filename)
            signing_key.public_key()
            signing_key.private_key()
            print("Successfully created key pairs!")
        else:
            pass

    def create_message(self):
        self.clear_screen()
        is_message = input("Create a message file? [y/n]: ")

        if is_message == 'y':
            self.clear_screen()
            message = input("Enter your message: ")
            filename = input("Enter message's filename: ")
            with open(f'{filename}.txt', 'w') as f:
                f.write(message)
                f.close()
            print(f"Successully created {filename}.txt file!")

    def encrypt_then_sign(self):
        try:
            self.clear_screen()
            print("Encrypting and Signing the Message...\n")
            file = open(input("Enter message's filename/path: "), 'r')
            message = file.read().encode()
            encryption_key = input("Specify the encryption public key: ")
            signing_key = input("Specify the signing private key: ")
            ciphertext = rsa_oeap.encrypt_message(message, encryption_key)
            print("Successfully encrypted message\n")
            signature = rsa_oeap.sign_ciphertext(ciphertext, signing_key)
            print("Successfully signed encrypted message! \n")

            with open('ciphertext', 'wb') as f:
                f.write(ciphertext)
            with open('signature.pem', 'wb') as f:
                f.write(signature)


        except(FileNotFoundError):
            print(f"File doesn't exist!")

    def tamper_encrypted_message(self):
        random_content = input("Enter random characters: ")
        ciphertext = open('ciphertext', 'wb')
        ciphertext.write(random_content.encode())
    
    def verify_then_decrypt(self):
        try:
            self.clear_screen()
            print("Verifying and Decrypting the Message")
            ciphertext = open('ciphertext', 'rb').read()
            signature = open('signature', 'rb').read()
            signing_public_key = input("Specify signing public key: ")
            decryption_private_key = input("Specify decryption key: ")
            self.clear_screen()
            decrypted_message = rsa_oeap.verify_message(signature, ciphertext, signing_public_key, decryption_private_key)
            print(f"Your message is {decrypted_message}")
            


        except(FileNotFoundError):
            print("File doesn't exist!")

   