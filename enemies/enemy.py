import pygame
import math

class Enemy:
    img = []
    def __init__(self):

        self.width = 64
        self.height = 64
        self.imgs = []
        self.animation_count = 0
        self.health = 1
        self.path = [(14, 339), (35, 341), (57, 341), (91, 334), (129, 331), (159, 329), (179, 332), (197, 340), (220, 352), (254, 359), (285, 353), (307, 347), (330, 339), (360, 336), (391, 334), (419, 333), (444, 333), (476, 333), (502, 342), (516, 349), (531, 354), (544, 353), (561, 347), (584, 339), (602, 337), (624, 339), (650, 352), (675, 371), (697, 385), (736, 392), (782, 392), (819, 382), (839, 373), (866, 358), (884, 343), (895, 313), (900, 287), (901, 266), (912, 238), (931, 224), (962, 211), (976, 208), (992, 207), (1015, 202), (1037, 197), (1065, 194), (1089, 193)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        print(self.imgs)
        self.img = self.imgs[self.animation_count]
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))
        self.move()
        # win.blit(self.img, (self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2 - 35))



    def collide(self, X, Y):
        if X <= self.x + self.width and X>=self.x:
            if Y<= self.y + self.height and Y >= self.y:
                return True
        # Returns if position has hit enemy
        return False

    def move(self):
        # move enemy and return non
        x1,y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 193)
        else:
            x2,y2 = self.path[self.path_pos+1]

        move_dis = math.sqrt((x2 - x1) ** 2 +  (y2 - y1) ** 2)

        self.move_count += 1


        self.move_count += 1
        dirn = (x2-x1, y2-y1)

        move_x, move_y = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count)

        self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) **2)

        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1

        self.x = move_x
        self.y = move_y
        pass

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True