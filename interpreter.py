#!/usr/bin/env python
import os
from parser import parser
from lexer import lexer


def main():
    import sys
    begin(sys.argv)

def begin(argv):
    if len(argv) > 1:
        with open(argv[1], 'r') as f:
            source = f.read()
            tokens = lexer.lex(source)
            expression = parser.parse(tokens)
            expression.eval()    
    else:
        print("Please provide a filename.")
        
main()
print("Closing interpreter...")