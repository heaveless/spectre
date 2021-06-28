import pygame as pg

from ..entites.player import Player

class Level():
  def __init__(self, resources):
    self.json_maps = resources.load_all_json_maps()
    self.image_maps = resources.load_all_image_maps()
    self.__load_level()
    self.__load_hero()

  def __load_level(self, level = 0):
    index = str(level)
    self.current_level = self.json_maps[index]
    self.current_background = self.image_maps[index]

  def __load_hero(self):
    start = self.current_level["start"]
    x = start["x"]
    y = start["y"]
    self.player = Player(x, y)

  def __restart_level(self):
    pass

  def update(self, delta_time):
    pass

  def draw(self, surface):
    surface.blit(self.current_background, (0, 0))

    for layer in self.current_level["layers"]:
      width = layer["width"]
      height = layer["height"]
      x = layer["x"]
      y = layer["y"]

      rect = pg.Surface([width, height])
      rect.fill((255, 255, 255))
      surface.blit(rect, (x, y))