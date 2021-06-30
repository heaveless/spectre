class SceneBase:
  def __init__(self):
      pass

  def complete(self, cb):
    cb(None)
    
  def update(self):
    pass

  def draw(self, surface):
    pass