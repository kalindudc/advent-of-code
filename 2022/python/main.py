#! /usr/bin/env python3

import sys
import importlib
import os

def main(args=None):

  if len(args) == 0:
    print('No arguments given')
    sys.exit(1)

  day = importlib.import_module(args[0] + '.solve')
  print("Part 1")
  day.main(args)

  print("\nPart 2")
  day.main_2(args)

def help():
  print('''
  Usage: ./main.py <day> [test, main]

  Example: ./main.py day-01 test
  ''')

if __name__ == '__main__':
  path = os.path.abspath("../../.secrets")
  sys.path.insert(1, path)
  path = os.path.abspath("../../python")
  sys.path.insert(1, path)
  path = os.path.abspath("../../python/utils")
  sys.path.insert(1, path)

  if len(sys.argv) == 1 or sys.argv[1] == 'help' or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    help()
    sys.exit(0)

  main(sys.argv[1:])
