# File created by Ryan McDonald
    # Helped by Krisjan Harnish
# import libraries and modules
import pygame as pg
from pygame.sprite import AbstractGroup, Sprite
from random import randint
from math import *
from time import *

# Defining a vector
vec = pg.math.Vector2

# game settings 
WIDTH = 800
HEIGHT = 500
FPS = 30
menuopen = False
# player friction
player_fric = -0.2
# time keeping vars
pt = 0
ct=0
pt2=0
# fire rate
rt=1
# death variables
died = False
cd = False
# score 
score = 0
# wave
wave = 0
restart = False
# game end
won = False
cw = False

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (66, 245, 242)
DARKBLUE = (26, 17, 112)
PINK = (232, 151, 152)
LIGHTGRAY = (212, 212, 212)
GRAY = (128, 128, 128)
DARKGRAY = (77, 77, 77)
PURPLE = (108, 0, 171)
LIME = (151, 255, 107)
LIGHTORANGE = (255, 215, 163)
ORANGE = (237, 134, 0)
GOLD = (168, 149, 50)

# text drawing
def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('calibri')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

# creates the player class and defines its capabilitys 
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30, 30))
        self.image.fill(DARKBLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, 420)
        self.pos = vec(WIDTH/2, 420)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direct = 0
        self.canshoot = False
        self.gt = 0
        self.hp = 200
        self.candamage = True
        
    # gets input for controlls
    def controls(self):
        global rt
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -3
            self.direct = 3            
        if keys[pg.K_d]:
            self.acc.x = 3
            self.direct = 1
        if keys[pg.K_w]:
            self.acc.y = -3  
            self.direct = 0            
        if keys[pg.K_s]:
            self.acc.y = 3
            self.direct = 2  
        if keys[pg.K_SPACE]:
            self.shoot()
        if keys[pg.K_1]:
            self.gt = 0
            rt = 1
        if keys[pg.K_2]:
            self.gt = 1
            rt = 4
        if keys[pg.K_3]:
            self.gt = 2
            rt = 1/2
            
    # moves the player and the visual rect
    def movement(self):
        self.acc += self.vel * player_fric
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
        self.acc = vec(0,0)
    
    # creates a pellet and is using a timer to only fire every after every 0.5 sec at the base rate
    def shoot(self):
        global ct
        global pt
        ct = pg.time.get_ticks()
        if self.canshoot == True and self.gt == 0:
            p = Pellet() 
            all_pellets.add(p)
            all_projectiles.add(p)
            self.canshoot = False
        elif self.canshoot == False:
            if ct - pt > 300/rt:
                self.canshoot = True
                pt = ct
    
            # check to see if player is in bounds

    def boundCheck(self):
        if self.rect.right > 800:
            self.rect.right = 800
            self.vel.x = 0
            self.acc.x = 0
            self.pos = self.rect.center
            self.pos += self.vel + 0.5 * self.acc
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel.x = 0
            self.acc.x = 0
            self.pos = self.rect.center
            self.pos += self.vel + 0.5 * self.acc
        if self.rect.top < 0:
            self.rect.top = 0
            self.vel.y = 0
            self.acc.y = 0
            self.pos = self.rect.center
            self.pos += self.vel + 0.5 * self.acc
        if self.rect.bottom > 500:
            self.rect.bottom = 500
            self.vel.y = 0
            self.acc.y = 0
            self.pos = self.rect.center
            self.pos += self.vel + 0.5 * self.acc

# check to see if player should be dead

    def damageCheck(self):
        global died
        global pt2
        hitsM = pg.sprite.spritecollide(self, all_mobs, False)
        hitsP = pg.sprite.spritecollide(self, all_mobProject, True)
        ct2 = pg.time.get_ticks()
        if hitsM and self.candamage == True:
            self.hp -= 20
            self.candamage = False
            pt2 = ct2

        elif hitsP and self.candamage == True:
            self.hp -= 5
            self.candamage = False
            pt2 = ct2

        elif self.candamage == False:
            if ct2 - pt2 > 800:
                self.candamage = True
                pt2 = ct2
        if self.hp < 1:
            died = True
            self.kill()

# updates player

    def update(self):
        self.controls()
        self.movement()
        self.boundCheck()
        self.damageCheck()
        if self.candamage == True:
            self.image.fill(DARKBLUE)
        else:
            self.image.fill(RED)
        
# creates pellet class


