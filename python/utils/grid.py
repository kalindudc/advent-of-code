class Grid(object):
  def __init__(self, rows, cols, offset_row=0, offset_col=0, default_value="."):
    self.rows = rows - offset_row
    self.cols = cols - offset_col
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
    col_row_1 = "      "
    col_row_2 = "      "
    col_row_3 = "      "

    res = ""
    for i in range(len(self.map[0])):
      col_num = str(i + self.offset_col).zfill(3)
      col_row_1 += col_num[0] + " "
      col_row_2 += col_num[1] + " "
      col_row_3 += col_num[2] + " "

    res += col_row_1 + "\n"
    res += col_row_2 + "\n"
    res += col_row_3 + "\n"
    for i in range(len(self.map[0]) + 3):
      res += "- "
    res += "\n"

    for i in range(len(self.map)):
      for j in range(len(self.map[0])):
        if j == 0:
          res += str(i + self.offset_row).zfill(3) + " | "
        res += str(self.map[i][j]) +  " "
      res += "\n"
    return res

  def is_edge(self, x, y):
    return x == 0 or y == 0 or x == self.rows - 1 or y == self.cols - 1

  def get(self, x, y):
    return self.map[x][y]

  def set(self, x, y, value):
    self.map[x][y] = value

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
        x = current[0] + i
        y = current[1] + j

        if x < 0 or y < 0 or x >= self.rows or y >= self.cols:
          continue
        if (x,y) in visited:
          continue

        if can_visit(self, current, (x, y)):
          visited.add((x,y))
          queue.append(((x,y), path + [(x,y)]))

    return []



