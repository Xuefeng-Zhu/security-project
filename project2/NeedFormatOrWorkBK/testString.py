from pymd5 import md5

if __name__=='__main__':
    testString = "ffifdyop"
    h = md5()
    h.update(testString)
    print h.digest()
