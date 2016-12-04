import pygame
import model.levels.level_init as levelinit
from pygame import *

from model.player.pacman import Player


def create_window():
    # Объявляем переменные
    win_width = 800  # Ширина создаваемого окна
    win_height = 480  # Высота
    win_size = win_width, win_height  # Группируем ширину и высоту в одну переменную
    background_color = "#000000"

    done = True
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = display.set_mode(win_size)  # Создаем окошко
    display.set_caption("PacMan")  # Пишем в шапку

    bg = Surface((win_width, win_height))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(background_color))  # Заливаем поверхность сплошным цветом

    hero = Player(384, 352)

    left = right = up = down = False  # по умолчанию — стоим

    timer = pygame.time.Clock()

    while done:  # Основной цикл программы
        timer.tick(30)
        for e in event.get():  # Обрабатываем события
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = False
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        e_p = levelinit.level_create(screen, hero)
        hero.update(left, right, up, down, e_p[1])  # передвижение
        display.update()  # обновление и вывод всех изменений на экран
