from pathlib import Path
from aoc_io import Input
def parse_packets(lines):
  packets = []
  i = 0
  current_pair = []
  while i < len(lines):
    line = lines[i].strip()
    if len(line) == 0:
      packets.append(current_pair)
      current_pair = []
    else:
      current_pair.append(parse_packet(line))
    i += 1

  if len(current_pair) > 0:
    packets.append(current_pair)
  return packets

def parse_all_packets(lines):
  packets = []
  for line in lines:
    line = line.strip()
    if len(line) == 0:
      continue
    packets.append(parse_packet(line))
  return packets

def parse_packet(line):
  if line[0] != "[" and line[-1] != "]":
    return []

  stack = [[]]
  done = []
  i = 1
  while len(stack) > 0 and i < len(line):
    curr = stack.pop()
    char = line[i]
    if char == "[":
      new_list = []
      curr.append(new_list)
      stack.append(curr)
      stack.append(new_list)
    elif char == "]":
      done.append(curr)
    elif char != ",":
      chars = char
      i += 1
      while i  < len(line) and line[i] != "," and line[i] != "]":
        chars += line[i]
        i += 1
      i -= 1
      curr.append(int(chars))
      stack.append(curr)
    else:
      stack.append(curr)
    i += 1

  return done[-1]

def is_pair_valid(pair):
  if len(pair) != 2:
    return False

  packet_1 = pair[0]
  packet_2 = pair[1]

  if type(packet_1) == int and type(packet_2) == int:
    if packet_1 < packet_2:
      return True
    elif packet_1 > packet_2:
      return False
  elif type(packet_1) == list and type(packet_2) == list:
    i = 0
    while i < len(packet_1):
      if i >= len(packet_2):
        return False

      item_1 = packet_1[i]
      item_2 = packet_2[i]

      valid = is_pair_valid([item_1, item_2])
      if not valid is None:
        return valid

      i += 1

    if len(packet_2) == len(packet_1):
      return None
    return len(packet_1) < len(packet_2)
  elif type(packet_1) == int:
    return is_pair_valid([[packet_1], packet_2])
  elif type(packet_2) == int:
    return is_pair_valid([packet_1, [packet_2]])


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
    io = Input(2022, 13)
    lines = io.get_lines()

  if len(lines) == 0:
    print("No input given")
    return 1

  packet_pairs = parse_packets(lines)

  valid = []
  for i in range(len(packet_pairs)):
    pair = packet_pairs[i]
    if is_pair_valid(pair):
      valid.append(i + 1)

  print("Valid packets: ", valid)
  print("Sum: ", sum(valid))
  return 0

def sort_packets(packets):
  if len(packets) == 0:
    return []

  sorted = [packets[0]]
  i = 1
  while i < len(packets):
    packet = packets[i]
    j = 0
    while j < len(sorted):
      sorted_packet = sorted[j]
      if is_pair_valid([packet, sorted_packet]):
        sorted.insert(j, packet)
        break
      j += 1
    if j == len(sorted):
      sorted.append(packet)
    i += 1
  return sorted

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
    io = Input(2022, 13)
    lines = io.get_lines()

  lines.append("[[2]]\n")
  lines.append("[[6]]\n")

  packets = parse_all_packets(lines)
  sorted_packets = sort_packets(packets)

  for packet in sorted_packets:
    print(packet)

  ind_1 = sorted_packets.index([[2]]) + 1
  ind_2 = sorted_packets.index([[6]]) + 1

  print("Ind 1: ", ind_1)
  print("Ind 2: ", ind_2)
  print("Signal: ", ind_1 * ind_2)


  if len(lines) == 0:
    print("No input given")
    return 1

  return 0
