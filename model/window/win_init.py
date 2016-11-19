import pygame
import model.levels.level_init as levelinit
from pygame import *

def create_window():
    # Объявляем переменные
    win_width = 800  # Ширина создаваемого окна
    win_heith = 640  # Высота
    display = (win_width, win_heith)  # Группируем ширину и высоту в одну переменную
    background_color = "#000000"

    done = True
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(display)  # Создаем окошко
    pygame.display.set_caption("PacMan")  # Пишем в шапку

    bg = Surface((win_width, win_heith))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(background_color))  # Заливаем поверхность сплошным цветом

    while done:  # Основной цикл программы
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                done = False

        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        levelinit.level_create(screen)

        pygame.display.update()  # обновление и вывод всех изменений на экран
