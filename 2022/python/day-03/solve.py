#! /usr/bin/python3

import sys
from pathlib import Path
from aoc_io import Input
ORD_LOWER_A = ord('a')
ORD_UPPER_A = ord('A')

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
    io = Input(2022, 3)
    lines = io.get_lines()

  sum = 0
  for line in lines:
    line = line.strip()
    mid_index = len(line) // 2
    common = ''.join(set(line[:mid_index]).intersection(line[mid_index:]))
    char_ord = ord(common[0])
    priority = 0
    if char_ord >= ORD_LOWER_A:
      priority = char_ord - ORD_LOWER_A + 1
    else:
      priority = char_ord - ORD_UPPER_A + 27

    sum += priority
    print(common, priority)

  print(sum)
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
    io = Input(2022, 3)
    lines = io.get_lines()

  sum = 0
  i = 0
  while i < len(lines):
    groups = [lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()]
    common = ''.join(set(groups[0]).intersection(groups[1]))
    common = ''.join(set(common).intersection(groups[2]))
    char_ord = ord(common[0])
    priority = 0
    if char_ord >= ORD_LOWER_A:
      priority = char_ord - ORD_LOWER_A + 1
    else:
      priority = char_ord - ORD_UPPER_A + 27

    sum += priority
    print(common, priority)
    i += 3

  print(sum)
  return 0

if __name__ == "__main__":
  sys.exit(main_2(sys.argv))
