import pygame as pg
from pygame.mixer import set_num_channels
from ..entites.player import Player

class Level():
  def __init__(self, resources):
    self.json_maps = resources.load_all_json_maps()
    self.image_maps = resources.load_all_image_maps()
    self.music = resources.load_all_music()
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
    self.player = Player()


  def __check_collision(self):
    return self.player.rect.collidelistall(self.layers)

  def __restart_level(self):
    if self.player.rect.y>610:
      self.__load_hero()

  def update(self, delta_time):
    hits = self.__check_collision()
    self.player.update(len(hits) > 0)
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
      surface.blit(rect, (x, y))
      rect = rect.get_rect()
      self.layers.append(rect)

    self.player.draw(surface)