import requests
import sys

class Input(object):
  def __init__(self, year, day):
    self.year = year
    self.day = day
    self.input_url = "https://adventofcode.com/{}/day/{}/input".format(year, day)
    self.secrets_file_path = [x for x in sys.path if x.endswith(".secrets")][0]
    self.lines = self.get_input_lines()

  def get_lines(self):
    return self.lines

  def get_input_lines(self):
    cookies = {}
    session = ""
    with open(self.secrets_file_path) as f:
      for line in f:
        if line.startswith("SESSION") or line.startswith("session"):
          session = line.split("=")[1].strip()
          break

    if session == "":
      print("No session found")
      return []

    cookies["session"] = session
    r = requests.get(self.input_url, cookies=cookies)
    if r.status_code != 200:
      print("Could not get input file from adventofcode.com")
      return []

    return r.text.splitlines()


