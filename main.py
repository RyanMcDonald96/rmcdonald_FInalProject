# File created by Ryan McDonald
# import libraries and modules

import pygame as pg
from pygame.sprite import Sprite
from random import randint

vec = pg.math.Vector2

# game settings
WIDTH = 800
HEIGHT = 500
FPS = 30

# level set
levelOn = (0,0)

# Player settings
player_fric = -0.2
player_grav = 3
gravOn = True

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKBLUE = (26, 17, 112)
PINK = (232, 151, 152)
LIGHTGRAY = (212, 212, 212)
GRAY = (128, 128, 128)
DARKGRAY = (77, 77, 77)
PURPLE = (108, 0, 171)
LIME = (151, 255, 107)
LIGHTORANGE = (255, 215, 163)
ORANGE = (237, 134, 0)


# sprites

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = 1
        self.hitx = 0
        self.hity = 0
        self.canJump = False
    def jump(self):
        if(self.canJump==True):
            self.acc.y=-50
            self.canJump = False
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
            direction = -1 
        if keys[pg.K_d]:
            self.acc.x = 5
            direction = 1
        if keys[pg.K_SPACE]:
            self.jump()
    def collision_test(self,plats):
        collisions = []
        for plat in plats:
            if self.rect.colliderect(plat):
                collisions.append(plat)
                return(collisions)
    

# buffer - after drawing everything, flip display
pg.display.flip()
pg.quit()







