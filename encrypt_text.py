class Encrypt:
    def __init__(self) -> None:
        self.main_text = ""
        self.encrypted_text = ""
    
    def encrypt(self, main_text):
        self.main_text = ""
        for i in main_text:
            self.encrypted_text += chr((ord(i) * 3) + 5)
        return self.encrypted_text
    
    def decrypt(self, decrypted_text):
        self.main_text = ""
        for i in decrypted_text:
            self.main_text += chr((ord(i) - 5) // 3)
        return self.main_text

def command():
    print('\t1.Encrypt text\n\t2.Decrypt text\n\t3.Exit')
    return input('Enter an option:')

def main():

    while True:
        user_input = command()

        match user_input:
            case '1':
                encrypt_text = input('Text: ')
                e = Encrypt()
                print(f'Encrypted text: {e.encrypt(encrypt_text)}')
                print('*' * 30)
            case '2':
                decrypted_text = input('Text: ')
                e = Encrypt()
                print(f'Decrypted text: {e.decrypt(decrypted_text)}')
                print('*' * 30)
            case '3':
                print('buy...')
                break
            case other:
                print('Inavalid...')
                print('*' * 30)


if __name__ == "__main__":
    main()