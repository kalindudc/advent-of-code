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
    io = Input(2022, 1)
    lines = io.get_lines()

  count = [0, 0, 0]
  current = 0
  for line in lines:
    line = line.strip()
    if (len(line) == 0):
      if current > count[0]:
        count = [current, count[0], count[1]]
      elif current > count[1]:
        count = [count[0], current, count[1]]
      elif current > count[2]:
        count = [count[0], count[1], current]
      current = 0
    else:
      current += int(line)

  print(sum(count))
  return 0

if __name__ == "__main__":
  sys.exit(main(sys.argv))
