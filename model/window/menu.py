from pygame import *
from model.window.fonts import fonts
import sys

class Menu:
    def __init__(self, points = [784, 240, "Start Game", (255, 255, 255), (135, 135, 135), 0]):
        self.points = points

    def draw(self, bg, font_menu, num_points):
        #font = fonts()
        for i in self.points:
            if num_points == i[5]:
                bg.blit(font_menu.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                bg.blit(font_menu.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self, screen, bg):
        done = True
        font_menu = fonts()
        point = 0

        mouse.set_visible(True)
        key.set_repeat(0, 0)

        picture = image.load("F:/pacman_py/Images/Other/picture.jpg")
        picture_screen = Surface((550, 168))
        picture_screen.blit(picture, (250, 16))

        while done:
            bg.fill(Color("#000000"))

            mp = mouse.get_pos()

            for i in self.points:
                if (mp[0] > i[0] and mp[0] < i[0] + 155) and (mp[1] > i[1] and mp[1] < i[1] + 32):
                    point = i[5]
            self.draw(bg, font_menu, point)

            for e in event.get():
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        sys.exit()
                    if e.key == K_UP:
                        if point > 0:
                            point -= 1
                    if e.key == K_DOWN:
                        if point < len(self.points) - 1:
                            point += 1
                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    if point == 0:
                        done = False
                    elif point == 1:
                        sys.exit()

            screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
            screen.blit(picture_screen, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
            display.update()
            #display.update()
