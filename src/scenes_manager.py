from .constants import LEVELS_INDEX
from .scenes.level import Level

class SceneManager:
  def __init__(self, sources):
    self.sources = sources
    self.__reset()

  def __reset(self):
    self.__all_scenes = []
    self.__current_scene = None

    self.__initialize_scenes()
    self.__set_starting_scene(LEVELS_INDEX)

  def __add_scene(self, scene):
    self.__all_scenes.append(scene)

  def __initialize_scenes(self):
    self.__add_scene(Level(self.sources))

  def __set_starting_scene(self, scene_type):
    self.__current_scene = self.__all_scenes[int(scene_type)]

  def update(self):
    self.__current_scene.update()

  def draw(self, surface):
    self.__current_scene.draw(surface)