from pygame import *

PLATFORM_WIDTH = 3
PLATFORM_HEIGHT = 3
PLATFORM_COLOR = "#1739C3"

class Platform_dots(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color("#EFD332"))
        self.rect = Rect(x+6, y+6, PLATFORM_WIDTH, PLATFORM_HEIGHT)