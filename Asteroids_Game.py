import pygame

from models import GameObject
from utils import load_sprite
from models import Spaceship

class Asteroids_Game:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()
        self.spaceship = Spaceship((400, 300))

        '''
        
        
        
        removed asteroid object call, because of GameObject base class is gonna
        be inherited by other classes, check models.py for more. it'll be
    


        '''

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Asteroids_Game")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

    def _process_game_logic(self):
        self.spaceship.move()
        self.asteroid.move()

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)
        self.asteroid.draw(self.screen)
        print("Collides:", self.spaceship.collides_with(self.asteroid))
        pygame.display.flip()
        self.clock.tick(60)