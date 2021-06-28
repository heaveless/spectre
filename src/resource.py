import os
import json
from src.constants import LEVELS
import pygame as pg

class Resource:
  def __init__(self, base_path):
    self.base_path = base_path

  def load_all_json_maps(self, accept=('.json')):
    jsons = {}

    directory = os.path.join(self.base_path, LEVELS)
    for file in os.listdir(directory):
      name, ext = os.path.splitext(file)
      if ext.lower() in accept:
        data = open(os.path.join(directory, file))
        jsons[name] = json.load(data)
    return jsons

  def load_all_image_maps(self, accept=('.png', '.jpg', '.jpeg')):
    images = {}

    directory = os.path.join(self.base_path, LEVELS)
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

