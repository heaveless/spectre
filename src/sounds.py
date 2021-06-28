import os
from pygame.mixer import Sound, music


class SoundControl:
  def __init__(self, music_path, sound_path):
    self.music_path = music_path
    self.sound_path = sound_path

  def play_music(self, name, volume = 0.5):
    if name != self.current:
      path = os.path.join(self.music_path, name)
      music.load(path)
      music.set_volume(volume)
      music.play()

      self.current = name

  def play_sound(self, name, volume = 0.5):
    path = os.path.join(self.sound_path, name)
    sound = Sound(path)
    sound.set_volume(volume)
    sound.play()