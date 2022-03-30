import os
import pygame as pg
from . import settings
from . import constants as c

OG_CAPTION = c.OG_CAPTION

os.environ['SDL_VIDEO_CENTERED'] = '1'

pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(c.OG_CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

FONTS = settings.load_fonts(os.path.join("resources", "fonts"))
MUSIC = settings.load_music(os.path.join("resources","music"))
GFX = settings.load_gfx(os.path.join("resources","graphics"))
SFX = settings.load_sfx(os.path.join("resources","sound"))