__author__ = "Raiyan Yahya"
import pygame

white = (255, 255, 255)
floro_blue = (58, 75, 241)


class Kryptonite(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, width, height, radius=5, color=floro_blue):
        super().__init__()
        self.image = pygame.Surface([radius, radius])
        self.image.fill(white)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.position = [x_position, y_position]
        self.WIDTH = width
        self.HEIGHT = height

    def update(self):
        x, y = self.position
        self.rect.x = x
        self.rect.y = y