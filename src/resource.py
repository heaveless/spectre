import os
import json
import pygame as pg
from .utils.folders_util import Folder

class Resource:
  def __init__(self, path):
    self.path = path

  def load_all_json_maps(self, accept=('.json')):
    jsons = {}

    directory = os.path.join(self.path, Folder.LEVELS)
    for file in os.listdir(directory):
      name, ext = os.path.splitext(file)
      if ext.lower() in accept:
        data = open(os.path.join(directory, file))
        jsons[name] = json.load(data)
    return jsons

  def load_all_image_maps(self, accept=('.png', '.jpg', '.jpeg')):
    images = {}

    directory = os.path.join(self.path, Folder.LEVELS)
    for pic in os.listdir(directory):
      name, ext = os.path.splitext(pic)
      if ext.lower() in accept:
        img = pg.image.load(os.path.join(directory, pic))
        if img.get_alpha():
          img = img.convert_alpha()
        else:
          img = img.convert()
          images[name]=img
    return images

  def load_all_music(self, accept=('.wav', '.mp3', '.ogg', '.ttf')):
      songs = {}

      directory = os.path.join(self.path, Folder.MUSIC)
      for song in os.listdir(directory):
          name,ext = os.path.splitext(song)
          if ext.lower() in accept:
              songs[name] = os.path.join(directory, song)
      return songs
      