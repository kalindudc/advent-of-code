#! /usr/bin/python3

import sys
from pathlib import Path
from aoc_io import Input
def set_head_and_tail(map, h_pos, t_pos):
  map[4][0] = 's'
  map[t_pos[0]][t_pos[1]] = 'T'
  map[h_pos[0]][h_pos[1]] = 'H'
  return map

def print_map(h_pos, t_pos):

  map = build_puzzle_map()
  map = set_head_and_tail(map, h_pos, t_pos)

  print("\nPrinting map...")
  print("  | 0 1 2 3 4 5")
  print("----------------")
  for i in range(0, len(map)):
    print(i, end=' | ')
    for col in map[i]:
      print(col, end=' ')
    print("")

def build_puzzle_map():
  map = [['.' for i in range(0,6)] for j in range(0, 5)]
  map[4][0] = 's'
  return map

def get_distance(h_pos, t_pos):
  return abs(h_pos[0] - t_pos[0]) + abs(h_pos[1] - t_pos[1])

def should_tail_move(h_pos, t_pos):
  if h_pos == t_pos:
    return False

  should_move = True
  for x in range(t_pos[0] - 1, t_pos[0] + 2):
    for y in range(t_pos[1] - 1, t_pos[1] + 2):
      if (x, y) == h_pos:
        should_move = False

  return should_move

def get_next_tail_pos(h_pos, t_pos):
  if not should_tail_move(h_pos, t_pos):
    return t_pos

  if get_distance(h_pos, t_pos) > 2:
    # move down
    if h_pos[0] > t_pos[0]:
      # move right
      if h_pos[1] > t_pos[1]:
        return (t_pos[0] + 1, t_pos[1] + 1)
      else:
        return (t_pos[0] + 1, t_pos[1] - 1)
    else:
      # move left
      if h_pos[1] > t_pos[1]:
        return (t_pos[0] - 1, t_pos[1] + 1)
      else:
        return (t_pos[0] - 1, t_pos[1] - 1)
  else:
    if h_pos[0] == t_pos[0]:
      if h_pos[1] > t_pos[1]:
        return (t_pos[0], t_pos[1] + 1)
      else:
        return (t_pos[0], t_pos[1] - 1)
    else:
      if h_pos[0] > t_pos[0]:
        return (t_pos[0] + 1, t_pos[1])
      else:
        return (t_pos[0] - 1, t_pos[1])

def get_next_head_pos(h_pos, move):
  if move == 'R':
    return (h_pos[0], h_pos[1] + 1)
  elif move == 'L':
    return (h_pos[0], h_pos[1] - 1)
  elif move == 'U':
    return (h_pos[0] - 1, h_pos[1])
  elif move == 'D':
    return (h_pos[0] + 1, h_pos[1])

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
    io = Input(2022, 9)
    lines = io.get_lines()

  h_pos = (4, 0)
  t_pos = (4, 0)
  #print_map(h_pos, t_pos)

  tail_moves = set()
  for line in lines:
    line = line.strip()
    if len(line) == 0:
      continue

    split = line.split(' ')
    move = split[0]
    steps = int(split[1])
    for i in range(0, steps):
      h_pos = get_next_head_pos(h_pos, move)
      t_pos = get_next_tail_pos(h_pos, t_pos)
      tail_moves.add(t_pos)
      #print_map(h_pos, t_pos)

  print(len(tail_moves))

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
    io = Input(2022, 9)
    lines = io.get_lines()

  knots = [(0,0) for i in range(0, 10)]

  tail_moves = [set() for i in range(0, 10)]
  for line in lines:
    line = line.strip()
    if len(line) == 0:
      continue

    split = line.split(' ')
    move = split[0]
    steps = int(split[1])
    for i in range(0, steps):
      h_pos = get_next_head_pos(knots[0], move)
      knots[0] = h_pos

      for i in range(1, 10):
        t_pos = get_next_tail_pos(knots[i - 1], knots[i])
        knots[i] = t_pos
        tail_moves[i].add(t_pos)
  print(len(tail_moves[9]))
  return 0

if __name__ == "__main__":
  print ("MAIN 1...")
  main(sys.argv)
  print ("\nMAIN 2...")
  main_2(sys.argv)
