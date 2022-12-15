from pathlib import Path
from aoc_io import Input
from utils import Grid

SENSOR = "S"
BEACON = "B"

def parse_lines(lines):
  sensors = {}
  distances = {}
  for line in lines:
    line = line.strip()
    if len(line) == 0:
      continue

    parts = line.split(":")
    sensor_descriptor = parts[0].strip()
    beacon_descriptor = parts[1].strip()

    raw_sensor_cords = sensor_descriptor[sensor_descriptor.index("x="):]
    raw_beacon_cords = beacon_descriptor[beacon_descriptor.index("x="):]

    sensor_cords_parts = raw_sensor_cords.split(",")
    beacon_cords_parts = raw_beacon_cords.split(",")

    sensor_cords = (int(sensor_cords_parts[1].split("=")[1].strip()), int(sensor_cords_parts[0].split("=")[1].strip()))
    beacon_cords = (int(beacon_cords_parts[1].split("=")[1].strip()), int(beacon_cords_parts[0].split("=")[1].strip()))
    sensors[sensor_cords] = beacon_cords
    distances[sensor_cords] = distance(sensor_cords, beacon_cords)

  print(sensors)
  print(distances)

  min_row = min([c[0] - distances[c] for c in sensors])
  max_row = max([c[0] + distances[c] for c in sensors])
  min_col = min([c[1] - distances[c] for c in sensors])
  max_col = max([c[1] + distances[c] for c in sensors])

  offset_row = min_row
  offset_col = min_col
  print(min_row, max_row, min_col, max_col)
  print(offset_row, offset_col)
  print((max_row - min_row) + 1, (max_col - min_col) + 1)

  # grid = GridV2((max_row - min_row) + 1, (max_col - min_col) + 1, offset_row, offset_col)
  # for sensor in sensors:
  #   grid.set(sensor[0], sensor[1], SENSOR)
  #   grid.set(sensors[sensor][0], sensors[sensor][1], BEACON)

  return sensors, distances, min_row, max_row, min_col, max_col

def distance(start, end):
  return abs(end[0] - start[0]) + abs(end[1] - start[1])

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
    io = Input(2022, 15)
    lines = io.get_lines()

  if len(lines) == 0:
    print("No input given")
    return 1

  sensors, distances, min_row, max_row, min_col, max_col = parse_lines(lines)
  beacons = sensors.values()

  row_to_inspect = 10 if len(args) < 3 else int(args[2])
  print("Row to inspect: ", row_to_inspect)

  no_beacon = 0
  for col in range(min_col, max_col + 1):
    current = (row_to_inspect, col)
    if current in beacons:
      continue

    for sensor in sensors:
      distance_to_sensor = distance(current, sensor)

      if distance_to_sensor <= distances[sensor]:
        no_beacon += 1
        break

  print("No beacon: ", no_beacon)

  return 0

def tune_frequency(row, col):
  return (col * 4000000) + row

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
    io = Input(2022, 15)
    lines = io.get_lines()

  if len(lines) == 0:
    print("No input given")
    return 1

  sensors, distances, min_row, max_row, min_col, max_col = parse_lines(lines)
  beacons = sensors.values()

  radius = 20 if len(args) < 4 else int(args[3])
  steps = 0

  for row in range(0, radius + 1):
    col = -1
    while col < radius + 1:
      print(row, col)
      steps += 1
      col += 1
      current = (row, col)
      if current in beacons:
        continue

      found = True
      for sensor in sensors:
        distance_to_sensor = distance(current, sensor)

        if distance_to_sensor <= distances[sensor]:
          # skip the range of his sensor
          col = sensor[1] + (distances[sensor] - abs(sensor[0] - current[0]))
          found = False
          break

      if found:
        print("Possible: ", current, tune_frequency(row, col))
        print("Steps: ", steps)
        return 0


  # This is still super slow :(
  return 0
