import pygame

import math
import random
from pygame.locals import *


class Car(pygame.sprite.Sprite):
    Image = pygame.image.load("assets/oppcar.png")
    Size = (20, 10)
    enemy_num = 0
    start_po = (500, random.randint(0, 800))
    speed = 0.3
    if enemy_num % 2 == 0:
        start_po = (1200, random.randint(0, 800))
    else:
        start_po = (0, random.randint(0, 800))

    def __init__(self):
        super(Car, self).__init__()
        self.image = Car.Image
        self.rect = pygame.Rect((0, 0), Car.Size)
        self.rect.center = Car.start_po

    def move_towards_player(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = player[0] - self.rect.x, player[1] - self.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
    def spawn_enemy(self):

        new_enemy =Car()

