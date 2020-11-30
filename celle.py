__author__ = "Raiyan Yahya"
import pygame

white = (255, 255, 255)
green = (92, 225, 15)


class Celle(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, width, height, radius=4, color=green, velocity=[0, 0], lifespan=30,
                 mutate=False):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.fill(white)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.position = [x_position, y_position]
        self.velocity = velocity
        self.WIDTH = width
        self.HEIGHT = height
        self.lifespan = lifespan
        self.mutate = mutate

    def update(self):
        if self.mutate:
            self.increase_velocity()
            self.increase_life()
            self.mutate = False
        self.position[0] = self.position[0] + self.velocity[0]
        self.position[1] = self.position[1] + self.velocity[1]
        x, y = self.position
        if x < 0:
            self.position[0] = self.WIDTH
            x = self.WIDTH
        if x > self.WIDTH:
            self.position[0] = 0
            x = 0
        if y < 0:
            self.position[1] = self.HEIGHT
            y = self.HEIGHT
        if y > self.HEIGHT:
            self.position[1] = 0
            y = 0
        if self.lifespan > 0:
            self.lifespan = self.lifespan - 1
        else:
            self.kill()
        self.rect.x = x
        self.rect.y = y

    def increase_life(self):
        self.lifespan += 30

    def increase_velocity(self):
        self.velocity[0] = self.velocity[0] * 2
        self.velocity[1] = self.velocity[1] * 2
