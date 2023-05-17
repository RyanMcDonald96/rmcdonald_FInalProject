# By Ryan McDonald
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
