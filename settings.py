import csv

def import_map(file):
    game_map = []
    with open(file) as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row != []:
                game_map.append(row)
            
    return game_map

RES = WIDTH, HEIGHT = (1200, 900)
FPS = 60
TILE = 35

PLAYER_POS = 1, 5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

LIGHT_COLOR = 'yellow'
PLAYER_COLOR = 'green'