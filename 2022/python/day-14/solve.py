from pathlib import Path
from utils import Grid
from aoc_io import Input

ROCKS = "#"
SAND = "o"
SAND_DISPENSER = "+"
AIR = "."
SAND_CORDS = [0, 500]

def paint_rocks(grid, rock_paths, offset_row, offset_col):
  for path in rock_paths:
    for i in range(len(path) - 1):
      start_row = int(path[i][0])
      start_col = int(path[i][1])
      end_row = int(path[i + 1][0])
      end_col = int(path[i + 1][1])
      reverse_row = -1 if start_row > end_row else 1
      reverse_col = -1 if start_col > end_col else 1

      for row in range(start_row, end_row + (1 * reverse_row), reverse_row):
        for col in range(start_col, end_col + (1 * reverse_col), reverse_col):
          grid.set(row - offset_row, col - offset_col, ROCKS)

def create_map(lines):
  raw_rock_paths = [ line.strip().split("->") for line in lines ]
  rock_paths = [[cords.strip().split(",")[::-1] for cords in path] for path in raw_rock_paths]

  all_col_cords = {int(cords[1]) for path in rock_paths for cords in path}
  all_row_cords = {int(cords[0]) for path in rock_paths for cords in path}

  all_col_cords.add(SAND_CORDS[1])
  all_row_cords.add(SAND_CORDS[0])

  min_col = min(all_col_cords)
  max_col = max(all_col_cords)
  min_row = min(all_row_cords)
  max_row = max(all_row_cords)

  offset_row = min_row
  offset_col = min_col - 1

  grid = Grid(max_row + 1, max_col + 1, offset_row=offset_row, offset_col=offset_col)
  grid.set(SAND_CORDS[0] - offset_row, SAND_CORDS[1] - offset_col, SAND_DISPENSER)
  paint_rocks(grid, rock_paths, offset_row, offset_col)

  return grid

def simulate_sand_fall(grid, row, col):
  symbol = grid.get(row, col)

  while symbol == AIR:
    row += 1
    if row >= grid.rows:
      break

    symbol = grid.get(row, col)


  return symbol, row

def get_filled(lines):
  raw_rock_paths = [ line.strip().split("->") for line in lines ]
  rock_paths = [[cords.strip().split(",")[::-1] for cords in path] for path in raw_rock_paths]

  occupied = {}
  for path in rock_paths:
    for i in range(len(path) - 1):
      start_row = int(path[i][0])
      start_col = int(path[i][1])
      end_row = int(path[i + 1][0])
      end_col = int(path[i + 1][1])
      reverse_row = -1 if start_row > end_row else 1
      reverse_col = -1 if start_col > end_col else 1

      for row in range(start_row, end_row + (1 * reverse_row), reverse_row):
        for col in range(start_col, end_col + (1 * reverse_col), reverse_col):
          occupied[(row, col)] = ROCKS

  return occupied

def simulate_sand(grid, sand_row, sand_col):
  number_of_sand = 0
  while True:
    if sand_row >= grid.rows - 1:
      return number_of_sand

    symbol, row = simulate_sand_fall(grid, sand_row+1, sand_col)

    if symbol == ROCKS or symbol == SAND:
      # check left and righ
      left_symbol = None
      right_symbol = None
      if sand_col + 1 < grid.cols:
        right_symbol = grid.get(row, sand_col + 1)
      if sand_col - 1 >= 0:
        left_symbol = grid.get(row, sand_col - 1)

      # try to move left
      if left_symbol == AIR:
        sand_row = row
        sand_col -= 1
      elif right_symbol == AIR:
        sand_row = row
        sand_col += 1
      else:
        if row - 1 <= 0:
          return number_of_sand
        grid.set(row - 1, sand_col, SAND)
        sand_row = SAND_CORDS[0] - grid.offset_row
        sand_col = SAND_CORDS[1] - grid.offset_col
        number_of_sand += 1
    else:
      return number_of_sand


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
    io = Input(2022, 14)
    lines = io.get_lines()

  if len(lines) == 0:
    print("No input given")
    return 1

  # this implementation sucks, part 2 is better
  grid = create_map(lines)
  print(grid)

  number_of_sand = simulate_sand(grid, SAND_CORDS[0] - grid.offset_row, SAND_CORDS[1] - grid.offset_col)

  print("")
  print(grid)
  print(number_of_sand)

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
    io = Input(2022, 14)
    lines = io.get_lines()

  if len(lines) == 0:
    print("No input given")
    return 1

  filled = get_filled(lines)
  max_row = max([row for row, col in filled.keys()])
  rock_layer_row = max_row + 2

  number_of_sand = 0
  sand_row = SAND_CORDS[0]
  sand_col = SAND_CORDS[1]

  while True:
    symbol, row = AIR, sand_row
    while row < rock_layer_row:
      if (row, sand_col) in filled:
        symbol = filled[(row, sand_col)]
        break
      row += 1

    if row == rock_layer_row:
      filled[(row-1, sand_col)] = SAND
      number_of_sand += 1
      sand_row = SAND_CORDS[0]
      sand_col = SAND_CORDS[1]
      continue

    if [row, sand_col] == SAND_CORDS:
      break

    if not (row, sand_col-1) in filled:
      # go left
      sand_row = row
      sand_col -= 1
    elif not (row, sand_col+1) in filled:
      # go right
      sand_row = row
      sand_col += 1
    else:
      # fill
      filled[(row-1, sand_col)] = SAND
      number_of_sand += 1
      sand_row = SAND_CORDS[0]
      sand_col = SAND_CORDS[1]

  min_rows = min([row for row, col in filled.keys()] + [SAND_CORDS[0]])
  min_cols = min([col for row, col in filled.keys()] + [SAND_CORDS[1]])
  max_rows = max([row for row, col in filled.keys()] + [SAND_CORDS[0]])
  max_cols = max([col for row, col in filled.keys()] + [SAND_CORDS[1]])

  offset_row = min_rows
  offset_col = min_cols - 1

  grid = Grid(max_rows + 2, max_cols + 2, offset_row=offset_row, offset_col=offset_col)

  for i in range(grid.cols):
    grid.set(grid.rows - 1 , i, ROCKS)

  for fill in filled:
    grid.set(fill[0] - offset_row, fill[1] - offset_col, filled[fill])

  print(grid)
  print("Number of sand: {}".format(number_of_sand))

  return 0
