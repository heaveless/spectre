import pygame as pg
from ..constants import (YELLOW, WIDTH, HEIGHT, GRAVITY, ACCELERATION, FRICTION)

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.hits = None

    def jump(self):
        self.rect.x += 1
        self.rect.x -= 1
        if self.hits:
            self.vel.y = -20

    def set_hits(self, hits):
        self.hits = hits

    def update(self):
        self.acc = vec(0, GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -ACCELERATION
        if keys[pg.K_d]:
            self.acc.x = ACCELERATION
        if keys[pg.K_w]:
            self.jump()

        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos
