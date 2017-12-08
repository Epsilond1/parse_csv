#!/usr/bin/env python
# encoding: utf-8

import sys

from parser import Parser
from writer import Writer


def print_help():
    print('d [filename] - разбор csv-файла')
    print('h - справка')


if __name__ == "__main__":
    try:
        command = sys.argv[1]
        if command == 'h':
            print_help()
        elif command == 'd':
            try:
                parser = Parser(sys.argv[2])
                result = parser.prepare_output(parser.read_file())
                writer = Writer(result)
                writer.record()
            except IndexError:
                print('Expected file name')
        else:
            print('Unknown command!')
            print_help()
    except IndexError:
        print('Invalid argument!')
        print_help()
