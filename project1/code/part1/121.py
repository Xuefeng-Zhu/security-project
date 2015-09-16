from utils import read_file


def index_key(key):
    result = {" ": " "}
    for i in range(len(key)):
        result[key[i]] = chr(ord("A") + i)
    return result

if __name__ == '__main__':
    key = read_file("../1.2.1_sub_key.txt")
    ciphertext = read_file("../1.2.1_sub_ciphertext.txt")
    key_dict = index_key(key)

    result = [key_dict[i] for i in ciphertext]
    print "".join(result)
