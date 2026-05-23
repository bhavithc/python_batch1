# Python interpretor 

C program -> Pre processing (Copy paste) -> Proper (Syntax) -> assembler (ASM) -> Linker ->


## Cpython uses interpretor from C
Python code -> ByteCode -> Interpreted instruction-by-instruction

```bash
python3 -m compileall hello.py
cd __pycache__
# hello.cpython-312.pyc
# hello -> name of the module 
# cpython -> Interpretor 
# 312 -> version of python
# pyc -> python byte code 
python3 hello.cpython-312.pyc

# To enable verbose 
python3 -v -m compileall hello.py

file hello.cpython-312.pyc
hello.cpython-312.pyc: Byte-compiled Python module for CPython 3.12 or newer, timestamp-based, .py timestamp: Fri May 22 17:39:46 2026 UTC, .py size: 91 bytes
```

## Jython uses JVM 
```bash
jython hello.py

jython -m compileall hello.py
Compiling hello.py ...

file  hello\$py.class
hello$py.class: compiled Java class data, version 50.0 (Java 1.6)

java -cp /usr/share/java/jython.jar:. hello\$py
```

## Pypy3 intepretor (alternative to python interpretor)
```bash

# try to run the pvm bytecode using pypy3 
pypy3 hello.cpython-312.pyc
RuntimeError: Bad magic number in .pyc file

pypy3 -m compileall hello.py
file hello.pypy39.pyc
hello.pypy39.pyc: Byte-compiled Python module for PyPy3.9, timestamp-based, .py timestamp: Fri May 22 17:39:46 2026 UTC, .py size: 91 bytes

# python code 
# Byte code 
# JIT compiler observes hot code
# Converts hot paths into machine code
```
> Note: So PyPy can become much faster for long-running programs.
> 

```bash
# cpython interpretor (PVM) - implemented using C 
sudo apt install python3 
sudo apt install jython # java interpretor (JVM)
sudo apt install pypy3 # 
```


```python
def hello():
    print("Hello")

import dis
dis.dis(hello)
```


# Link 
https://godbolt.org/
https://markdownlivepreview.com/
https://en.wikipedia.org/wiki/Guido_van_Rossum
https://en.wikipedia.org/wiki/ABC_(programming_language)
https://homepages.cwi.nl/~steven/abc/types.html
https://www.python.org/downloads/macos/
https://www.markdownguide.org/cheat-sheet/
https://github.com/torvalds/linux
https://github.com/bhavithc/python_batch1

# Git commands 

- `git clone git@github.com:bhavithc/python_batch1.git` -> To clone 
- `git remote -v` -> To see from where I cloned ?
- `git add Day1` -> Day1 folder is added to staged area
- `git status` -> You can see the status of the git any time
- `git log` -> To check the commit messages 
- `git log -1` -> To check only 1 message, if you give 2 then it shows last two commit messages