class Pellet(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.direction = player.direct
        if self.direction == 0:
            self.rect.center = (gun.pos.x, gun.pos.y-10)
            self.pos = vec(gun.pos.x, gun.pos.y-10)
        if self.direction == 2:
            self.rect.center = (gun.pos.x, gun.pos.y+10)
            self.pos = vec(gun.pos.x, gun.pos.y+10)
        if self.direction == 1:
            self.rect.center = (gun.pos.x+10, gun.pos.y-5)
            self.pos = vec(gun.pos.x+10, gun.pos.y-5)
        if self.direction == 3:
            self.rect.center = (gun.pos.x, gun.pos.y-5)
            self.pos = vec(gun.pos.x, gun.pos.y-5)
        
        
        
        # moves pellet
    
    def update(self):
        if self.direction == 0:
            self.pos.y -= 20
        if self.direction == 2:
            self.pos.y += 20
        if self.direction == 3:
            self.pos.x -= 20
        if self.direction == 1:
            self.pos.x += 20
        self.rect.center = self.pos
        if(self.pos.y <0):
            self.kill()
        if(self.pos.x <0):
            self.kill()
        if(self.pos.y > 500):
            self.kill()
        if(self.pos.x > 800):
            self.kill()
        
class MobPellet(Sprite):
    def __init__(self, posx, posy):
        Sprite.__init__(self)
        self.image = pg.Surface((7, 7))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.direction = player.direct
        self.rect.center = (posx,posy)
        self.pos = vec(posx,posy)
        if posx > player.pos.x:
            if posy > player.pos.y:
                if posx-player.pos.x > posy-player.pos.y:
                    self.direction = 3
                else:
                    self.direction = 0
            else: 
                if posx-player.pos.x > player.pos.y-posy:
                    self.direction = 3
                else:
                    self.direction = 2
        else:
            if posy > player.pos.y:
                if player.pos.x - posx > posy-player.pos.y:
                    self.direction = 1
                else:
                    self.direction = 0
            else: 
                if player.pos.x-posx > player.pos.y-posy:
                    self.direction = 1
                else:
                    self.direction = 2

        # moves pellet
    
    def update(self):
        if self.direction == 0:
            self.pos.y -= 15
        if self.direction == 2:
            self.pos.y += 15
        if self.direction == 3:
            self.pos.x -= 15
        if self.direction == 1:
            self.pos.x += 15
        self.rect.center = self.pos
        if(self.pos.y <0):
            self.kill()
        if(self.pos.x <0):
            self.kill()
        if(self.pos.y > 500):
            self.kill()
        if(self.pos.x > 800):
            self.kill()

class MobPelletTrack(Sprite):
    def __init__(self, posx, posy):
        Sprite.__init__(self)
        self.image = pg.Surface((8, 8))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (posx,posy)
        self.pos = vec(posx,posy)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.fric = 1.02

        # moves pellet
    
    def update(self):
        self.acc = vec(0,0)
        self.vel = self.vel/self.fric
        
        if self.pos.x > player.pos.x:
            self.acc.x -= 1.5
        else:
            self.acc.x += 1.5
        if self.pos.y > player.pos.y:
            self.acc.y -= 1.5
        else:
            self.acc.y+= 1.5

        self.vel += self.acc
        self.pos += self.vel

        self.rect.center = self.pos
        if(self.pos.y <0):
            self.kill()
        if(self.pos.x <0):
            self.kill()
        if(self.pos.y > 500):
            self.kill()
        if(self.pos.x > 800):
            self.kill()

        
# creates rect to be a visual gun
class Gun(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((15, 25))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (player.pos.x, player.pos.y-25)
        self.pos = vec(player.pos.x, player.pos.y-25)
        self.direction = player.direct

        
            # moves gun to player position and roatates to match direction

    def update(self):
        self.direction = player.direct
        self.pos = vec(player.pos.x, player.pos.y-25)
        self.rect.center = self.pos
        if self.direction == 0 or self.direction == 2:
            self.image = pg.Surface((15, 25))
            if self.direction == 0:
                self.rect.center = (player.pos.x, player.pos.y-25)
                self.pos = vec(player.pos.x, player.pos.y-25)
            else:
                self.rect.center = (player.pos.x, player.pos.y+25)
                self.pos = vec(player.pos.x, player.pos.y+25)
            
        else:
            self.image = pg.Surface((25, 15))
            if self.direction == 1:
                self.rect.center = (player.pos.x+20, player.pos.y+5)
                self.pos = vec(player.pos.x+20, player.pos.y+5)
            else:
                self.rect.center = (player.pos.x-30, player.pos.y+5)
                self.pos = vec(player.pos.x-30, player.pos.y+5)
        if player.gt == 0:
            self.image.fill(BLACK)
        elif player.gt == 1:
            self.image.fill(PURPLE)
        elif player.gt == 2:
            self.image.fill(ORANGE)

class Streaker(Sprite):
    def __init__(self,posx,posy):
        Sprite.__init__(self)
        self.image = pg.Surface((25, 25))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.center = (posx,posy)
        self.pos = vec(posx,posy)
        self.attacking = False
        self.hitBottom = False
        self.point =  vec(randint(25,775),randint(25,475))
        self.hitpoint = vec(0,0)
        self.hp = 25


        # movement for mob a to keep it in bounds and move randomly on y but still restrainded

    def movement(self):
        if self.point.x-6 > self.pos.x:
            self.pos.x += 5
            self.rect.center = self.pos

        elif self.point.x+6 < self.pos.x:
            self.pos.x -= 5
            self.rect.center = self.pos
        else:
            self.hitpoint.x = 1

        if self.point.y-6 > self.pos.y:
            self.pos.y += 5
            self.rect.center = self.pos   
        elif self.point.y+6 < self.pos.y:
            self.pos.y -= 5
            self.rect.center = self.pos
        else:
            self.hitpoint.y = 1
    
    def redirect(self):
        self.point = vec(randint(25,775),randint(25,475))
        self.hitpoint = vec(0,0)


    def damage(self,type):
        global score
        if type == 1:
            self.hp -= 10
            brighten = 10*5
        if type == 2:
            self.hp -= 3
            brighten = 3*5
        if type == 3:
            self.hp -=8
            brighten = 8*5
        self.image.fill((brighten, brighten, brighten), special_flags=pg.BLEND_RGB_ADD)
        if self.hp < 1:
            score += 10
            self.kill()

    def shoot(self):
        p = MobPellet(self.pos.x, self.pos.y) 
        all_mobProject.add(p)
    
# updates and switches between attack and movemnt states

    def update(self):
        self.movement()
        if self.hitpoint == (1,1):
            self.shoot()
            self.redirect()
        hitsp = pg.sprite.spritecollide(self, all_pellets, True)
        hitsl = pg.sprite.spritecollide(self, all_lasers, True)
        hitss = pg.sprite.spritecollide(self, all_shells, True)
        if hitsp:
           self.damage(1)
        if hitsl:
           self.damage(2)
        if hitss:
           self.damage(3)

# creates the screen for menues
class Menu(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.type = 2

    def restart(self):
        global wave
        global score
        global died
        global player
        global gun
        wave = 10
        for x in all_mobs:
            x.kill()
        for x in all_mobProject:
            x.kill()
        for x in all_projectiles:
            x.kill()
        score = 0
        x = Streaker(50,50)
        all_mobs.add(x)
        player = Player()
        gun = Gun()
        all_players.add(player)
        all_players.add(gun)
        all_sprites.add(all_players)
        all_sprites.add(all_mobs)
        self.type = 0 

    def update(self):
        if self.type == 2: 
            screen.fill(DARKBLUE) 
            draw_text('Infinite Shooter',90,GOLD,400,180)
            draw_text('By Ryan McDonald: ', 30, WHITE, 400, 260)
            draw_text('Press K to Start', 50, GREEN, 400, 300)
            keys = pg.key.get_pressed()
            if keys[pg.K_k]:
                self.restart()
        
# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Shooter")
clock = pg.time.Clock()

# create a group for all sprites
all_players = pg.sprite.Group()
all_sprites = pg.sprite.Group()
all_mobs = pg.sprite.Group()
all_mobProject = pg.sprite.Group()
all_projectiles = pg.sprite.Group()
all_pellets = pg.sprite.Group()
all_lasers = pg.sprite.Group()
all_shells = pg.sprite.Group()

# init player

menu = Menu()

# add items to groups
# add groups to groups

all_sprites.add(all_players)
all_sprites.add(all_projectiles) 
all_sprites.add(all_mobs)

# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False

# wave system

    if len(all_mobs.sprites()) < 1:
        if wave == 1:
            wave = 2
            for x in range(3):
                x = Streaker(randint(0,700), randint(10,100))
                all_mobs.add(x)
            all_sprites.add(all_mobs)
            if rand == 0:
                for x in range(1):
                    x = Streaker(randint(0,700), randint(10,100))
                    all_mobs.add(x)
            elif rand == 1:
                for x in range(2):
                    x = Streaker(randint(0,700), randint(10,100))
                    all_mobs.add(x)
            rand = randint(0,2)
            
############ Update ##############
# update all sprites

    all_sprites.update()
    all_projectiles.update()
    all_mobProject.update()

# updateing the objects
    
    ############ Draw ################
    # draw the background screen
    screen.fill(DARKGRAY)
    # draw all sprites
    all_sprites.draw(screen)
    all_projectiles.draw(screen)
    all_mobProject.draw(screen)

    # draw text
    if menu.type == 0:
        draw_text('Health: '+ str(player.hp),20,RED,60,20)
        draw_text('Wave: ' + str(wave), 20, WHITE, 60, 40)
        draw_text('Score: ' + str(score), 20, GREEN, 60, 60)
    
    # check menu
    if died == True:
        menu.type = 1
    menu.update()

    # buffer - after drawing everything, flip display
    
    pg.display.flip()

pg.quit()