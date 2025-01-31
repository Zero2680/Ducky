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
            'one': "Algo está pasando en la selva tropical...",
            'two': "Los animales están atacando sin motivo y se muestran muy agresivos.",
            'three': "Perry quiere descubrir lo que ocurre.",
            'four': "¿Está dispuesto a ayudarle para llegar al fondo del asunto?"
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
            'one': "Jajaja, un patito.",
            'two': "No durarás ni un día en esta selva.",
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
            'one': "Auch, ¿qué ha pasado?",
            'two': "Me ha atacado algo en el estanque y perdí la conciencia.",
            'three': "Iré a descansar, ¡suerte en tu aventura!"
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
            'one': "¿Otra vez tú?, de esta sí que no pasas",
            'two': "No cualquiera tiene la agilidad para esquivar las conchas.",
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
            'one': "Uff, ¡qué dolor de cabeza!",
            'two': "Me atacó una medusa en la playa y no recuerdo nada.",
            'three': "¡Ostras, mis huevos tienen que estar a punto de eclosionar! Me voy."
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
            'one': "Bajo el agua no creo que seas tan bueno patito.",
            'two': "Cuidado con los tentáculos jajaja.",
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
            'one': "Perdona, no se que me ha pasado, pero creo que te puedo ayudar.",
            'two': "Detrás de esa roca hay una cueva secreta.",
            'three': "Ahí se esconde lo que estás buscando."
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
            'one': "No me voy a molestar ni en moverme de aquí.",
            'two': "Mis pequeños se encargarán",
            'three': "¡CHICOS ATACAD!"
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
            'one': "Chicos vamonos de aquí.",
            'two': "Desde que llegó es cosa solo han pasado cosas malas.",
            'three': "No te recomiendo entrar ahí solo patito..."
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