import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

####https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html



def rsaLibreria():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)  # generate public and private keys

    publickey = key.publickey  # pub key export for exchange

    encrypted = publickey.encrypt('encrypt this message', 32)
    # message to encrypt is in the above line 'encrypt this message'

    print('encrypted message:', encrypted)  # ciphertext
    f = open('encryption.txt', 'w')
    f.write(str(encrypted))  # write ciphertet

    # decrypted code below

    f = open('encryption.txt', 'r')
    message = f.read()

    decrypted = key.decrypt(message)

    print('decrypted', decrypted)

    f = open('encryption.txt', 'w')
    f.write(str(message))
    f.write(str(decrypted))
    f.close()



def rsaLibreria2():
    print("RSA LIBRERIA 2")
    key = RSA.generate(2048)
    f = open("tusa.txt", 'wb')
    f.write(key.exportkey('PEM'))
    f.close()

    f = open('mykey.pem', 'r')
    key = RSA.importKey(f.read())


if __name__ == '__main__':
    rsaLibreria2()