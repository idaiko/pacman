from pygame import *

MOVE_SPEED = 7
WIDTH = 14
HEIGHT = 14
COLOR = "#EB6313"


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.yvel = 0 # speed moved
        self.startX = 384  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = 352
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self, left, right, up, down):
        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
        if up:
            self.yvel = -MOVE_SPEED  # up = x- n

        if down:
            self.yvel = MOVE_SPEED  # down = x + n

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not (up or down):  # стоим, когда нет указаний идти
            self.yvel = 0

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.rect.y += self.yvel  # переносим свои положение на xvel

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))