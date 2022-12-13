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
    io = Input(2022, 24)
    lines = io.get_lines()

  if len(lines) == 0:
    print("No input given")
    return 1

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
    io = Input(2022, 24)
    lines = io.get_lines()

  if len(lines) == 0:
    print("No input given")
    return 1

  return 0
