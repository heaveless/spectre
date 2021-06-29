from os import X_OK
import pygame as pg
from pygame.mixer import set_num_channels
from ..entites.player import Player

class Level():
  def __init__(self, resources, surface):
    self.json_maps = resources.load_all_json_maps()
    self.image_maps = resources.load_all_image_maps()
    self.music = resources.load_all_music()
    self.surface = surface
    self.__load_level()
    self.__load_hero()
    self.__play_music()

    self.layers = []

  def __play_music(self):
    pass
    # pg.mixer.music.load(self.music["industrial"])
    # pg.mixer.music.play(-1)

  def __load_level(self, level = 0):
    index = str(level)
    self.current_index = level
    self.current_level = self.json_maps[index]
    self.current_background = self.image_maps[index]

  def change(self):
    self.current_index +=1
    if self.current_index < 10:
      self.__load_level(self.current_index)
      self.__load_hero()
      

  def verificador(self):
    end=self.current_level["end"]
    point=end["location"]
    if self.player.rect.collidepoint(point["x"],point["y"]):
      self.change()

  def __load_hero(self):
    start = self.current_level["start"]
    x = start["x"]
    y = start["y"]
    self.player = Player(x, y)
    # self.player.rect.x = x
    # print(self.player.rect.x)
    # self.player.rect.y = y
    # print(self.player.rect.y)


  def __check_collision(self):
    return self.player.rect.collidelistall(self.layers)

  def __restart_level(self):
    if self.player.rect.y>610:
      self.__load_hero()

  def update(self, delta_time, surface):
    hits = self.__check_collision()
    self.player.update(len(hits) > 0, surface)
    self.verificador()
    self.__restart_level()

  def draw(self, surface):
    surface.blit(self.current_background, (0, 0))

    self.layers = []
    for layer in self.current_level["layers"]:
      width = layer["width"]
      height = layer["height"]
      x = layer["x"]
      y = layer["y"]

      rect = pg.Surface((width, height))
      rect.set_colorkey((0,0,0))
      # surface.blit(rect, (x, y))
      rect = rect.get_rect()
      rect.x = x
      rect.y = y
      # print(rect.height, rect.width, rect.x, rect.y)
      self.layers.append(rect)
    self.player.draw(surface)