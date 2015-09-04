from Crypto.Cipher import AES
from utils import read_file

if __name__ == '__main__':
    ciphertext = read_file('../1.2.3_aes_weak_ciphertext.hex').decode('hex')

    result = []
    iv = chr(0) * 16
    for i in range(32):
        key = chr(0) * 15 + chr(i)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        print cipher.decrypt(ciphertext)
