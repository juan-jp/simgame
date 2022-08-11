import pygame
from pygame.locals import *
import GlobalVal as G
vec =pygame.math.Vector2
class Frog(pygame.sprite.Sprite):
    Start_po =vec(300,400)
    size =(20, 10)
    Image = pygame.image.load('assets/car.png')
    def __init__(self):
        super(Frog, self).__init__()
        self.image = Frog.Image
        self.original_image = self.image
        self.rect = pygame.Rect((0,0), Frog.size)
        self.position = vec(G.WIDTH / 2, G.HEIGHT / 2)
        self.rect.center = Frog.Start_po
        self.vel = vec(0,0)
        self.acceleration = vec(0,-0.2)
        self.angle_speed =0
        self.angle = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            self.angle_speed = -2
            G.player.rotate()
        if keys[K_d]:
            self.angle_speed = 2
            G.player.rotate()
        # If up or down is pressed, accelerate the ship by
        # adding the acceleration to the velocity vector.
        if keys[K_w]:
            self.vel += self.acceleration
        if keys[K_s]:
            self.vel -= self.acceleration
        if keys[K_SPACE]:
            if self.vel[0] > 0:
                self.vel[0] -= 0.1
            if self.vel[0] < 0:
                self.vel[0] += 0.1
            if self.vel[1] > 0:
                self.vel[1] += -0.1
            if self.vel[1] < 0:
                self.vel[1] -= -0.1
            if -0.1 < self.vel[0] < 0.1:
                self.vel[0]=0
            if -0.1 < self.vel[1] < 0.1:
                self.vel[1] = 0

        # max speed
        if self.vel.length() > G.MAX_SPEED:
            self.vel.scale_to_length(G.MAX_SPEED)

        self.position += self.vel
        self.rect.center = self.position

    def rotate(self):
        # Rotate the acceleration vector.
        self.acceleration.rotate_ip(self.angle_speed)
        self.angle += self.angle_speed
        if self.angle > 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def wrap_around_screen(self):
        """Wrap around screen."""
        if self.position.x > G.WIDTH:
            self.position.x = G.WIDTH
        if self.position.x < 0:
            self.position.x = 0
        if self.position.y <= 0:
            self.position.y = 0
        if self.position.y > G.HEIGHT:
            self.position.y = G.HEIGHT
    def bullet_fire(self):
        pass

