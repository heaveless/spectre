import pygame as pg
import os
from .resource import Resource
from .scenes_manager import SceneManager
from .common.enums.game_state import GameState
from .utils.colors_util import Color
from .entites.player import Player
from .config.game import SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
  def __init__(self):
    self.__initialize_pygame()
    self.__setup_window("Spectre", SCREEN_WIDTH, SCREEN_HEIGHT, 60)

    self.state = GameState.RUNNING
    self.clock = pg.time.Clock()
    self.current_time = 0, 0
    self.last_time = 0
    self.delta_time = 0
    self.ticks = 0

    root_dir = os.path.dirname(os.path.abspath(__file__))
    resources = Resource(os.path.join(root_dir, "assets"))
    self.scene_manger = SceneManager(resources, self.window)

    self.player = Player()

  def __initialize_pygame(self):
    pg.mixer.init()
    pg.init()

  def __setup_window(self, title, width, height, target_fps):
    self.target_fps = target_fps
    pg.display.set_caption(title)
    self.window = pg.display.set_mode((width, height))

  def __quit_game(self):
    self.state = GameState.QUIT

  def __calculate_delta_time(self):
    self.clock.tick(self.target_fps)
    self.delta_time = (pg.time.get_ticks() - self.ticks) / 1000.0
    self.ticks = pg.time.get_ticks()

  def __calculate_time(self):
    self.current_time = pg.time.get_ticks() - self.last_time

  def __update_control(self):
    pass

  def __update_events(self):
    for event in pg.event.get():    
      if event.type == pg.QUIT:
        self.__quit_game()

  def __clear_screen(self, color = Color.BLACK):
    self.window.fill(color)

  def __update(self):
    self.__calculate_delta_time()
    self.__calculate_time()
    self.scene_manger.update(self.delta_time, self.current_time)
    self.__update_events()

  def __draw(self):
    self.__clear_screen()
    self.scene_manger.draw(self.window)

    pg.display.update()


  def run(self):
    while self.state != GameState.QUIT:
      self.__update()
      self.__draw()

    pg.quit()