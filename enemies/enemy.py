import pygame

class Enemy:
    imgs = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.imgs = []
        self.animation_count = 0
        self.health = 1
        self.path = []

    def draw(self, win):
        pass

    def collide(self, x, y):
        # Returns if position has hit enemy
        return False

    def move(self):
        # move enemy and return non
        pass

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True