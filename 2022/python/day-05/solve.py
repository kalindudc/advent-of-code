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
    io = Input(2022, 5)
    lines = io.get_lines()

  stacks = []
  moves = []
  for i in range(len(lines)):
    line = lines[i].rstrip()
    # first fill the stacks
    if line == "":
      moves = lines[i+1:]
      break

    index = 0
    stack_count = 0
    while index < len(line):
      _char = line[index]
      if len(stacks) <= stack_count:
        stacks.append([])

      if _char == "[":
        stacks[stack_count].insert(0, line[index+1])

      stack_count += 1
      index += 4

  print(stacks)
  print(moves)

  for move in moves:
    move = move.rstrip()

    # move x from y to z
    move = move.split(" ")
    number_of_moves = int(move[1])
    from_stack = int(move[3]) - 1
    to_stack = int(move[5]) - 1

    print("Move %d from %d to %d" % (number_of_moves, from_stack, to_stack))

    for i in range(number_of_moves):
      if (len(stacks[from_stack]) > 0):
        stacks[to_stack].append(stacks[from_stack].pop())

  res = []
  for stack in stacks:
    res.append(stack[len(stack)-1])

  print("".join(res))
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
    io = Input(2022, 5)
    lines = io.get_lines()

  stacks = []
  moves = []

  for i in range(len(lines)):
    line = lines[i].rstrip()
    # first fill the stacks
    if line == "":
      moves = lines[i+1:]
      break

    index = 0
    stack_count = 0
    while index < len(line):
      _char = line[index]
      if len(stacks) <= stack_count:
        stacks.append([])

      if _char == "[":
        stacks[stack_count].insert(0, line[index+1])

      stack_count += 1
      index += 4

  print(stacks)
  print(moves)

  for move in moves:
    move = move.rstrip()

    # move x from y to z
    move = move.split(" ")
    number_of_moves = int(move[1])
    from_stack = int(move[3]) - 1
    to_stack = int(move[5]) - 1

    print("Move %d from %d to %d" % (number_of_moves, from_stack, to_stack))
    print(stacks[from_stack][:-number_of_moves])
    print(stacks[from_stack][::-1][:number_of_moves])
    if (len(stacks[from_stack]) > 0):
      stacks[to_stack] = stacks[to_stack] + stacks[from_stack][::-1][:number_of_moves][::-1]
      stacks[from_stack] = stacks[from_stack][:-number_of_moves]

    print(stacks)


  res = []
  for stack in stacks:
    res.append(stack[len(stack)-1])

  print("".join(res))
  return 0

if __name__ == "__main__":
  print ("MAIN 1...")
  main(sys.argv)
  print ("\nMAIN 2...")
  main_2(sys.argv)
