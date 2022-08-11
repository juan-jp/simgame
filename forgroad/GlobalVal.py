import pygame
from Protagonist import Frog
from car import Car

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)
SCREEN_DIM = WIDTH, HEIGHT = 1200, 700
MAX_SPEED = 4

all_sprites = pygame.sprite.Group()
player = Frog()

all_sprites.add(player)


