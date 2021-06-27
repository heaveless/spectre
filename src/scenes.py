from .common.enums.scene import SceneType

class SceneManager:
  def __init__(self):
      pass


  def __reset(self):
    self.__all_scenes = []
    self.__current_scene = None
    self.__previous_scene = None
    self.__next_scene = None


    self.__initialize_scenes()
    self.__set_starting_scene(SceneType.TITLE)


  def __initialize_scenes(self):
    self.__all_scenes = []
    self.__add_scene()


# class Title():