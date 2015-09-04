def wha(inStr):
    binArray = bytearray(inStr)
    
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
    print (wha("Hello world!"))
    print (wha("I am Groot."))
