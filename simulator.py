__author__ = "Raiyan Yahya"

import random
import sys
import pygame

from celle import Celle
from kryptonite import Kryptonite

pygame.init()
pygame.display.set_caption('Natural Selection Simulation')
programIcon = pygame.image.load('simulation.png')
pygame.display.set_icon(programIcon)

container = pygame.sprite.Group()
clock = pygame.time.Clock()


class Simulator:
    def __init__(self, width=800, height=640):
        self.WIDTH = width
        self.HEIGHT = height
        self.steps = 5000
        self.celle_group = pygame.sprite.Group()
        self.krytonite_group = pygame.sprite.Group()
        self.sim_group = pygame.sprite.Group()

    def generate_kryptonites(self, n):
        for _ in range(n):
            kryptonite = Kryptonite(random.randint(0, self.WIDTH + 1), random.randint(0, self.HEIGHT + 1), self.WIDTH,
                                    self.HEIGHT)
            self.krytonite_group.add(kryptonite)
            self.sim_group.add(kryptonite)

    def generate_celle(self, n, mutate=False):
        for _ in range(n):
            vel = [random.random() * 2 - 1 for _ in range(0, 2)]
            celle = Celle(random.randint(0, self.WIDTH + 1), random.randint(0, self.HEIGHT + 1), self.WIDTH,
                          self.HEIGHT, velocity=vel, mutate=mutate)
            self.celle_group.add(celle)
            self.sim_group.add(celle)

    def start_sim(self):
        screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.generate_kryptonites(100)
        self.generate_celle(500)
        for step in range(self.steps):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.sim_group.update()
            eaten_krypto__group = pygame.sprite.groupcollide(self.celle_group, self.krytonite_group, False, True, )
            for celle in eaten_krypto__group:
                celle.increase_life()
                self.generate_celle(1, mutate=True)
            eaten_krypto__group.clear()
            if step % 5 == 0:
                self.generate_kryptonites(5)
            screen.fill((255, 255, 255))
            self.sim_group.draw(screen)
            pygame.display.flip()
            clock.tick(10)

        pygame.quit()


if __name__ == "__main__":
    sim = Simulator()
    sim.start_sim()
