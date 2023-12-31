import pygame
import sys
from settings import *
from map import Map
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
    
    def upadate(self):
        self.player.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption("Maze runner")
        
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()
        
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
        