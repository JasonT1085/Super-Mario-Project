SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

OG_CAPTION = "Super Mario Bros"

GRAY         = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
WHITE        = (255, 255, 255)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK    = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215,   0)

BGCOLOR = WHITE

SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62


#Mario Movement
WALK_ACCEL = 0.15
RUN_ACCEL = .20
SMALL_TURNAROUND = 0.35

GRAVITY = 1.01
JUMP_GRAVITY = .31
JUMP_VEL = -10.25
FAST_JUMP_VEL = -12.5
MAX_Y_VEL = 11

MAX_RUN_SPEED = 7
MAX_WALK_SPEED = 6

#Mario Animation States
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'
WALKING_TO_CASTLE = 'walking to castle'
END_OF_LEVEL_FALL = 'end of level fall'
SLIDEPIPE = 'sliding into pipe'
SLIDEUGPIPE = 'sliding into UGpipe'
SLIDEOUTOFPIPE = 'slidingoutofpipe'
##ENEMIES##

#UNDERGROUND
STONE = 'stone'
BRICK = 'brick'
UGCOIN = 'UGCOIN'
BLOCKSIZE = 32

#Goomba
LEFT = 'left'
RIGHT = 'right'
GHURT = 'ghurt'
GDEATH = 'gdeath'

#Koopa
KSLIDE = 'kslide'

#BRICKS
REST = 'rest'
BUMPED = 'bumped'

#COINS
GAINED = 'gained'

#MUSHROOM ANIMATION STATES
MSPAWN = 'mspawn'
MSLIDE = 'mslide'

#COIN Animation State
SPIN = 'spin'

#Star Animation State

SBOUNCE = 'bounce'

#FIRE Animation States

INAIR = 'inair'
FBOUNCE = 'fbounce'
FCOLLIDE = 'fcollide'

#Brick and coin box contents

MUSHROOM = 'mushroom'
STAR = 'star'
FIREFLOWER = 'fireflower'
SIXCOINS = '6coins'
COIN = 'coin'
LIFE_MUSHROOM = '1up_mushroom'

FIREBALL = 'fireball'

#ENEMY LISTS

GOOMBA = 'goomba'
KOOPA = 'koopa'

#LEVEL STATES
FROZEN = 'frozen'
NOT_FROZEN = 'not frozen'
IN_CASTLE = 'in castle'
FLAG_AND_FIREWORKS = 'flag and fireworks'

#FLAG STATES
TOP_OF_POLE = 'top of pole'
SLIDE_DOWN = 'slide down'
BOTTOM_OF_POLE = 'bottom of pole'

#1UP SCORE
ONEUP = '379'

#MAIN MENU STATES
PLAYER1 = '1 player'
PLAYER2 = '2 player'

#UI INFO STATES
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'loading screen'
LEVEL = 'level'
GAME_OVER = 'game over'
FAST_COUNT_DOWN = 'fast count down'
END_OF_LEVEL = 'end of level'

#GAME INFO DICTIONARY KEYS
COIN_TOTAL = 'coin total'
SCORE = 'score'
TOP_SCORE = 'top score'
LIVES = 'lives'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
CAMERA_START_X = 'camera start x'
MARIO_DEAD = 'mario dead'

#STATES FOR ENTIRE GAME
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL1 = 'level1'

#SOUND STATES
NORMAL = 'normal'
STAGE_CLEAR = 'stage clear'
WORLD_CLEAR = 'world clear'
TIME_WARNING = 'time warning'
SPED_UP_NORMAL = 'sped up normal'
MARIO_INVINCIBLE = 'mario invincible'
