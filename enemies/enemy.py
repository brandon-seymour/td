import pygame

class Enemy:
    imgs = []
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.imgs = []
        self.animation_count = 0
        self.health = 1
        self.path = []

    def draw(self, win):
        pass

    def collide(self, X, Y):
        if X <= self.x + self.width and X>=self.x:
            if Y<= self.y + self.height and Y >= self.y:
                return True
        # Returns if position has hit enemy
        return False

    def move(self):
        # move enemy and return non
        pass

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True