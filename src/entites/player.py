import pygame as pg

class Player():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def update(self):
    pass

  def draw(self, surface):
    rect = pg.Surface([100, 100])
    rect.fill((255, 255, 255))

    surface.blit(rect, (self.x, self.y))