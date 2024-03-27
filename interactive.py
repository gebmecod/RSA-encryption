from generate_key import Key
import rsa_oeap

class Interactive():

    def __init__(self):
        pass

    def generate_key(self):
        is_generate = input('Do you want to generate key pair? [y/n]: ')

        if is_generate == 'y':
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
            print("Done!")
        else:
            pass

    def create_message(self):
        is_message = input("Create a message file? [y/n]: ")

        if is_message == 'y':

            message = input("Enter your message: ")
            filename = input("Enter message's filename: ")
            with open(f'{filename}.txt', 'w') as f:
                f.write(message)
                f.close()

    def encrypt_then_sign(self):
        try:
            file = open(input("Enter message's filename/path: "), 'r')
            message = file.read().encode()
            print(message)
            encryption_key = input("Specify an encryption public key: ")
            signing_key = input("Specify a signing private key: ")
            ciphertext = rsa_oeap.encrypt_message(message, encryption_key)
            signature = rsa_oeap.sign_ciphertext(ciphertext, signing_key)

            print(ciphertext,'\n',signature)

            with open('ciphertext', 'wb') as f:
                f.write(ciphertext)
                f.close()

            with open('signature.pem', 'wb') as f:
                f.write(signature)
                f.close()


        except(FileNotFoundError):
            print(f"File doesn't exist!")




   