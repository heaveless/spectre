import pygame as pg

from ..common.enums.direction_type import DirectionType

class Player(pg.Rect):
  def __init__(self, x, y, width, height):
    pg.Rect.__init__(self, x, y, width, height)
    
    self.center = (800 / 2, 600 / 2)
    self.position = pg.Vector2(800 / 2, 600 / 2)
    self.velocity = pg.Vector2(0, 0)
    self.acceleration = pg.Vector2(0, 0)

    def __jump(self):
      self.x += 1
      hits = self.hits
      self.x -= 1
      if hits:
        self.velocity.y = -20










  def __pressed(self):
    self.acceleration = pg.Vector2(0, 0.8)
    keys = pg.key.get_pressed()
      # self.__run(DirectionType.RIGHT)
    if keys[pg.K_a]:
      self.acceleration.x = 0.5
    if keys[pg.K_d]:
      self.acceleration.x = -0.5
      # self.__run(DirectionType.LEFT)
    if keys[pg.K_w]:
      self.__jump()

    # self.set_location(self.x, self.y)
      # self.__vertical_movement(DirectionType.UP)


  # def __run(self, type):
  #   if type == DirectionType.RIGHT:
  #     self.x += self.velocity.x  
  #   elif type == DirectionType.LEFT:
  #     self.x -= self.velocity.x

  # def __gravity(self):
  #   self.velocity.y += self.gravity
  #   self.set_location(self.x, self.y + self.velocity.y)

  # def __vertical_movement(self, type):
  #   self.velocity.y += self.gravity 
  #   if type == DirectionType.UP:
  #     if self.velocity.y < 8:
  #       self.velocity.y += 6
  #       self.set_location(self.x, self.y - self.velocity.y)
  #     else:
  #       self.__gravity()
    

  def __jump(self):
    if self.is_jumping:
      self.velocity.y = 100
    self.is_jumping = False

    self.y += self.velocity.y
    self.velocity.y -= self.gravity
    print(self.y, self.velocity.y)

  # def __velocity(self, is_collision):
  #   self.velocity.y += self.gravity

  #   if len(is_collision):
  #     self.velocity.y = 0

  #   self.y += self.velocity.y

  # def collision(self, is_collision):
  #   self.__velocity(is_collision)






  def update(self, hits):
    self.hits = hits

    self.__pressed()
    
    self.acceleration.x = self.velocity.x * -0.12
    self.velocity += self.acceleration
    self.position += self.velocity + 0.5 * self.acceleration

    if self.position.x > 800:
      self.position.x = 0
    if self.position.x < 0:
      self.position.x = 800

    self.midbottom = self.position


  # def set_location(self, x, y):
  #   self.x = x
  #   self.y = y

  def draw(self, surface):
    pg.draw.rect(surface, (255, 0, 255), self)