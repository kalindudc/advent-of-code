#! /usr/bin/python3

import sys
from pathlib import Path
from aoc_io import Input
def count_dirs(dirs, sizes):

  dir_size = 0
  for dirname in dirs.keys():
    size = 0
    dir = dirs[dirname]
    for file in dir["files"]:
      size += int(file[0])

    size += count_dirs(dir["dirs"], sizes)

    sizes.append(size)
    dir_size += size

  return dir_size

def list_dir(dir, lines, i):
  while i < len(lines):
    line = lines[i].rstrip()
    if line.startswith("$"):
      break

    if line.startswith("dir"):
      dirname = line[4:]
      if not dirname in dir["dirs"].keys():
        dir["dirs"][dirname] = {
          "files": [],
          "dirs": {}
        }
    else:
      dir["files"].append(line.split(" "))
    i = i + 1

  return i - 1

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
    io = Input(2022, 7)
    lines = io.get_lines()

  parent_dir = {}
  current_dir = {}
  dirs = {
    "files": [],
    "dirs": {}
  }

  i = 0
  stack = []
  while i < len(lines):
    line = lines[i].rstrip()
    if line.startswith("$"):
      # this is a command
      command = line[2:]
      if command.startswith("cd"):
        if command == "cd ..":
          stack.pop()
        else:
          stack.append(command[3:])

        current_dir = dirs
        for dir in stack:
          if dir not in current_dir["dirs"].keys():
            current_dir["dirs"][dir] = {
              "files": [],
              "dirs": {}
            }
          current_dir = current_dir["dirs"][dir]
      elif command.startswith("ls"):
        i = i + 1
        i = list_dir(current_dir, lines, i)
    i = i + 1

  print(dirs)
  print("\n")

  sizes = []
  count_dirs(dirs["dirs"], sizes)

  valid_sizes = []
  for size in sizes:
    if size <= 100000:
      valid_sizes.append(size)

  print(sizes)
  print(valid_sizes)
  print(sum(valid_sizes))
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
    io = Input(2022, 7)
    lines = io.get_lines()

  parent_dir = {}
  current_dir = {}
  dirs = {
    "files": [],
    "dirs": {}
  }

  i = 0
  stack = []
  while i < len(lines):
    line = lines[i].rstrip()
    if line.startswith("$"):
      # this is a command
      command = line[2:]
      if command.startswith("cd"):
        if command == "cd ..":
          stack.pop()
        else:
          stack.append(command[3:])

        current_dir = dirs
        for dir in stack:
          if dir not in current_dir["dirs"].keys():
            current_dir["dirs"][dir] = {
              "files": [],
              "dirs": {}
            }
          current_dir = current_dir["dirs"][dir]
      elif command.startswith("ls"):
        i = i + 1
        i = list_dir(current_dir, lines, i)
    i = i + 1

  print(dirs)
  print("\n")

  sizes = []
  root_size = count_dirs(dirs["dirs"], sizes)

  unused = 70000000 - root_size
  needed = 30000000 - unused

  valid_sizes = []
  for size in sizes:
    if size >= needed:
      valid_sizes.append(size)

  print(sizes)
  print(valid_sizes)
  print(needed)
  print(min(valid_sizes))
  return 0

if __name__ == "__main__":
  print ("MAIN 1...")
  main(sys.argv)
  print ("\nMAIN 2...")
  main_2(sys.argv)
