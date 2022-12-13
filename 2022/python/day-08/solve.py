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
    io = Input(2022, 8)
    lines = io.get_lines()

  cols = len(lines[0]) - 1
  rows = len(lines)

  visible = 0
  for y in range(1, cols-1):
    for x in range(1, rows-1):
      is_visible_up = True
      is_visible_down = True
      is_visible_left = True
      is_visible_right = True

      print("Checking: %d,%d | Value: %d" % (x, y, int(lines[x][y])))
      # up
      for dx in range(0, x):
        print("  > Checking: %d, Current: %d" % (int(lines[dx][y]), int(lines[x][y])))

        if int(lines[dx][y]) >= int(lines[x][y]):
          is_visible_up = False
          break

      # down
      for dx in range(x+1, rows):
        print("  > Checking: %d, Current: %d" % (int(lines[dx][y]), int(lines[x][y])))

        if int(lines[dx][y]) >= int(lines[x][y]):
          is_visible_down = False
          break

      # left
      for dy in range(0, y):
        print("  > Checking: %d, Current: %d" % (int(lines[dx][y]), int(lines[x][y])))

        if int(lines[x][dy]) >= int(lines[x][y]):
          is_visible_left = False
          break

      # right
      for dy in range(y+1, cols):
        print("  > Checking: %d, Current: %d" % (int(lines[dx][y]), int(lines[x][y])))

        if int(lines[x][dy]) >= int(lines[x][y]):
          is_visible_right = False
          break

      if is_visible_up or is_visible_down or is_visible_left or is_visible_right:
        print("  > Visible: %d,%d" % (x, y))
        visible += 1

  print(visible + ((2*rows) + ((cols - 2) * 2)))
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
    io = Input(2022, 8)
    lines = io.get_lines()

  cols = len(lines[0]) - 1
  rows = len(lines)

  scores = []
  for y in range(1, cols-1):
    for x in range(1, rows-1):
      print("Checking: %d,%d | Value: %d" % (x, y, int(lines[x][y])))

      score_1 = 0
      score_2 = 0
      score_3 = 0
      score_4 = 0
      # up
      for dx in range(x-1, -1, -1):
        print("  > Checking: %d, Current: %d" % (int(lines[dx][y]), int(lines[x][y])))
        score_1 += 1
        if int(lines[dx][y]) >= int(lines[x][y]):
          break

      # down
      for dx in range(x+1, rows):
        print("  > Checking: %d, Current: %d" % (int(lines[dx][y]), int(lines[x][y])))
        score_2 += 1
        if int(lines[dx][y]) >= int(lines[x][y]):
          break

      # left
      for dy in range(y-1, -1, -1):
        print("  > Checking: %d, Current: %d" % (int(lines[dx][y]), int(lines[x][y])))
        score_3 += 1
        if int(lines[x][dy]) >= int(lines[x][y]):
          break

      # right
      for dy in range(y+1, cols):
        print("  > Checking: %d, Current: %d" % (int(lines[dx][y]), int(lines[x][y])))
        score_4 += 1
        if int(lines[x][dy]) >= int(lines[x][y]):
          break

      scores.append(score_1 * score_2 * score_3 * score_4)

    print(max(scores))
  return 0

if __name__ == "__main__":
  print ("MAIN 1...")
  main(sys.argv)
  print ("\nMAIN 2...")
  main_2(sys.argv)
