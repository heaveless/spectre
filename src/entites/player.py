import pygame as pg

from ..common.enums.direction_type import DirectionType

class Player():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.velocity = 5

  def __pressed(self):
    keys = pg.key.get_pressed()
    if keys[pg.K_d]:
      self.__run(DirectionType.RIGHT)
    if keys[pg.K_a]:
      self.__run(DirectionType.LEFT)
    if keys[pg.K_w]:
      self.__jump()

  def __gravity(self):
    self.set_location(self.x, self.y + self.velocity)

  def __run(self, type):
    if type == DirectionType.RIGHT:
      self.set_location(self.x + self.velocity, self.y)
    elif type == DirectionType.LEFT:
      self.set_location(self.x - self.velocity, self.y)

  def __jump(self):
    self.set_location(self.x, self.y - self.velocity)

  def update(self, delta_time):
    self.__pressed()
    self.__gravity()

  def set_location(self, x, y):
    self.x = x
    self.y = y

  def draw(self, surface):
    rect = pg.Surface([100, 100])
    rect.fill((255, 0, 255))

    surface.blit(rect, (self.x, self.y))