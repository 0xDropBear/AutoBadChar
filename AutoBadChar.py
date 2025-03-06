#!/usr/bin/python

import sys
import math

length = 256
charArray = []
badChars = []

def buildCharArray():
    for i in range(length):
        charArray.append("{:02x}".format(i))

def inputParser():
    inputArray = []
    lines = []
    print("\n\n[+] Enter \'db <memory location of characters> L100\' into WinDbg and copy output here or type \"END\" to Quit:")
    while True:
        line = input()
        if line == "END":
            quit()
        elif not line:
            break
        lines.append(line)
    for x in lines:
        doubleWhiteSpace = x.split('  ')
        doubleWhiteSpace.pop(0)
        doubleWhiteSpace.pop(1)
        temp = doubleWhiteSpace[0].split()
        for i in temp:
            if len(i) > 6:
                temp.remove(i)
            elif len(i) != 2:
                splitter = i.split("-")
                inputArray.append(splitter[0])
                inputArray.append(splitter[1])
            else:
                inputArray.append(i)
    comparator(inputArray)

def comparator(input):
    count = 0
    for i in charArray:
        if input[count] != i:
            print("[+] Bad Character Found: " + i)
            badChars.append(i)
            charArray.remove(i)
            print("[+] New Character Array for testing")
            printBadChars()
        else: 
            count = count + 1
    print("[+] Found all Bad Characters!")
    badCharOutput = ' ,'.join(badChars)
    print("[+] #Bad Characters: " + badCharOutput)
    quit()

def printBadChars():
    linebreak = 16
    rows = int(math.ceil(float(length) / linebreak))
    count = 0
    sys.stdout.write("badchars = (\n")
    for row in range(1, rows + 1):
            sys.stdout.write(' b"')
            for char in range(1, linebreak + 1):
                if count == length:
                    break
                value = "{:02x}".format(count)
                if value not in badChars:
                    sys.stdout.write("\\" + "x" + value)
                count += 1
                if count % linebreak and count != length:
                    sys.stdout.write("")
            if count == length:
                sys.stdout.write('"\n')
                sys.stdout.write(')')
                break
            sys.stdout.write('"')
            sys.stdout.write("\n")
    inputParser() 

if __name__ == "__main__":
    buildCharArray()
    print("[+] Welcome to AutoBadChar...")
    print("[!] This program works with PoC developed in Python and utilising WinDbg for debugging")
    print("[!] After copying the Output into you PoC run with WinDbg attached to the target")
    print("[!] Then in WinDbg run \'db <memory location of characters> L100\' and copy the output ")
    print("[!] You may need to adjust the \'L100\' to get stack alignment correct for copying")
    print("[+] Generating Default BadChar Byte Array")
    
    printBadChars()   