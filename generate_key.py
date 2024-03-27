from Crypto.PublicKey import RSA

class Key():
    def __init__(self, filename) -> None:
        self.key = RSA.generate(2048)
        self.filename = filename

    def public_key(self):
        with open(f'{self.filename}.pub', 'wb') as f:
            f.write(self.key.public_key().export_key())
    
    def private_key(self):
        with open(self.filename, 'wb') as f:
            f.write(self.key.export_key())

