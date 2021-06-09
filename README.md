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
