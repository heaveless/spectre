import pygame
from .utils.colors import Color

def scale_value(value):
  return value

def draw_rectangle(surface, rect, color = Color.WHITE):
  pygame.draw.rect(surface, color, (
    rect.x,
    rect.y,
    rect.width,
    rect.height
  ))

def draw_image(surface, image, rect):
  surface.blit(image, (rect.x, rect.y))
