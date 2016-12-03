from pygame import *

PLATFORM_WIDTH = 16
PLATFORM_HEIGHT = 16
PLATFORM_COLOR = "#1739C3"

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        #self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("F:/pacman_py/Images/Blocks/wall-straight-horiz.gif")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)