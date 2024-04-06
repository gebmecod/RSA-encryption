from interactive import Interactive

def main():
    

    interactive = Interactive()
    interactive.generate_key()
    interactive.create_message()
    interactive.encrypt_then_sign()
    tamper = input('Do you want to tamper the encrypted message?[y/n]: ')
    if tamper == 'y':
        interactive.tamper_encrypted_message()
    interactive.verify_then_decrypt()

        
        
        



if __name__ == '__main__':
    main()