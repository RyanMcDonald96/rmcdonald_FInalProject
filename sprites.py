# By Ryan McDonald

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
        

class Laser(Sprite):
        def __init__(self):
            Sprite.__init__(self)
            self.image = pg.Surface((7, 7))
            self.image.fill(LIGHTBLUE)
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

class Shotgun(Sprite):
    def __init__(self, offset):
        Sprite.__init__(self)
        self.image = pg.Surface((8, 8))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.direction = player.direct
        if self.direction == 0:
            self.rect.center = (gun.pos.x+offset, gun.pos.y-10)
            self.pos = vec(gun.pos.x, gun.pos.y-10)
        if self.direction == 2:
            self.rect.center = (gun.pos.x+offset, gun.pos.y+10)
            self.pos = vec(gun.pos.x, gun.pos.y+10)
        if self.direction == 1:
            self.rect.center = (gun.pos.x+10, gun.pos.y-5+offset)
            self.pos = vec(gun.pos.x+10, gun.pos.y-5)
        if self.direction == 3:
            self.rect.center = (gun.pos.x, gun.pos.y-5+offset)
            self.pos = vec(gun.pos.x, gun.pos.y-5)

        
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

class Gun(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((15, 25))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (player.pos.x, player.pos.y-25)
        self.pos = vec(player.pos.x, player.pos.y-25)
        self.direction = player.direct

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


class Spawner(Sprite):
    def __init__(self,posx,posy):
        Sprite.__init__(self)
        self.image = pg.Surface((40, 40))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (posx,posy)
        self.pos = vec(posx,posy)
        self.attacking = False
        self.hitBottom = False
        self.point =  vec(randint(25,775),randint(25,475))
        self.hitpoint = vec(0,0)
        self.hp = 50

        class Bouncer(Sprite):
    def __init__(self,posx,posy):
        Sprite.__init__(self)
        self.image = pg.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (posx,posy)
        self.pos = vec(posx,posy)
        self.attacking = False
        self.hitBottom = False
        self.dir = vec(randint(1,2), randint(1,2))
        self.hp = 40



class Tracker(Sprite):
    def __init__(self,posx,posy):
        Sprite.__init__(self)
        self.image = pg.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (posx,posy)
        self.pos = vec(posx,posy)
        self.attacking = False
        self.hitBottom = False
        self.point =  vec(randint(25,775),randint(25,475))
        self.hitpoint = vec(0,0)
        self.hp = 20

class Bull(Sprite):
    def __init__(self,posx,posy):
        Sprite.__init__(self)
        self.image = pg.Surface((60, 60))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        self.rect.center = (posx,posy)
        self.pos = vec(posx,posy)
        self.attacking = False
        self.hitBottom = False
        self.hp = 75
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.fric = 1.05

class Health(Sprite):
    def __init__(self,posx,posy):
        Sprite.__init__(self)
        self.image = pg.Surface((15, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (posx,posy)
        self.pos = vec(posx,posy)
        self.dir = vec(randint(1,2), randint(1,2))
    
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

        all_players = pg.sprite.Group()
all_sprites = pg.sprite.Group()
all_mobs = pg.sprite.Group()
all_mobProject = pg.sprite.Group()
all_projectiles = pg.sprite.Group()
all_pellets = pg.sprite.Group()
all_lasers = pg.sprite.Group()
all_shells = pg.sprite.Group()
