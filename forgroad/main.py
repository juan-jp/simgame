import pygame
from pygame.locals import *
import GlobalVal as G
import sys
from car import Car
pygame.init()


SCREEN = pygame.display.set_mode(G.SCREEN_DIM)

pygame.display.set_caption('Frog Road!')

CLOCK = pygame.time.Clock()
FPS = 60
enemy_list = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    G.player.wrap_around_screen()
    G.all_sprites.update()
    G.car.move_towards_player(G.player.rect.center)
    G.car.spawn_enemy()
    # print(G.player.vel)
    G.car.spawn_enemy
    SCREEN.fill(G.BLACK)
    G.all_sprites.draw(SCREEN)

    pygame.display.update()
    CLOCK.tick(FPS)
pygame.quit()