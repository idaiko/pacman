from pygame import *
import controller.pyganim as pyganim
import os

MONSTER_WIDTH = 16
MONSTER_HEIGHT = 16
MONSTER_COLOR = "#2110FF"
#ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

ANIMATION_MONSTERHORYSONTAL = [("F:/pacman_py//Images/Ghosts/ghost 1.gif"),
                               ("F:/pacman_py/Images/Ghosts/ghost 2.gif"),
                               ("F:/pacman_py/Images/Ghosts/ghost 3.gif"),
                               ("F:/pacman_py/Images/Ghosts/ghost 4.gif"),
                               ("F:/pacman_py/Images/Ghosts/ghost 5.gif"),
                               ("F:/pacman_py/Images/Ghosts/ghost 6.gif")]


class Monster(sprite.Sprite):
    def __init__(self, x, y, left, up, gPosX, gPosY):
        sprite.Sprite.__init__(self)
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(Color(MONSTER_COLOR))
        self.rect = Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.image.set_colorkey(Color(MONSTER_COLOR))
        self.startX = x  # начальные координаты
        self.startY = y
        self.gPosX = gPosX  # максимальное расстояние, которое может пройти в одну сторону
        self.gPosY = gPosY  # максимальное расстояние, которое может пройти в одну сторону, вертикаль
        self.xvel = left  # cкорость передвижения по горизонтали, 0 - стоит на месте
        self.yvel = up  # скорость движения по вертикали, 0 - не двигается
        boltAnim = []
        for anim in ANIMATION_MONSTERHORYSONTAL:
            boltAnim.append((anim, 0.3))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self, platforms, hero):  # по принципу героя

        self.image.fill(Color(MONSTER_COLOR))
        self.boltAnim.blit(self.image, (0, 0))

        self.rect.y += self.yvel
        self.rect.x += self.xvel

        self.collide(platforms, hero)

        #if (abs(self.startX - self.rect.x) > self.gPosX):
           # self.xvel = -self.xvel  # если прошли максимальное растояние, то идеи в обратную сторону
        #if (abs(self.startY - self.rect.y) > self.gPosY):
          #  self.yvel = -self.yvel  # если прошли максимальное растояние, то идеи в обратную сторону, вертикаль

    def collide(self, platforms, hero):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p:  # если с чем-то или кем-то столкнулись
                self.xvel = - self.xvel  # то поворачиваем в обратную сторону
                self.yvel = - self.yvel
        if sprite.collide_rect(self, hero) and self != hero:  # если с чем-то или кем-то столкнулись
            self.xvel = - self.xvel  # то поворачиваем в обратную сторону
            self.yvel = - self.yvel