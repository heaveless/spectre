import os
import pygame as pg
from .utils.folders_util import Folder

class Resource:
  def __init__(self, path):
    self.path = path

  def __load_all_levels(self, directory, colorkey=(255,0,255), accept=('.png', '.jpg')):
      graphics = {}
      for pic in os.listdir(directory):
          name, ext = os.path.splitext(pic)
          if ext.lower() in accept:
              img = pg.image.load(os.path.join(directory, pic))
              if img.get_alpha():
                  img = img.convert_alpha()
              else:
                  img = img.convert()
                  img.set_colorkey(colorkey)
              graphics[name]=img
      return graphics

  def __load_all_music(self, directory, accept=('.wav', '.mp3', '.ogg', '.ttf')):
      songs = {}
      for song in os.listdir(directory):
          name,ext = os.path.splitext(song)
          if ext.lower() in accept:
              songs[name] = os.path.join(directory, song)
      return songs

  def __load_all_sounds(self, directory, accept=('.wav','.mpe','.ogg')):
    effects = {}
    for fx in os.listdir(directory):
      name, ext = os.path.splitext(fx)
      if ext.lower() in accept:
          effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects

  def __load_all_fonts(self, directory, accept=('.ttf')):
    return self.load_all_music(directory, accept)

  def __load_all_sprites(self, directory, accept=('.png', '.jpg')):
    return self.load_all_levels(directory, accept)

  def get_levels(self):
    return self.__load_all_levels(os.path.join(self.path, Folder.LEVELS))

  def get_music(self):
    return self.__load_all_music(os.path.join(self.path, Folder.MUSIC))

  def get_sounds(self):
    return self.__load_all_sounds(os.path.join(self.path, Folder.SOUNDS))

  def get_fonts(self):
    return self.__load_all_fonts(os.path.join(self.path, Folder.FONTS))
    
  def get_sprites(self):
    return self.__load_all_sprites(os.path.join(self.path, Folder.SPRITES))