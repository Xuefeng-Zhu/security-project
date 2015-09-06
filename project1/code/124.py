from utils import read_file
from Crypto.Util import number


def fasterExponent(ciphertext, d, n):
    temp = 1
    for i in xrange(0, d):
        temp = (temp * ciphertext) % n
    return temp

if __name__ == '__main__':
    d = int(read_file("../1.2.4_private_key.hex"), 16)
    n = int(read_file("../1.2.4_RSA_modulo.hex"), 16)
    ciphertext = int(read_file("../1.2.4_RSA_ciphertext.hex"), 16)

    decryptedtext = fasterExponent(ciphertext, d, n)
    print hex(decryptedtext), "But is it prime???:", number.isPrime(decryptedtext)