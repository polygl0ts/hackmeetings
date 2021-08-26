# hackmeetings
Repo for hosting challenges and various hacks we produce during our meetings

## 2021-06-08

The challenge today comes from [dex](https://github.com/0ddc0de), and is a reverse engineering challenge called [teammanager](./20210608_teammanager).

The first few steps when faced with a binary like this are usually variants of :

 * run `file` to get basic info about the binary
 * run [`checksec`](https://github.com/slimm609/checksec.sh), which will check the different properties of the executable
 * run `string` to see if we can recover info from the plaintext stored in the binary
 * run the binary
 * `strace` the running process
 * open the binary in ghidra/ida/radare2 and start dissecting

Here is what the team was able to accomplish :

 * reverse teammanager (in Ghidra)
 * find a use-after-free and create a poc in python
 * discuss a strategy for write-primitive
 * maybe having a working setup for heap analysis would be good (e.g., `gef's heap (chunk|chunks|bins|arenas)` commands)

Next time we will :
 * finish the teammanager exploit
 * [cyanpencil](https://github.com/cyanpencil) will bring another heap challenge

## 2021-06-15

Finished an exploit for `teammanger`.
There are two ways of exploiting the `teammanager` challenge:

* type confusion after uaf (we focused on this one)
* manipulate tcache

Some tools/commands we used:

* gdb/gef
  * set follow-fork-mode child
  * `-ex` cmd line flag (only one command per flag)
  * add-symbol-file 
  * `pselected`
  * `xinfo <addr>`
  * `got`
* compile c file using a struct so that we can `print *(struct player_t*) <addr>`
  * the struct must be used _at least once_ in main otherwise ignored by gcc
* pwntools
  * fit({<offset>: b"random bytes"})
  * pause()
  * set debug level from cmdline: `./x.py DEBUG`
  * use `sendlineafter()` to consume all input and clear the input buffer
  * create `ELF` object and set `libc.address`, then refer to `libc.symbols['system']`
  
  
## 2021-08-24

The challenge babyrev comes from [corCTF](https://2021.cor.team/) and is about reverse engineering.

We follow the same steps as in the hackmeeting held the 06-08-2021.
Once the binary is opened in ghidra/ida/radare2 it is pretty easy to grasp the goal of the challenge, the binary expects the flag as input.

Tools we used to reverse the binary :

  * ghidra
  * [man-pages](https://www.kernel.org/doc/man-pages/)
  * python3

The team then tried other ways of getting the flag :
 * use of [angr](https://angr.io/) to solve the challenge with symbolic execution
 * use of [afl++](https://github.com/AFLplusplus/AFLplusplus) to solve the challenge by fuzzing a decompiled version where a crash was added if the flag was correct.
 
 
