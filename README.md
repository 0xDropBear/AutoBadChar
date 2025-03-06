# AutoBadChar

## Introduction
I made this tool after finding it painful to quickly identify Bad Characters in exploit development. 

This tool in its current version (v0.1.0) only works with Proof of Concepts (PoC) written with Python and by reading memory from target application using WinDbg.

Future versions may include PoC's written in other languages and work with other Debuggers.

The code is pretty untested but does work with some messing around the WinDbg command.

## Usuage
This program works with PoC developed in Python and utilising WinDbg for debugging. 

`python AutoBadChar.py`

After copying the Output into you PoC run with WinDbg attached to the target. 

Then in WinDbg run `db <memory location of characters> L100` and copy the output. 

You may need to adjust the `L100` to get stack alignment correct for copying

## Visual Demo
![alt text](ScreenGrabs\ScreenGrab1.png)

Copy the badchars string into you Python PoC and then attach WinDbg to your target application. Once running, send your exploit to the machine. Once landed run the command `db <memory location of characters> L100` and copy the output.

![alt text](ScreenGrabs\ScreenGrab2.png)

Copy this output into the tool and press `ENTER`. The tool will then return either a new badchar string to use:

![alt text](ScreenGrabs\ScreenGrab3.png)

Or, it will complete the check and present you with all the Bad Characters found ready for copying into your POC for reference:

![alt text](ScreenGrabs\ScreenGrab4.png)

At any time you can enter `END` to quit the tool gracefully.