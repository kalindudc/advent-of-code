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
    io = Input(2022, 10)
    lines = io.get_lines()

  cycle = 0
  x = 1
  signal = []

  i = 0
  delay = False

  while i < len(lines):
    line = lines[i].strip()
    if len(line) == 0:
      continue

    cycle += 1
    print("Cycle: %d, x: %d" % (cycle, x))
    if ((cycle - 20) % 40 == 0):
      print("add to signal")
      signal.append(x * cycle)

    command = line.split(' ')
    if command[0] == "addx":
      if delay:
        print("Command: %s, %s" % (command[0], command[1]))
        x += int(command[1])
        delay = False
      else:
        delay = True

    if not delay:
      i += 1

  print (signal)
  print (sum(signal))


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
    io = Input(2022, 10)
    lines = io.get_lines()

  cycle = 0
  x = 1
  sprite_pos = 1

  i = 0
  delay = False

  while i < len(lines):
    line = lines[i].strip()
    if len(line) == 0:
      continue

    command = line.split(' ')
    cycle += 1

    col = cycle % 40
    if (col == 0):
      col = 40

    if (col >= x and col <= (x + 2)):
      print("#", end="")
    else:
      print(".", end="")

    if (cycle % 40 == 0):
      print("")

    if command[0] == "addx":
      if delay:
        x += int(command[1])
        delay = False
      else:
        delay = True

    if not delay:
      i += 1
  return 0

if __name__ == "__main__":
  print ("MAIN 1...")
  main(sys.argv)
  print ("\nMAIN 2...")
  main_2(sys.argv)
