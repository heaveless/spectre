from .scenes_manager import SceneManager
from .resource import Resource
from .constants import FPS, HEIGHT, TITLE, WIDTH, BLACK
import pygame as pg
import os

class Game:
  def __init__(self) -> None:
    self.__initialize_pygame()
    self.__setup_screen()

    self.clock = pg.time.Clock()
    self.running = True

    self.sources = self.__load_resouces()
    self.scene_manger = SceneManager(self.sources)

  def __initialize_pygame(self):
    pg.mixer.init()
    pg.init()

  def __setup_screen(self):
    self.screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)

  def __load_resouces(self):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return Resource(os.path.join(root_dir, "assets"))

  def __update_events(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        self.running = False

  def __update(self):
    self.scene_manger.update()
    self.__update_events()

  def __draw(self):
    self.scene_manger.draw(self.screen)
    pg.display.update()
    # pg.display.flip()

  def run(self):
    while self.running:
      self.clock.tick(FPS)
      self.__update()
      self.__draw()