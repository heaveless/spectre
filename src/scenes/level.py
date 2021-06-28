import pygame as pg
from pygame.mixer import set_num_channels
from ..entites.player import Player

class Level():
  def __init__(self, resources):
    self.json_maps = resources.load_all_json_maps()
    self.image_maps = resources.load_all_image_maps()
    self.__load_level()
    self.__load_hero()

    self.layers = []

  def __load_level(self, level = 0):
    index = str(level)
    self.current_index = level
    self.current_level = self.json_maps[index]
    self.current_background = self.image_maps[index]

  def change(self):
    self.current_index +=1
    self.__load_level(self.current_index)
    self.__load_hero()
  

  def verificador(self):
    end=self.current_level["end"]
    point=end["location"]
    if self.player.collidepoint(point["x"],point["y"]):
      self.change()
      self.__restart_level()

  def __load_hero(self):
    start = self.current_level["start"]
    x = start["x"]
    y = start["y"]
    self.player = Player(x, y, 100, 100)


  def __check_collision(self):
    return self.player.collidelistall(self.layers)

  def __restart_level(self):
    position=self.current_level["start"]
    self.player.x=position["x"]
    self.player.y=position["y"]

  def update(self, delta_time):
    hits = self.__check_collision()
    self.player.update(len(hits) > 0)
    self.verificador()

  def draw(self, surface):
    surface.blit(self.current_background, (0, 0))

    self.layers = []
    for layer in self.current_level["layers"]:
      width = layer["width"]
      height = layer["height"]
      x = layer["x"]
      y = layer["y"]

      rect = pg.Rect(x, y, width, height)
      pg.draw.rect(surface, (255, 255, 255), rect)
      self.layers.append(rect)

    self.player.draw(surface)