import pygame as pg
from ..config.game import SCREEN_WIDTH, SCREEN_HEIGHT
from ..common.base.scene_base import SceneBase
from ..utils.colors_util import Color
class GameOver(SceneBase):
  def __init__(self, resources):
    SceneBase.__init__(self)
    self.__initialize()

  def __initialize(self):
    font = pg.font.Font(None, 25)
    self.screen = font.render("You win!", True, Color.WHITE)

  def draw(self, surface):
    text_rect = self.screen.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    surface.blit(self.screen, text_rect)