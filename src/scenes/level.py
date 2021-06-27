import pygame as pg

class Level():
  def __init__(self, resources):
    self.json_maps = resources.load_all_json_maps()
    self.image_maps = resources.load_all_image_maps()
    self.__load_level()

<<<<<<< Updated upstream
  def __load_level(self, level = 0):
    index = str(level)
    self.current_level = self.json_maps[index]
    self.current_background = self.image_maps[index]
=======
  def __load_level(self, level = 3):
    self.current_level = self.json_maps[str(level)]
>>>>>>> Stashed changes

  def __restart_level(self):
    pass

  def update(self, level):
    pass

  def draw(self, surface):
    surface.blit(self.current_background, (0, 0))

    for layer in self.current_level["layers"]:
      rect = pg.Surface([layer["width"], layer["height"]])
      rect.fill((255, 255, 255))

      surface.blit(rect, (layer["x"], layer["y"]))