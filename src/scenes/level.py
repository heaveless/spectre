import pygame as pg

class Level():
  def __init__(self, resources):
    self.json_maps = resources.load_all_json_maps()
    self.__load_level()

  def __load_level(self, level = 0):
    self.current_level = self.json_maps[str(level)]

  def __restart_level(self):
    pass

  def update(self, level):
    pass

  def draw(self, surface):
    for layer in self.current_level["layers"]:
      rect = pg.Surface([layer["width"], layer["height"]])
      rect.fill((255, 255, 255))

      surface.blit(rect, (layer["x"], layer["y"]))