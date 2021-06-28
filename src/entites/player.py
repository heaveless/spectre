import pygame as pg

from ..common.enums.direction_type import DirectionType

class Player():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.gravity = .35
    self.velocity = pg.math.Vector2(4, 0)

  def __pressed(self):
    keys = pg.key.get_pressed()
    if keys[pg.K_d]:
      self.__run(DirectionType.RIGHT)
    if keys[pg.K_a]:
      self.__run(DirectionType.LEFT)
    if keys[pg.K_w]:
      self.vertical_movement(DirectionType.UP)

  def __run(self, type):
    if type == DirectionType.RIGHT:
      self.x += self.velocity.x  
      self.set_location(self.x, self.y)
    elif type == DirectionType.LEFT:
      self.x -= self.velocity.x
      self.set_location(self.x, self.y)
  
  def vertical_movement(self, type):
    self.velocity.y += self.gravity 
    if type == DirectionType.UP:
      self.velocity.y += 4
      self.set_location(self.x, self.y + self.velocity.y)

  def update(self, delta_time):
    self.__pressed()

  def set_location(self, x, y):
    self.x = x
    self.y = y

  def draw(self, surface):
    rect = pg.Surface([100, 100])
    rect.fill((255, 0, 255))

    surface.blit(rect, (self.x, self.y))