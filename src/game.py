import pygame
from .common.enums.game_state import GameState


class Game:
  def __init__(self):
    self.__initialize_pygame()
    self.__setup_window("Spectre", 800, 600)

    self.state = GameState.RUNNING
    self.clock = pygame.time.Clock()
    self.ticks = 0


  def __initialize_pygame(self):
    pygame.mixer.init()
    pygame.init()

  def __setup_window(self, title, width, height):
    pygame.display.set_caption(title)
    pygame.display.set_mode((width, height))

  def quit_game(self):
    self.state = GameState.QUIT

  def update_control(self):
    pass


  def __update(self):
    pass

  def __draw(self):
    if self.state == GameState.QUIT:
      print("terminar todo")
    else: 
      print("se resetea")

    pygame.display.update()


  def run(self):
    while self.state != GameState.QUIT:
      self.__update()
      self.__draw()

    pygame.quit()