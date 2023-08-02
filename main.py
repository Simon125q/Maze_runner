import pygame
import sys
from settings import *
from map import Map

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = Map(self)
    
    def upadate(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption("Maze runner")
        
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.upadate()
            
if __name__ == "__main__":
    game = Game()
    game.run()
        