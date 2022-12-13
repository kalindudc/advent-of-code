#! /usr/bin/python3

import sys
from pathlib import Path
from aoc_io import Input

def main(args):
  if len(args) < 2:
    print("No mode given")
    return 1

  lines = []
  if args[1] == "test":
    file = Path(__file__).parent / "./test.txt"
    with open(file) as f:
      lines = f.readlines()
  else:
    io = Input(2022, 6)
    lines = io.get_lines()


  for line in lines:
    line = line.rstrip()
    print(line)
    chars = []
    count = 0
    for c in line:
      if len(chars) == 4:
        print(count)
        break

      for i in range(len(chars)):
        if c == chars[i]:
          chars = chars[i+1:]
          break

      chars.append(c)

      print(chars)
      count += 1

  return 0

def main_2(args):
  if len(args) < 2:
    print("No mode given")
    return 1

  lines = []
  if args[1] == "test":
    file = Path(__file__).parent / "./test.txt"
    with open(file) as f:
      lines = f.readlines()
  else:
    io = Input(2022, 6)
    lines = io.get_lines()

  for line in lines:
    line = line.rstrip()
    print(line)
    chars = []
    count = 0
    for c in line:
      if len(chars) == 14:
        print(count)
        break

      for i in range(len(chars)):
        if c == chars[i]:
          chars = chars[i+1:]
          break

      chars.append(c)

      print(chars)
      count += 1

  return 0

if __name__ == "__main__":
  print ("MAIN 1...")
  main(sys.argv)
  print ("\nMAIN 2...")
  main_2(sys.argv)
