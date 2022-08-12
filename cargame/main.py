from email.header import Header
from turtle import width
import pygame
import time
import math
from utils import scale_image, blit_rotate_center
import random
import neat


RED_CAR = scale_image(pygame.image.load('cargame/car.png'), 1)
BLUE_CAR =scale_image(pygame.image.load('cargame/oppcar.png'), 1)
generation = 0
WIDTH, HEIGHT = 1200,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

FPS = 60
enenmy_list =[]
enemycount=len(enenmy_list)
class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()
    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi


class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)


def draw(win, player_car):
    
    player_car.draw(win)
    pygame.display.update()
player_car = PlayerCar(4, 4)

class enenmy(AbstractCar):
    IMG = BLUE_CAR
    
    if enemycount%2 ==0:
        START_POS =(0, random.randint(0, WIDTH)) 
    else:
        START_POS =(WIDTH, random.randint(0, WIDTH))
    def __init__(self, max_vel, rotation_vel):
        super().__init__(max_vel, rotation_vel)
        
        self.vel = max_vel
    def create_enemy():
        new_enemy =enenmy(1.5,1.5)
        enenmy_list.append(new_enemy)
    
    def move(self):
        if self.START_POS == 0:
            self.x+=0.3
        else:
            self.x-=0.3

run = True
clock = pygame.time.Clock()
record = time.time()
player_car = PlayerCar(4, 4)


while run:
    clock.tick(FPS)

    draw(WIN, player_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
    ct =time.time()

    enenmy.create_enemy()

    for i in enenmy_list:
        draw(WIN, i)
        i.move()
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()

    if not moved:
        player_car.reduce_speed()
    if player_car.x <= 0:
        player_car.x=0
    if player_car.y <=0:
        player_car.y=0
    if player_car.x >=WIDTH:
        player_car.x=0
    if player_car.y >=HEIGHT:
        player_car.y =0
    
    WIN.fill((0,0,0))

pygame.quit()
