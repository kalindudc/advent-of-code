#! /usr/bin/python3

import sys
from pathlib import Path
from aoc_io import Input

ORD_LOWER_A = ord('a')
ORD_UPPER_A = ord('A')

def is_contained(elf_1, elf_2):
  if int(elf_1[0]) <= int(elf_2[0]) and int(elf_1[1]) >= int(elf_2[1]):
    return True

  if int(elf_2[0]) <= int(elf_1[0]) and int(elf_2[1]) >= int(elf_1[1]):
    return True

  return False

def get_overlap(elf_1, elf_2):
  overlap = set()
  for i in range(int(elf_1[0]), int(elf_1[1]) + 1):
    if int(elf_2[0]) <= i and int(elf_2[1]) >= i:
      overlap.add(i)

  for i in range(int(elf_2[0]), int(elf_2[1]) + 1):
    if int(elf_1[0]) <= i and int(elf_1[1]) >= i:
      overlap.add(i)

  return overlap

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
    io = Input(2022, 4)
    lines = io.get_lines()

  count = 0
  for line in lines:
    line = line.strip()
    groups = line.split(',')
    elf_1 = groups[0].split('-')
    elf_2 = groups[1].split('-')

    if is_contained(elf_1, elf_2):
      count += 1

  print(count)
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
    io = Input(2022, 4)
    lines = io.get_lines()

  count = 0
  unique = set()
  for line in lines:
    line = line.strip()
    groups = line.split(',')
    elf_1 = groups[0].split('-')
    elf_2 = groups[1].split('-')

    numbers = get_overlap(elf_1, elf_2)
    if len(get_overlap(elf_1, elf_2)) > 0:
      count += 1
      unique = unique.union(numbers)

  print(count)
  print(unique)
  print(len(unique))
  return 0

def does_not_overlap(elf_1, elf_2):
  if int(elf_1[1]) < int(elf_2[0]) or int(elf_2[1]) < int(elf_1[0]):
    return True

  return False

def main_3(args):
  if len(args) < 2:
    print("No mode given")
    return 1

  lines = []
  if args[1] == "test":
    file = Path(__file__).parent / "./test.txt"
    with open(file) as f:
      lines = f.readlines()
  else:
    io = Input(2022, 4)
    lines = io.get_lines()

  count = 0
  for line in lines:
    line = line.strip()
    groups = line.split(',')
    elf_1 = groups[0].split('-')
    elf_2 = groups[1].split('-')

    if not does_not_overlap(elf_1, elf_2):
      count += 1

    print(count)
    print(len(lines) - count)
  return 0

if __name__ == "__main__":
  sys.exit(main_3(sys.argv))
