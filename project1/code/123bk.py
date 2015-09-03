from Crypto.Cipher import AES
from utils import read_file

if __name__ == '__main__':
    ciphertext = read_file('../1.2.3_aes_weak_ciphertext.hex').decode('hex')
    iv = "00000000000000000000000000000000"
    iv = iv.decode('hex')
    for i in range (0,32):
        testKey = str(hex(i)[2:])
        while len(testKey)<64:
            testKey = "0"+testKey
        testKey = testKey.decode('hex')

        cipher = AES.new(testKey, AES.MODE_CBC, iv)
        #Second to last decryption appears to be correct one
        print cipher.decrypt(ciphertext)
            
