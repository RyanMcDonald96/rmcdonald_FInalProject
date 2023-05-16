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
    def movement(self, plats):
        self.acc = vec(0,player_grav)
        self.controls()
        self.acc.x += self.vel.x * player_fric
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + 0.5 * self.acc.x
        self.rect.centerx = self.pos.x
        collisions = self.collision_test(plats)
        for plat in collisions:
            if self.vel.x>0:
                self.rect.right = plat.rect.left
                self.acc.x = 0
                self.vel.x = 0
                self.pos = self.rect.center
                self.pos += self.vel + 0.5 * self.acc
                if self.vel.x<0:
                    self.rect.left = plat.rect.right
                    self.acc.x = 0
                    self.vel.x = 0
                    self.pos = self.rect.center
                    self.pos += self.vel + 0.5 * self.acc
                    self.acc.y += self.vel.y * player_fric
                    self.vel.y += self.acc.y
                    self.pos.y += self.vel.y + 0.5 * self.acc.y
                    self.rect.centery = self.pos.y
                    collisions = self.collision_test(plats)
        for plat in collisions:
            if self.vel.y>0:
                self.rect.bottom = plat.rect.top
                self.acc.y = 0
                self.vel.y = 0
                self.pos = self.rect.center
                self.pos += self.vel + 0.5 * self.acc
                self.canJump = True
            if self.vel.y<0:
                self.rect.top = plat.rect.bottom
                self.acc.y = 0
                self.vel.y = 0
                self.pos = self.rect.center
                self.pos += self.vel + 0.5 * self.acc
    def update(self):
        self.movement(all_platforms)
        print(self.canJump)

class Platform(Sprite):
    def __init__(self,x,y,w,h,color):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


# init pygame and create a window

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()


# create a group for all sprites

all_players = pg.sprite.Group()
borders_and_doors = pg.sprite.Group()
all_platforms = pg.sprite.Group()
mobs = pg.sprite.Group()
level_0_0 = pg.sprite.Group()

# instantiate the player class
player = Player()


# init borders and doors
rightWall = Platform(0,0,20,500,GRAY)
leftWall = Platform(780,0,20,500,GRAY)
floor = Platform(0,480,800,20,GRAY)
ceiling = Platform(0,0,800,20,GRAY)
block = Platform(350,100,50,50,LIGHTORANGE)

# Add Sprites to groups
all_players.add(player)
borders_and_doors.add(rightWall)
borders_and_doors.add(leftWall)
borders_and_doors.add(floor)
borders_and_doors.add(ceiling)
borders_and_doors.add(block)
all_platforms.add(borders_and_doors)


# Game loop

running = True

while running:
    clock.tick(FPS)
for event in pg.event.get():
    if event.type == pg.QUIT:
        running = False






############ Update ##############
# update all sprites
    all_players.update()
    all_platforms.update()




############ Draw ################

# draw the background screen
    screen.fill(DARKBLUE)

# draw all sprites
    borders_and_doors.draw(screen)
    all_players.draw(screen)
    if(levelOn == (0,0)):
        level_0_0.draw(screen)

# buffer - after drawing everything, flip display
pg.display.flip()
pg.quit()







