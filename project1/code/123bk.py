from Crypto.Cipher import AES
from utils import read_file

if __name__ == '__main__':
    ciphertext = read_file('../1.2.3_aes_weak_ciphertext.hex').decode('hex')
    iv = "0" * 32
    iv = iv.decode('hex')
    for i in range(0, 32):
        last_byte = str(hex(i)[2:])
        key = "0" * (64-len(last_byte)) + last_byte

        cipher = AES.new(key.decode('hex'), AES.MODE_CBC, iv)
        # Second to last decryption appears to be correct one
        print cipher.decrypt(ciphertext), key, "\n"
