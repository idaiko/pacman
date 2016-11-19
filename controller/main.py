# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame
import model.window.init as wininit
import model.levels.level_init as levelinit
from pygame import *

# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = wininit.background()
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"


def main():
    done = True
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("PacMan")  # Пишем в шапку

    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    while done:  # Основной цикл программы
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                done = False



        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        levelinit.level_create(screen)

        pygame.display.update()  # обновление и вывод всех изменений на экран

if __name__ == "__main__":
    main()
