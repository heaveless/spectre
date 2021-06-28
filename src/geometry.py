from .utils.colors_util import Color
from .common.base.geometry_base import GeometryBase

class Shape(GeometryBase):
  def __init__(self, x, y, width, height, color):
    GeometryBase.__init__(self, x, y, width, height)
    self.color = color

class Rectangle(Shape):
  def __init__(self, x, y, width, height, color = Color.WHITE):
    Shape.__init__(self, x, y, width, height)
    