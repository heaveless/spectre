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
      self.__vertical_movement(DirectionType.UP)
  
  def __run(self, type):
    if type == DirectionType.RIGHT:
      self.x += self.velocity.x  
      self.set_location(self.x, self.y)
    elif type == DirectionType.LEFT:
      self.x -= self.velocity.x
      self.set_location(self.x, self.y)
  def __gravity(self):
    self.velocity.y += self.gravity
    self.set_location(self.x, self.y + self.velocity.y)

  def __vertical_movement(self, type):
    self.velocity.y += self.gravity 
    if type == DirectionType.UP:
      if self.velocity.y < 8:
        self.velocity.y += 6
        self.set_location(self.x, self.y - self.velocity.y)
      else:
        self.__gravity()
    

  def update(self, delta_time):
    self.__pressed()
    # self.__gravity()

  def set_location(self, x, y):
    self.x = x
    self.y = y

  def draw(self, surface):
    rect = pg.Surface([100, 100])
    rect.fill((255, 0, 255))

    surface.blit(rect, (self.x, self.y))