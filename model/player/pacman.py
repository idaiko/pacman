from pygame import *
from controller.pyganim import *
from model.levels.teleports import BlockTeleport

MOVE_SPEED = 4
WIDTH = 16
HEIGHT = 16
COLOR = "#EB6313"

ANIMATION_DELAY = 0.1 # скорость смены кадров
PACMAN_WALK_UP = [('F:/pacman_py/Images/Player/pacman-u 1.gif'),
                  ('F:/pacman_py/Images/Player/pacman-u 2.gif'),
                  ('F:/pacman_py/Images/Player/pacman-u 3.gif'),
                  ('F:/pacman_py/Images/Player/pacman-u 4.gif'),
                  ('F:/pacman_py/Images/Player/pacman-u 5.gif'),
                  ('F:/pacman_py/Images/Player/pacman-u 6.gif'),
                  ('F:/pacman_py/Images/Player/pacman-u 7.gif'),
                  ('F:/pacman_py/Images/Player/pacman-u 8.gif')]

PACMAN_WALK_DOWN = [('F:/pacman_py/Images/Player/pacman-d 1.gif'),
                    ('F:/pacman_py/Images/Player/pacman-d 2.gif'),
                    ('F:/pacman_py/Images/Player/pacman-d 3.gif'),
                    ('F:/pacman_py/Images/Player/pacman-d 4.gif'),
                    ('F:/pacman_py/Images/Player/pacman-d 5.gif'),
                    ('F:/pacman_py/Images/Player/pacman-d 6.gif'),
                    ('F:/pacman_py/Images/Player/pacman-d 7.gif'),
                    ('F:/pacman_py/Images/Player/pacman-d 8.gif')]

PACMAN_WALK_LEFT = [('F:/pacman_py/Images/Player/pacman-l 1.gif'),
                    ('F:/pacman_py/Images/Player/pacman-l 2.gif'),
                    ('F:/pacman_py/Images/Player/pacman-l 3.gif'),
                    ('F:/pacman_py/Images/Player/pacman-l 4.gif'),
                    ('F:/pacman_py/Images/Player/pacman-l 5.gif'),
                    ('F:/pacman_py/Images/Player/pacman-l 6.gif'),
                    ('F:/pacman_py/Images/Player/pacman-l 7.gif'),
                    ('F:/pacman_py/Images/Player/pacman-l 8.gif')]

PACMAN_WALK_RIGHT = [('F:/pacman_py/Images/Player/pacman-r 1.gif'),
                    ('F:/pacman_py/Images/Player/pacman-r 2.gif'),
                    ('F:/pacman_py/Images/Player/pacman-r 3.gif'),
                    ('F:/pacman_py/Images/Player/pacman-r 4.gif'),
                    ('F:/pacman_py/Images/Player/pacman-r 5.gif'),
                    ('F:/pacman_py/Images/Player/pacman-r 6.gif'),
                    ('F:/pacman_py/Images/Player/pacman-r 7.gif'),
                    ('F:/pacman_py/Images/Player/pacman-r 8.gif')]

#PACMAN_WALK_RIGHT = [('F:/pacman_py/Images/Player/pacman.png'),
#                    ('F:/pacman_py/Images/Player/pacman')]

ANIMATION_STAY = [('F:/pacman_py/Images/Player/pacman-r 1.gif', 0.1)]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.yvel = 0 # speed moved
        self.startX = 384  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = 352
        self.image = Surface((WIDTH, HEIGHT))
        #self.image = image.load("F:/pacman_py/Images/Player/pacman.gif")
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

        self.image.set_colorkey(Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо
        boltAnim = []
        for anim in PACMAN_WALK_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in PACMAN_WALK_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        #        Анимация движения up
        boltAnim = []
        for anim in PACMAN_WALK_UP:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimUp = PygAnimation(boltAnim)
        self.boltAnimUp.play()

        #        Анимация движения down
        boltAnim = []
        for anim in PACMAN_WALK_DOWN:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimDown = PygAnimation(boltAnim)
        self.boltAnimDown.play()

        self.boltAnimStay = PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY

    def update(self, left, right, up, down, platforms):
        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))


        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            self.image.fill(Color(COLOR))
            self.boltAnimStay.blit(self.image, (0, 0))
        if up:
            self.yvel = -MOVE_SPEED  # up = x- n
            self.image.fill(Color(COLOR))
            self.boltAnimUp.blit(self.image, (0, 0))

        if down:
            self.yvel = MOVE_SPEED  # down = x + n
            self.image.fill(Color(COLOR))
            self.boltAnimDown.blit(self.image, (0, 0))

        if not (up or down):  # стоим, когда нет указаний идти
            self.yvel = 0

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)


    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

                if isinstance(p, BlockTeleport):
                    self.teleporting(p.goX, p.goY)
