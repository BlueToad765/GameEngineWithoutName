"""
SAVE SYSTEM
SAVE SYSTEM
SAVE SYSTEM
"""

def save_res(file=str, current_res=tuple):
  file = open(file, "w")
  file.write(f"{current_res[0]}\n{current_res[1]}\n")
  file.close()


"""
def read_res(file=str):
  file=str = open(file, "r")
  res = []
  for line in file:
    length = ""
    i = 0
    while line[i] != "\n":
      length += line[i]
      i += 1
    length = int(length)
    res.append(length)
  file=str.close()
  resolution = (res[0], res[1])
  return resolution
"""


def save_time(file=str, tick=int, sec=int, min=int, hour=int):
  file = open(file, "w")
  file.write(f"{tick}\n{sec}\n{min}\n{hour}\n")
  file.close()

def load_time(file=str):
  file = open(file, "r")
  time_list_smh = []
  for line in file:
    i = 0
    length = ""
    while line[i] != "\n":
        length += line[i]
        i += 1
    time_list_smh.append(int(i))
  file.close()
  return time_list_smh


def read_save(file=str):
  file = open(file, "r")
  stat_list = []
  for line in file:
    stat_list.append(str(line-2))
  file.close()
  return stat_list

def savePlayer(file=str, score=int, level=int):
  file = open(file, "w")
  file.write(f"{score}\n{level}\n")
  file.close()


def loadPlayer(player):
  stats = read_save()
  player.score = int(stats[0])
  player.level = int(stats[2])
  return player

def clear_save(file=str):
  savePlayer(file, 0, 1)