import pygame
from pygame import *

def level_create(screen):
    level = [
        "-------------------------",
        "-                       -",
        "-                       -",
        "-                       -",
        "-            --         -",
        "-                       -",
        "--                      -",
        "-                       -",
        "-                   --- -",
        "-                       -",
        "-                       -",
        "-      ---              -",
        "-                       -",
        "-   -----------         -",
        "-                       -",
        "-                -      -",
        "-                   --  -",
        "-                       -",
        "-                       -",
        "-------------------------"]
    platform_width = 32
    platform_heigth = 32
    platform_color = "#FF6262"

    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                # создаем блок, заливаем его цветом и рисеум его
                pf = Surface((platform_width, platform_heigth))
                pf.fill(Color(platform_color))
                screen.blit(pf, (x, y))

            x += platform_width  # блоки платформы ставятся на ширине блоков
        y += platform_heigth  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля