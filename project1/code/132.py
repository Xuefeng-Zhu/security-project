from utils import read_file
import string
import random


def wha(in_str):
    bin_array = bytearray(in_str)

    hexdata1 = int('CC', 16)
    hexdata2 = int('33', 16)
    hexdata3 = int('AA', 16)
    hexdata4 = int('55', 16)

    mask = int('3FFFFFFF', 16)
    outHash = 0

    for byte in bin_array:
        intermediate_value = ((byte ^ hexdata1) << 24) | (
            (byte ^ hexdata2) << 16) | ((byte ^ hexdata3) << 8) | (byte ^ hexdata4)
        outHash = (outHash & mask) + (intermediate_value & mask)
    return hex(outHash)

if __name__ == '__main__':
    # Test
    # assert wha("Hello world!") == "0x50b027cf"
    # assert wha("I am Groot.") == "0x57293cbb"

    jeopardyQ = read_file("../1.3.2_input_string.txt")
    jeopardyHash = wha(jeopardyQ)

    print jeopardyHash

    testHash = ""
    while (testHash != jeopardyHash):
        test = " PRESIDENTS NATIONAL HISTORIC SITE IN WEST BRANCH IOWA HAS A QUAKER MEETINGHOUSE ON THE GROUNDS"
        for i in range(0, 4):
            test = random.choice(string.ascii_uppercase) + test
        testHash = wha(test)

    print test, testHash
