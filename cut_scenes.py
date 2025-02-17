from pygame import *
from sys import *
init()


def draw_text(screen, text, size, color, x, y):
    main_font = font.SysFont(None, size)
    text_surface = main_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

class CutSceneZero:
    
    def __init__(self, player):

        # Variables
        self.name = 'zero'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "Something is happening in the rainforest...",
            'two': "The animals are attacking for no reason and they are very aggressive.",
            'three': "Ducky wants to find out what's going on.",
            'four': "Are you willing to help him get to the bottom of the matter?",
            'move': "MOVE: WASD",
            'volume': "VOLUME: ARROWS",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 3
                    self.time = 0
                    self.text_counter = 0

        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):

        draw_text(
            screen,
            self.text['move'][0:len(self.text['move'])],
            50,
            (236, 157, 83),
            50,
            20
        )

        draw_text(
            screen,
            self.text['volume'][0:len(self.text['volume'])],
            50,
            (236, 157, 83),
            900,
            20
        )
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )
        
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

class CutSceneOneStart:
    
    def __init__(self, player):

        # Variables
        self.name = 'one_start'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "Hahaha, a duckling.",
            'two': "You won't last a day in this jungle.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

class CutSceneOneFinal:
    
    def __init__(self, player):

        # Variables
        self.name = 'one_final'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "Ouch, what happened?",
            'two': "Something attacked me in the pond and I lost consciousness.",
            'three': "I'll go rest, good luck on your adventure!"
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )
        
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

class CutSceneTwoStart:
    
    def __init__(self, player):

        # Variables
        self.name = 'two_start'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "You again? You can't pass this one.",
            'two': "Not everyone has the agility to avoid the shells.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

class CutSceneTwoFinal:
    
    def __init__(self, player):

        # Variables
        self.name = 'two_final'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "Uff, what a headache!",
            'two': "I was attacked by a jellyfish on the beach and I don't remember anything.",
            'three': "Damn, my eggs have to be ready to hatch! Bye."
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )
        
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

class CutSceneThreeStart:
    
    def __init__(self, player):

        # Variables
        self.name = 'three_start'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "Under water I don't think you're that good, little duck.",
            'two': "Be careful with the tentacles hahaha.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

class CutSceneThreeFinal:
    
    def __init__(self, player):

        # Variables
        self.name = 'three_final'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "Sorry, I don't know what happened to me, but I think I can help you.",
            'two': "Behind that rock is a secret cave.",
            'three': "What you are looking for is hidden there."
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )
        
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

class CutSceneFourStart:
    
    def __init__(self, player):

        # Variables
        self.name = 'four_start'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "I'm not even going to bother moving from here.",
            'two': "My little ones will take care.",
            'three': "ATTACK GUYS!"
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )
        
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

class CutSceneFourFinal:
    
    def __init__(self, player):

        # Variables
        self.name = 'four_final'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "Guys let's get out of here.",
            'two': "Since this thing arrived, only bad things have happened.",
            'three': "I don't recommend you go in there alone Ducky..."
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )
        
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

class CutSceneFiveStart:
    
    def __init__(self, player):

        # Variables
        self.name = 'five_start'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "...",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                640
            )

class CutSceneFiveFinal:
    
    def __init__(self, player):

        # Variables
        self.name = 'five_final'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "...",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 750:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space and self.time == 750:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                640
            )

class CutSceneSix:
    
    def __init__(self, player):

        # Variables
        self.name = 'six'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "Thanks for playing :)",
            'two': "Game by Zero2680",
            'three': "Music by bluelike_u (Pixabay)",
            'four': "Press space to leave."
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 3
                    self.time = 0
                    self.text_counter = 0

        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running
    
    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )
        
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                50,
                (255, 255, 255),
                50,
                650
            )

class CutSceneManager:

    def __init__(self, screen):
        self.cut_scenes_complete = []
        self.cut_scene = None
        self.cut_scene_running = False

        # Drawing variables
        self.screen = screen
        self.window_size = 0

    def start_cut_scene(self, cut_scene):
        if cut_scene.name not in self.cut_scenes_complete:
            self.cut_scenes_complete.append(cut_scene.name)
            self.cut_scene = cut_scene
            self.cut_scene_running = True

    def end_cut_scene(self):
        self.cut_scene = None
        self.cut_scene_running = False

    def update(self):

        if self.cut_scene_running:
            if self.window_size < self.screen.get_height()*0.3: self.window_size += 2
            self.cut_scene_running = self.cut_scene.update()
        else:
            self.end_cut_scene()

    def draw(self):
        if self.cut_scene_running:
            # Draw rect generic to all cut scenes
            draw.rect(self.screen, (0, 0, 0), (0, 600, self.screen.get_width(), self.window_size))
            # Draw specific cut scene details
            self.cut_scene.draw(self.screen)
