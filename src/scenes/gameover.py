import pygame as pg
from ..config.game import SCREEN_WIDTH, SCREEN_HEIGHT
from ..common.base.scene_base import SceneBase
from ..utils.colors_util import Color
class GameOver(SceneBase):
  def __init__(self, resources):
    SceneBase.__init__(self)
    self.music = resources.load_all_music()
    self.current_second = -1
    self.current_global_second = 0
    self.__set_text("")
    self.__initialize()
    self.__play_music()

  def __initialize(self):
    self.message = {}
    words = [
      "Thank you,",
      "I'll say goodbye soon",
      "Though its the end of the world,",
      "Don't blame yourself now",
      "And if its true,",
      "I will surround you",
      "and give life to a world",
      "That's our own.",
      ""
    ]
    self.keys = ('0', '3', '7', '10', '14', '18', '21', '26', '29')
    for key in self.keys:
      index = self.keys.index(key)
      self.message[key] = words[index]


  def __set_subtitle(self, string_index):
    if string_index in self.keys:
      word = self.message[string_index]
      self.__set_text(word)

  def __set_text(self, text):
    font = pg.font.Font(None, 25)
    self.text = font.render(text, True, Color.WHITE)

  def __play_music(self):
    pg.mixer.music.load(self.music["thank-you"])
    pg.mixer.music.set_volume(0.3)
    pg.mixer.music.play()

  def update(self, delta_time, time):
    if self.current_global_second < time[1]:
      self.current_global_second = time[1]
      self.current_second += 1

  def draw(self, surface):
    self.__set_subtitle(str(self.current_second))
    text_rect = self.text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    surface.blit(self.text, text_rect)
