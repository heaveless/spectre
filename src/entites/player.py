import pygame as pg


from ..common.enums.direction_type import DirectionType

class Player(pg.Rect):
  def __init__(self, x, y, width, height):
    pg.Rect.__init__(self, x, y, width, height)
    
    self.position = pg.Vector2(x, y)
    self.velocity = pg.Vector2(0, 0)
    self.gravity = 0.5

  def __pressed(self):
    self.acceleration = pg.Vector2(0, 0.1)
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
      self.velocity.x = -5
    elif keys[pg.K_d]:
      self.velocity.x = 5
    else:
      self.velocity.x = 0
    if keys[pg.K_w] and self.hits:
      self.velocity.y -= 13

  def update(self, hits):
    self.hits = hits

    self.velocity.y += self.gravity

    if self.hits:
      self.velocity.y = -self.gravity

    self.__pressed()

    self.position += self.velocity

    if self.position.x > 800:
      self.position.x = 0
    if self.position.x < 0:
      self.position.x = 800

    

    self.x = self.position.x 
    self.y = self.position.y

  def draw(self, surface):
    pg.draw.rect(surface, (255, 0, 255), self)