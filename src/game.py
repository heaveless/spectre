import pygame
import os
from .resource import Resource
from .scenes_manager import SceneManager
from .common.enums.game_state import GameState
from .utils.colors_util import Color

class Game:
  def __init__(self):
    self.__initialize_pygame()
    self.__setup_window("Spectre", 800, 600, 60)

    self.state = GameState.RUNNING
    self.clock = pygame.time.Clock()
    self.delta_time = 0
    self.ticks = 0

    root_dir = os.path.dirname(os.path.abspath(__file__))
    resources = Resource(os.path.join(root_dir, "assets"))
    self.scene_manger = SceneManager(resources)

  def __initialize_pygame(self):
    pygame.mixer.init()
    pygame.init()

  def __setup_window(self, title, width, height, target_fps):
    self.target_fps = target_fps
    pygame.display.set_caption(title)
    self.window = pygame.display.set_mode((width, height))

  def quit_game(self):
    self.state = GameState.QUIT

  '''  sfssdfsdfsdfsd '''

  def __calculate_delta_time(self):
    self.clock.tick(self.target_fps)
    self.delta_time = (pygame.time.get_ticks() - self.ticks) / 1000.0
    self.ticks = pygame.time.get_ticks()

  def __update_control(self):
    pass

  def __clear_screen(self, color = Color.BLACK):
    self.window.fill(color)

  def __update(self):
    self.__calculate_delta_time()
    self.scene_manger.update(self.delta_time)

  def __draw(self):
    self.__clear_screen()
    self.scene_manger.draw(self.window)

    pygame.display.update()


  def run(self):
    while self.state != GameState.QUIT:
      self.__update()
      self.__draw()

    pygame.quit()