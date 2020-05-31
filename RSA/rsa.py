import random
####https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html

def chooseE(totient):
    """
    Chooses a random number, 1 < e < totient, and checks whether or not it is
    coprime with the totient, that is, gcd(e, totient) = 1
    """
    while (True):
        e = random.randrange(2, totient)

        if (gcd(e, totient) == 1):
            return e

def xgcd(a, b):
    """
    Performs the extended Euclidean algorithm
    Returns the gcd, coefficient of a, and coefficient of b
    """
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y

def gcd(a, b):
    """
    Performs the Euclidean algorithm and returns the gcd of a and b
    """
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def chooseKeys():
    """
    Selects two random prime numbers from a list of prime numbers which has
    values that go up to 100k. It creates a text file and stores the two
    numbers there where they can be used later. Using the prime numbers,
    it also computes and stores the public and private keys in two separate
    files.
    """

    # choose two random numbers within the range of lines where
    # the prime numbers are not too small and not too big
    rand1 = random.randint(100, 300)
    rand2 = random.randint(100, 300)

    # store the txt file of prime numbers in a python list
    fo = open('primes-to-100k.txt', 'r')
    lines = fo.read().splitlines()
    fo.close()

    # store our prime numbers in these variables
    prime1 = int(lines[rand1])
    prime2 = int(lines[rand2])

    # compute n, totient, e
    n = prime1 * prime2
    totient = (prime1 - 1) * (prime2 - 1)
    e = chooseE(totient)

    # compute d, 1 < d < totient such that ed = 1 (mod totient)
    # e and d are inverses (mod totient)
    gcd, x, y = xgcd(e, totient)

    # make sure d is positive
    if (x < 0):
        d = x + totient
    else:
        d = x

    # write the public keys n and e to a file
    f_public = open('public_keys.txt', 'w')
    f_public.write(str(n) + '\n')
    f_public.write(str(e) + '\n')
    f_public.close()

    f_private = open('private_keys.txt', 'w')
    f_private.write(str(n) + '\n')
    f_private.write(str(d) + '\n')
    f_private.close()




def leerTexto():
    text = input("Introduce Texto")
    text = "tusa.txt"
    f = open(text, "r")

    #for x in f:
    #    print(x)
    return  f

def rsa():
    print("RSA")
    choose_again = input('Do you want to generate new public and private keys? (y or n) ')
    if (choose_again == 'y'):
        chooseKeys()
    instruction = input('Would you like to encrypt or decrypt? (Enter e or d): ')



if __name__ == '__main__':
    rsa()
    f = leerTexto()
    for x in f:
        print(x)
