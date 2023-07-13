import pygame
from image_load import *
from save import *
from math import fmod
from sys import exit
from time import perf_counter


pygame.init()

"""
engine for my games, heavily modded for each game
i reccomend checking the documentation file and screwing around in a new file
Creative Commons Zero licence, do what you want
made by an idiot
"""


FONT = pygame.font.Font('assets/fonts/impact.ttf')


# group class
class Group(list):
  def __init__(self):
    self = super.__init__(self)

  def update(self):
    for i in self:
      i.update()


# all possible resolutions
RESOLUTIONS = {
  "450p" : (800, 450),
  "720p" : (1280, 720),
  "768p" : (1366, 768),
  "900p" : (1600, 900),
  "1080p" : (1920, 1080),
  "1440p" : (2560, 1440)
}
# sets default resolution
current_resolution = RESOLUTIONS.get("450p")

# button list for resolution buttons
RES_BTTN_LIST = [
  BTTN_RES_450,
  BTTN_RES_720,
  BTTN_RES_768,
  BTTN_RES_900,
  BTTN_RES_1080,
  BTTN_RES_1440
]
# coordinates for resolution buttons on the start screen
RES_BTTN_COORDS = {
  BTTN_RES_450 : (35, 50),
  BTTN_RES_720 : (95, 50),
  BTTN_RES_768 : (155, 50),
  BTTN_RES_900 : (215, 50),
  BTTN_RES_1080 : (275, 50),
  BTTN_RES_1440 : (335, 50)
}


# gamestates to tell whether to be on the titlescreen, startscreen, or game
gamestates = {
  0 : "startup",
  1 : "titlescreen",
  2 : "game"
}


# default resolution
gamestate = gamestates[1]


# window setup
SCREEN_SIZE = current_resolution
WIN_WID = current_resolution[0]
WIN_HIGH = current_resolution[1]


# frame timing system
CLOCK = pygame.time.Clock()


def update_resolution(res_key=str, FONT=FONT, BTTN_CHECK=pygame.image):
  global WIN_WID, WIN_HIGH, START_BG
  old_res = RESOLUTIONS.get("450p")

  res = RESOLUTIONS.get(res_key)


  STARTSCREEN = pygame.display.set_mode(res)
  current_resolution = res

  START_BG = pygame.transform.scale(START_BG, (current_resolution))
  STARTSCREEN.blit(START_BG, (0, 0))

  OK_LABEL = FONT.render("resolution ok?", True, "white")
  STARTSCREEN.blit(OK_LABEL, ((res[0] / 2), (res[1] / 2) - 30))

  STARTSCREEN.blit(BTTN_CHECK, ((res[0] / 2), (res[1] / 2)))

  pygame.display.flip()

  timer_start = perf_counter()

  update_res_del = 1

  while update_res_del:
    time_elapsed = perf_counter()
    if time_elapsed - timer_start >= 10:
      STARTSCREEN = pygame.display.set_mode(old_res)
      START_BG = pygame.transform.scale(START_BG, (old_res))
      pygame.display.flip()
      break
    for ev in pygame.event.get():
      if ev.type == pygame.MOUSEBUTTONDOWN:
        MOUSE = pygame.mouse.get_pos()
        if MOUSE[0] > (res[0] / 2) and MOUSE[0] < ((res[0] / 2) + 50) and MOUSE[1] > (res[1] / 2) and MOUSE[1] < ((res[1] / 2) + 50):
          WIN_WID = current_resolution[0]
          WIN_HIGH = current_resolution[1]
          save_res(current_resolution)
          return res
        


def ERROR(line=int):
  print(f'error: line {line}')
  exit(0)


def int_checker(item, errorLine=int):
  if not isinstance(item, int):
    ERROR(errorLine)
  else:
    return item
  

"""
PLAYER SYSTEM
PLAYER SYSTEM
PLAYER SYSTEM
"""
class Player(pygame.sprite.Sprite):

  # creates player system
  def __init__(self, image=pygame.image, Xpos=0, Ypos=0, lvl_player=int, mass=int, effect_grav=bool):
    self = super.__init__(self)
    self.image = image
    self.rect = self.image.get_rect()
    
    self.rect.x = Xpos
    self.rect.y = Ypos

    self.level = lvl_player

    self.gravity = effect_grav
    self.mass = mass

    self.yvel = 0
    self.xvel = 0