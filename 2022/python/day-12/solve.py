from utils import Grid
from pathlib import Path
from aoc_io import Input

STARTING_SYMBOL = "S"
ENDING_SYMBOL = "E"

def can_visit(grid, current, next):
  current_tile = grid.get(current[0], current[1])
  next_tile = grid.get(next[0], next[1])

  current_value = ord(current_tile)
  next_value = ord(next_tile)

  if current_tile == STARTING_SYMBOL:
    current_value = ord('a')

  if next_tile == ENDING_SYMBOL:
    next_value = ord('z')

  return next_value - current_value <= 1

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
    io = Input(2022, 12)
    lines = io.get_lines()

  if len(lines) == 0:
    print("No input given")
    return 1

  grid = Grid(len(lines), len(lines[0]) - 1)
  grid.parse_map(lines)

  start = grid.find_symbol(STARTING_SYMBOL)
  end = grid.find_symbol(ENDING_SYMBOL)

  print(grid)
  print("Start: ", start)
  print("End: ", end)

  shortest_path = grid.find_shortest_path(start, end, can_visit=can_visit)
  print("Shortest path length: ", len(shortest_path) - 1)
  print("Shortest path: ", shortest_path)

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
    io = Input(2022, 12)
    lines = io.get_lines()

  if len(lines) == 0:
    print("No input given")
    return 1

  grid = Grid(len(lines), len(lines[0]) - 1)
  grid.parse_map(lines)

  start = grid.find_symbol(STARTING_SYMBOL)
  end = grid.find_symbol(ENDING_SYMBOL)
  other_starts = grid.find_all_symbols('a')

  print(grid)
  print("Start: ", start)
  print("End: ", end)

  shortest_path = grid.find_shortest_path(start, end, can_visit=can_visit)
  for s in other_starts:
    _shortest_path = grid.find_shortest_path(s, end, can_visit=can_visit)
    if len(_shortest_path) > 0 and len(_shortest_path) < len(shortest_path):
      shortest_path = _shortest_path

  print("Shortest path length: ", len(shortest_path) - 1)
