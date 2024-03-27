from interactive import Interactive

def main():
    
    while True:
        option = input("Choose an option\n\n(1) Interactive\n(2) Automatic\n: ")

        if option == '1':
            interactive = Interactive()
            interactive.generate_key()
            interactive.create_message()
            interactive.encrypt_then_sign()
            break
        elif option == '2':
            pass
        else:
            print("Invalid option. Please try again!\n")
        
        
        



if __name__ == '__main__':
    main()