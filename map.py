import pygame
from settings import *

class Map:
    def __init__(self, game):
        self.game = game
        self.game_map = import_map('maze.csv')
        self.world_map = {}
        self.get_map()
        
    def get_map(self):
        for j, row in enumerate(self.game_map):
            for i, value in enumerate(row):
                if value == '#':
                    self.world_map[(i, j)] = value
                    
    def draw(self):
        for pos in self.world_map:
            pygame.draw.rect(self.game.screen, 'darkgrey', (pos[0] * TILE, pos[1] * TILE, TILE, TILE), 2)