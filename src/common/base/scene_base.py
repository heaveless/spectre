class SceneBase:
  def __init__(self):
      pass

  def complete(self, cb):
    cb(None)
    
  def update(self, delta_time, time):
    pass

  def draw(self, surface):
    pass