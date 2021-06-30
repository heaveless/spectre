from .scenes.boss import Boss
from .scenes.gameover import GameOver
from .scenes.level import Level
from .scenes.title import Title
from .common.enums.scene_type import SceneType

class SceneManager:
  def __init__(self, resources, surface):
    self.resources = resources
    self.surface = surface
    self.__reset()

  def __reset(self):
    self.__all_scenes = []
    self.__current_scene = None
    self.__previous_scene = None
    self.__current_scene_type = SceneType.TITLE

    self.__initialize_scenes()
    self.__set_starting_scene()

  def __add_scene(self, scene):
    self.__all_scenes.append(scene)

  def __initialize_scenes(self):
    self.__add_scene(Title)
    self.__add_scene(Level)
    self.__add_scene(Boss)
    self.__add_scene(GameOver)

  def __set_starting_scene(self):
    current_class = self.__all_scenes[int(self.__current_scene_type)]
    self.__current_scene = current_class(self.resources)

  def __update_scene_type(self, scene_type):
    self.__current_scene_type = scene_type

  def __update_scene(self, scene_type):
    if scene_type:
      self.__update_scene_type(scene_type)
      self.__set_starting_scene()

  def update(self, delta_time, time):
    self.__current_scene.update(delta_time, time)
    self.__current_scene.complete(self.__update_scene)

  def draw(self, surface):
    self.__current_scene.draw(surface)