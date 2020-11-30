__author__ = "Raiyan Yahya"
import pygame

white = (255, 255, 255)
green = (92, 225, 15)

generation_color = [(92, 225, 15), (255, 192, 203), (255, 182, 193), (255, 105, 180), (255, 20, 147), (219, 112, 147),
                    (199, 21, 133), (218, 112, 214), (255, 0, 255), (238, 130, 238), (221, 160, 221), (128, 0, 0),
                    (139, 0, 0), (165, 42, 42), (178, 34, 34), (220, 20, 60), (255, 0, 0), (255, 99, 71),
                    (255, 127, 80), (205, 92, 92), (240, 128, 128), (233, 150, 122), (250, 128, 114), (255, 160, 122),
                    (255, 69, 0), (255, 140, 0), (255, 165, 0), (255, 215, 0), (184, 134, 11), (218, 165, 32),
                    (238, 232, 170), (189, 183, 107), (240, 230, 140), (128, 128, 0), (255, 255, 0), (154, 205, 50),
                    (85, 107, 47), (107, 142, 35), (124, 252, 0), (127, 255, 0), (173, 255, 47), (0, 100, 0),
                    (0, 128, 0), (34, 139, 34), (0, 255, 0), (50, 205, 50), (144, 238, 144), (152, 251, 152),
                    (143, 188, 143), (0, 250, 154), (0, 255, 127), (46, 139, 87), (102, 205, 170), (60, 179, 113),
                    (32, 178, 170), (47, 79, 79), (0, 128, 128), (0, 139, 139), (0, 255, 255), (0, 255, 255),
                    (224, 255, 255), (0, 206, 209), (64, 224, 208), (72, 209, 204), (175, 238, 238), (127, 255, 212),
                    (176, 224, 230), (95, 158, 160), (70, 130, 180), (100, 149, 237), (0, 191, 255), (30, 144, 255),
                    (173, 216, 230), (135, 206, 235), (135, 206, 250)]


class Celle(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, width, height, radius=4, color=green, velocity=[0, 0], lifespan=30,
                 mutate=False, generation=0):
        super().__init__()
        self.mutate = mutate
        self.generation = generation
        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.fill(white)
        pygame.draw.circle(self.image, generation_color[generation], (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.position = [x_position, y_position]
        self.velocity = velocity
        self.WIDTH = width
        self.HEIGHT = height
        self.lifespan = lifespan
        if self.mutate:
            self.increase_velocity()
            self.increase_life()

    def update(self):
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
        self.velocity[0] = self.velocity[0] * 3
        self.velocity[1] = self.velocity[1] * 3
