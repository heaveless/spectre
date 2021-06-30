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
    self.__next_scene = None

    self.__initialize_scenes()
    self.__set_starting_scene(SceneType.LEVEL)

  def __add_scene(self, scene):
    self.__all_scenes.append(scene)

  def __initialize_scenes(self):
    self.__add_scene(Title(self.resources))
    self.__add_scene(Level(self.resources, self.surface))
    self.__add_scene(Boss(self.resources))
    self.__add_scene(GameOver(self.resources))

  def __set_starting_scene(self, scene_type):
    self.__current_scene = self.__all_scenes[int(scene_type)]

  def update(self, delta_time):
    self.__current_scene.update()

  def draw(self, surface):
    self.__current_scene.draw(surface)