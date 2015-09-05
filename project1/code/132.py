from utils import read_file
import string
import random

def wha(inStr):
    binArray = inStr
    
    hexdata1 = int('CC',16)
    hexdata2 = int('33',16)
    hexdata3 = int('AA',16)
    hexdata4 = int('55',16)

    mask = int('3FFFFFFF',16)
    outHash = 0

    for byte in binArray:
        intermediate_value = ((byte^hexdata1)<<24)|((byte^hexdata2)<<16)|((byte^hexdata3)<<8)|(byte^hexdata4)
        outHash = (outHash & mask) + (intermediate_value & mask)
    return hex(outHash)

if __name__=='__main__':
    #print (wha(bytearray("Hello world!")))
    #print (wha(bytearray("I am Groot.")))

    jeopardyQ = read_file("../1.3.2_input_string.txt")
    jeopardyHash = wha(bytearray(jeopardyQ))

    print jeopardyHash

    test = ""
    testHash = wha(bytearray(test))
    while (testHash!=jeopardyHash):
        test = " PRESIDENTS NATIONAL HISTORIC SITE IN WEST BRANCH IOWA HAS A QUAKER MEETINGHOUSE ON THE GROUNDS"
        for i in range (0,4):
            test = random.choice(string.ascii_uppercase) + test
        testHash = wha(bytearray(test))
        

    print test, testHash
        

    
