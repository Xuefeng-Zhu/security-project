from Crypto.Cipher import AES
from utils import read_file

if __name__ == '__main__':
    key = read_file('../1.2.2_aes_key.hex').decode('hex')
    iv = read_file('../1.2.2_aes_iv.hex').decode('hex')
    ciphertext = read_file('../1.2.2_aes_ciphertext.hex').decode('hex')

    cipher = AES.new(key, AES.MODE_CBC, iv)
    print cipher.decrypt(ciphertext)
