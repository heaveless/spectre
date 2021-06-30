import pygame as pg
from ..config.game import SCREEN_WIDTH, SCREEN_HEIGHT
from ..common.base.scene_base import SceneBase
from ..common.enums.scene_type import SceneType
from ..utils.colors_util import Color
class Title(SceneBase):
  def __init__(self, resources):
    SceneBase.__init__(self)
    self.is_complete = False
    self.stay_time = 3

    self.__initialize()

  def __initialize(self):
    font = pg.font.Font(None, 25)
    self.screen = font.render("Start Game", True, Color.WHITE)

  def complete(self, cb):
    if self.is_complete:
      cb(SceneType.LEVEL)

  def update(self, delta_time, time):
    seconds = time[1]
    if seconds > self.stay_time:
      self.is_complete = True

  def draw(self, surface):
    text_rect = self.screen.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    surface.blit(self.screen, text_rect)