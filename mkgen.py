#!/usr/bin/python3

'''
C\C++ Makefile generator
writes all dependences for every .c .cpp .cxx .h .hpp files in the directory
usage: makegen $dirname $makefilename
or: makegen $makefilename (for use current directory)
or: makegen
'''


import os
import sys


def iscppfile(name):
    l = name.split('.')
    l[-1].lower()
    ext = ['c', 'cpp', 'cxx', 'h', 'hpp']

    for e in ext:
        if e == l[-1]:
            return True
    return False


def createdependences(f):
    print("File:", f.name, "depends from:", end=' ' )
    dep = []

    for line in f:
        s = line
        s = s.strip()

        if s.startswith("#include"):
            l = s[8:]
            l = l.strip()
            l = l.strip('\"')
            if l[0] != '<':
                dep.append(l)
                print(l, end=' ')
    print()
    return dep


if __name__ == "__main__":
    dirname = '.'
    outfilename = 'Makefile'

    if len(sys.argv) == 2:
        dirname = sys.argv[1]

    if len(sys.argv) >= 3:
        dirname = sys.argv[1]
        outfilename = sys.argv[2]

    try:
        files = [open(name, 'r') for name in os.listdir(dirname) if iscppfile(name)]
        makefile = open(outfilename, 'w')

        for f in files:
            d = createdependences(f)
            makefile.write((f.name + ':') + ' ' + ' '.join(d) + '\n')

        makefile.close()
        for f in files:
            f.close()

    except Exception as a:
        print("Error", a)
        exit(1)




