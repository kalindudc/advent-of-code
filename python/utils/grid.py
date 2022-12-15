class Grid(object):
  def __init__(self, rows, cols, offset_row=0, offset_col=0, default_value="."):
    self.rows = rows
    self.cols = cols
    self.move_dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    self.map = [[default_value for i in range(self.cols)] for j in range(self.rows)]
    self.offset_row = offset_row
    self.offset_col = offset_col

  def set_move_dirs(self, moves):
    self.move_dirs = moves

  def parse_map(self, lines):
    for i in range(self.rows):
      for j in range(self.cols):
        self.map[i][j] = lines[i][j]

  def set_map(self, map):
    self.map = map

  def __repr__(self):
    return str(self.__str__())

  def __str__(self):
    fill = len(str(self.offset_row)) + 1
    col_rows = [" " * (fill + 3) for i in range(fill)]

    res = "\n"
    for i in range(len(self.map[0])):
      col_num = str(i + self.offset_col).zfill(fill)
      for j in range(len(col_rows)):
        col_rows[j] += col_num[j] + " "

    for col_row in col_rows:
      res += col_row + "\n"

    for i in range(len(self.map[0]) + fill):
      res += "- "
    res += "\n"

    for i in range(len(self.map)):
      for j in range(len(self.map[0])):
        if j == 0:
          res += str(i + self.offset_row).zfill(fill) + " | "
        res += str(self.map[i][j]) +  " "
      res += "\n"
    return res

  def is_edge(self, x, y):
    return x == 0 or y == 0 or x == self.rows - 1 or y == self.cols - 1

  def get(self, row, col):
    return self.map[row + (-1 * self.offset_row)][col + (-1 * self.offset_col)]

  def set(self, row, col, value):
    self.map[row + (-1 * self.offset_row)][col + (-1 * self.offset_col)] = value

  def find_symbol(self, symbol):
    for i in range(len(self.map)):
      for j in range(len(self.map[0])):
        if self.map[i][j] == symbol:
          return (i,j)
    return None

  def find_all_symbols(self, symbol):
    res = []
    for i in range(self.rows):
      for j in range(self.cols):
        if self.map[i][j] == symbol:
          res.append((i,j))
    return res

  def get_distance(self, start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

  def size(self):
    return (self.rows, self.cols)

  def __can_visit(grid, current, next):
    return True

  def find_shortest_path(self, start, end, can_visit=__can_visit):
    queue = [(start, [start])]
    visited = set()

    while len(queue) > 0:
      current, path = queue.pop(0)
      if current == end:
        return path

      for i,j in self.move_dirs:
        x = current[0] + (-1 * self.offset_row) + i
        y = current[1]+ (-1 * self.offset_col) + j

        if x < 0 or y < 0 or x >= self.rows or y >= self.cols:
          continue
        if (x,y) in visited:
          continue

        real_x = x + self.offset_row
        real_y = y + self.offset_col
        if can_visit(self, current, (real_x, real_y)):
          visited.add((x,y))
          queue.append(((real_x,real_y), path + [(real_x,real_y)]))

    return []

  def find_closest_value(self, start, value, can_visit=__can_visit):
    queue = [start]
    visited = set()

    while len(queue) > 0:
      current = queue.pop(0)
      if self.get(current[0], current[1]) == value:
        return current

      for i,j in self.move_dirs:
        x = current[0] + (-1 * self.offset_row) + i
        y = current[1]+ (-1 * self.offset_col) + j

        if x < 0 or y < 0 or x >= self.rows or y >= self.cols:
          continue
        if (x,y) in visited:
          continue

        real_x = x + self.offset_row
        real_y = y + self.offset_col
        if can_visit(self, current, (real_x, real_y)):
          visited.add((x,y))
          queue.append((real_x, real_y))

    return ()
