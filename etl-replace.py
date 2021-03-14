#!python

import sys
import os

fin = open("data.txt","rt")
fout = open("out.txt","wt")

for line in fin:
    fout.write(line.replace('pyton','python'))

fin.close()
fout.close()
