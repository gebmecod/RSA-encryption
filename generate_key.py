from Crypto.PublicKey import RSA

class Key():
    def __init__(self) -> None:
        self.key = RSA.generate(2048)

    def public_key(self):
        return self.key.publickey().export_key()
    
    def private_key(self):
        return self.key.export_key()

