import pygame
import os
from .resource import Resource
from .scenes_manager import SceneManager
from .common.enums.game_state import GameState


class Game:
  def __init__(self):
    self.__initialize_pygame()
    self.__setup_window("Spectre", 800, 600)

    self.state = GameState.RUNNING
    self.clock = pygame.time.Clock()

    root_dir = os.path.dirname(os.path.abspath(__file__))
    resources = Resource(os.path.join(root_dir, "assets"))
    self.scene_manger = SceneManager(resources)

  def __initialize_pygame(self):
    pygame.mixer.init()
    pygame.init()

  def __setup_window(self, title, width, height):
    pygame.display.set_caption(title)
    self.window = pygame.display.set_mode((width, height))

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
      self.scene_manger.draw(self.window)

    pygame.display.update()


  def run(self):
    while self.state != GameState.QUIT:
      self.__update()
      self.__draw()

    pygame.quit()