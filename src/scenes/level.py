from ..constants import HEIGHT
from src.components.portal import Portal
import pygame as pg

from ..components.plataform import Platform
from ..components.player import Player

class Level():
  def __init__(self, sources):
    self.sources = sources
    self.json_maps = sources.load_all_json_maps()
    self.image_maps = sources.load_all_image_maps()
    
    self.all_sprites = pg.sprite.Group()
    self.platforms = pg.sprite.Group()
    self.portals = pg.sprite.Group()

    self.__load_level()
    self.__load_hero()
    self.__load_portal()

  def __reset(self):
    for plataform in self.platforms:
      plataform.kill()

  def __check_fail(self):
    if self.player.rect.y >= HEIGHT:
      self.__load_level(self.curret_level_index)
      self.__load_hero()

  def __load_level(self, level = 0):
    index = str(level)
    self.curret_level_index = level
    self.current_level = self.json_maps[index]
    self.current_background = self.image_maps[index]

  def __load_hero(self):
    start = self.current_level["start"]
    self.player = Player(start["x"], start["y"], self.sources)
    self.all_sprites.add(self.player)
  
  def __load_portal(self):
    end = self.current_level["end"]
    self.portal = Portal(end["x"], end["y"], end["width"], end["height"])
    self.portals.add(self.portal)

  def __complete_level(self):
     hits = pg.sprite.spritecollide(self.player, self.portals, False)
     if hits:
       self.__reset()
       self.__load_level(self.curret_level_index + 1)
       self.__load_hero()

  def update(self):
    self.player.rect.x += 1
    hits = pg.sprite.spritecollide(self.player, self.platforms, False)
    self.player.rect.x -= 1
    self.player.set_hits(hits)
    
    self.__complete_level()
    self.player.update()

    self.all_sprites.update()
    if self.player.vel.y > 0 and hits:
      self.player.pos.y = hits[0].rect.top
      self.player.vel.y = 0

    self.__check_fail()

  def draw(self, surface):
    for layer in self.current_level["layers"]:
      plataform = Platform(layer["x"], layer["y"], layer["width"], layer["height"])
      self.all_sprites.add(plataform)
      self.platforms.add(plataform)

    surface.blit(self.current_background, (0, 0))
    self.all_sprites.draw(surface)