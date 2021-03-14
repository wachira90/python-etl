#!python
'''
read file for python3
'''
import sys

def main():
    file1 = sys.argv[1]
    f= open(file1,"r", encoding="UTF-8")
    for i in f:
        print(i,end='')

if (__name__== "__main__"):
  main()