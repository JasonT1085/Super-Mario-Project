import os
import pygame as pg

keybinds = {
    'action':pg.K_LSHIFT,
    'jump': pg.K_SPACE,
    'left': pg.K_LEFT,
    'right': pg.K_RIGHT,
    'down': pg.K_DOWN
}
class Control(object):
    def __init__(self, caption):
        self.screen = pg.display.get_surface()
        self.finished = False
        self.clock = pg.time.Clock()
        self.caption = caption
        self.fps = 60
        self.show_fps = False
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None
        
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.start_name = start_state
        self.state = self.state_dict[self.start_name]
    
    def update(self):
        self.current_time = pg.time.get_ticks()
        if self.state.quit:
            self.finished = True
        elif self.state.finished:
            self.change_state()
        self.state.update(self.screen, self.keys, self.current_time)
    
    def change_state(self):
        previous,  self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.previous = previous
    
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.finished = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
                if event.key == pg.K_DOWN:
                    pressed = True
                elif event.key != pg.K_DOWN:
                    pressed = False
                self.toggle_show_fps(event.key)
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
            self.state.get_event(event)
            
    def toggle_show_fps(self, key):
        if key == pg.K_F5:
            self.show_fps = not self.show_fps
            if not self.show_fps:
                pg.display.set_caption(self.caption)
    
    def main(self):
        while not self.finished:
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)
            if self.show_fps:
                fps = self.clock.get_fps()
                with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
                pg.display.set_caption(with_fps)

pg.mixer.init()
class _State(object):
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.finished = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}
        
    def get_event(self, event):
        pass
    
    def startup(self, current_time, persistant):
        self.persist = persistant
        self.start_time = current_time
    
    def cleanup(self):
        self.finished = False
        return self.persist
    
    def update(self, surface, keys, current_time):
        pass
    
def load_gfx(directory, colorkey=(255,0,255), accept=('.png','.jpg','.bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory,pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name]=img
    return graphics
    
def load_music(directory, accept=('.wav','.mp3','.ogg','.mdi')):
    songs = {}
    for song in os.listdir(directory):
        name, ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs
    
def load_fonts(directory, accept =('.ttf')):
    return load_music(directory, accept)
    
def load_sfx(directory, accept=('.wav','.mp3','.ogg','mdi')):
    effects = {}
    for fx in os.listdir(directory):
        name,ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects