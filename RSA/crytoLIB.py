import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
#https://stackoverflow.com/questions/30056762/rsa-encryption-and-decryption-in-python




def RSA():
    random_generator = Random.new().read
    key = Crypto.PublicKey.RSA.generate(1024, random_generator)  # generate public and private keys

    publickey = key.publickey  # pub key export for exchange

    encrypted = publickey.encrypt('encrypt this message', 32)
    # message to encrypt is in the above line 'encrypt this message'

    print
    'encrypted message:', encrypted  # ciphertext

    f = open('encryption.txt', 'w')
    f.write(str(encrypted))  # write ciphertext to file
    f.close()

    # decrypted code below

    f = open('encryption.txt', 'r')
    message = f.read()

    decrypted = key.decrypt(message)

    print
    'decrypted', decrypted

    f = open('encryption.txt', 'w')
    f.write(str(message))
    f.write(str(decrypted))
    f.close()



if __name__ == '__main__':
    RSA()
