import pygame as pg

class Title():
  def __init__(self, resources):
    pass

  def update(self, delta_time):
    pass
    # super().update(delta_time)

  def draw(self, surface):
    rect = pg.Surface([100, 100])
    rect.fill((255, 255, 255))

    surface.blit(rect, (10, 10))