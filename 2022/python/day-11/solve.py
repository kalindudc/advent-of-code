#! /usr/bin/python3

import sys
from pathlib import Path
from aoc_io import Input
import math
import inspect

NUM_ROUNDS = 10000
OPERATIONS = {
  "*": lambda x, y: x * y,
  "+": lambda x, y: x + y,
  "-": lambda x, y: x - y,
  "/": lambda x, y: x / y,
}

def print_monkeys(monkey_data):
  for monkey in monkey_data:
    print("Monkey {}: {}".format(monkey, monkey_data[monkey]["items"]))
    print("OP {}".format(monkey_data[monkey]["op"](2)))

def create_lambda(op_parts):
  if op_parts[0] == "old" and op_parts[2] == "old":
    return lambda x: OPERATIONS[op_parts[1].strip()](x, x)
  elif op_parts[0] == "old":
    const = int(op_parts[2].strip())
    return lambda x: OPERATIONS[op_parts[1].strip()](x, const)
  else:
    const = int(op_parts[0].strip())
    return lambda x: OPERATIONS[op_parts[1].strip()](const, x)

def parse_lines(lines):
  current_monkey = "0"
  monkey_data = {}

  for line in lines:
    line = line.strip()
    if len(line) == 0:
      continue

    if line.startswith("Monkey"):
      _split = line.split(" ")
      current_monkey = _split[1][:-1]
      monkey_data[current_monkey] = {
        "items": [],
        "op": None,
        "test": None,
        "conditions": {
          True: None,
          False: None
        }
      }
    elif line.startswith("Starting items"):
      _split = line.split(":")
      monkey_data[current_monkey]["items"] = [int(x.strip()) for x in _split[1].split(",")]
    elif line.startswith("Operation"):
      _split = line.split(":")
      op_parts = _split[1].strip().split(" ")
      monkey_data[current_monkey]["op"] = create_lambda(op_parts[2:])
    elif line.startswith("Test"):
      _split = line.split(":")
      divisor = int(_split[1].strip().split(" ")[2].strip())
      monkey_data[current_monkey]["test"] = divisor
    elif line.startswith("If"):
      _split = line.split(":")
      condition = _split[0].split(" ")[1].strip() == "true"
      throw_to = _split[1].split(" ")[-1].strip()
      monkey_data[current_monkey]["conditions"][condition] = throw_to

  return monkey_data


def get_relief_factor(monkey_data):
  gcd = 1
  for monkey in monkey_data:
    gcd *= monkey_data[monkey]["test"]

  return gcd

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
    io = Input(2022, 11)
    lines = io.get_lines()

  current_monkey = 0
  monkey_data = parse_lines(lines)

  relief_devisor = 3
  inspected_items = [0 for i in range(len(monkey_data))]
  for i in range(NUM_ROUNDS):
    print("Round {}".format(i))
    for j in range(len(monkey_data)):
      current_monkey = str(j)
      inspected_items[int(current_monkey)] += len(monkey_data[current_monkey]["items"])
      for item in monkey_data[current_monkey]["items"]:
        worry_level = monkey_data[current_monkey]["op"](item)
        worry_level = math.floor(worry_level/relief_devisor)
        condition = (worry_level % monkey_data[current_monkey]["test"]) == 0
        throw_to = monkey_data[current_monkey]["conditions"][condition]
        monkey_data[throw_to]["items"].append(worry_level)
        print("Monkey {} threw {} to Monkey {} on {}".format(current_monkey, worry_level, throw_to, condition))
      monkey_data[current_monkey]["items"] = []

    for monkey in monkey_data:
      print("Monkey {}: {}".format(monkey, monkey_data[monkey]["items"]))

    print("")

  inspected_items.sort(reverse=True)
  print(inspected_items)
  print(inspected_items[0] * inspected_items[1])
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
    io = Input(2022, 11)
    lines = io.get_lines()

  current_monkey = 0
  monkey_data = parse_lines(lines)

  gcd_factor = get_relief_factor(monkey_data)
  inspected_items = [0 for i in range(len(monkey_data))]
  for i in range(NUM_ROUNDS):
    print("Round {}".format(i))
    for j in range(len(monkey_data)):
      current_monkey = str(j)
      inspected_items[int(current_monkey)] += len(monkey_data[current_monkey]["items"])
      for item in monkey_data[current_monkey]["items"]:
        worry_level = monkey_data[current_monkey]["op"](item)
        #worry_level = math.floor(worry_level/relief_divisor)
        condition = (worry_level % monkey_data[current_monkey]["test"]) == 0
        throw_to = monkey_data[current_monkey]["conditions"][condition]
        monkey_data[throw_to]["items"].append(worry_level % gcd_factor)
        print("Monkey {} threw {} to Monkey {} on {}".format(current_monkey, worry_level, throw_to, condition))
      monkey_data[current_monkey]["items"] = []

    for monkey in monkey_data:
      print("Monkey {}: {}".format(monkey, monkey_data[monkey]["items"]))

    print("")

  inspected_items.sort(reverse=True)
  print(inspected_items)
  print(inspected_items[0] * inspected_items[1])
  return 0


if __name__ == "__main__":
  print ("MAIN 1...")
  main(sys.argv)
  print ("\nMAIN 2...")
  main_2(sys.argv)
