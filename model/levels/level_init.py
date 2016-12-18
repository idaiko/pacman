from pygame import *

from model.levels.block import Platform
from model.levels.teleports import BlockTeleport
from model.levels.dots import Platform_dots



def level_create(screen, hero, mn):

    monsters = sprite.Group()  # Все передвигающиеся объекты

    entities = sprite.Group()  # Все объекты
    entities_dot = sprite.Group()
    platforms = []  # то, во что мы будем врезаться или опираться
    entities.add(hero)
    platforms_dots = []

    entities.add(mn)
    platforms.append(mn)
    monsters.add(mn)  #left = right = up = down = False  # по умолчанию — стоим

    level = [
        "",
        "",
        "",
        "",
        "\t\t\t\t\t\t\t\t\t\t\t\t-------------------------",
        "\t\t\t\t\t\t\t\t\t\t\t\t-00000000000-00000000000-",
        "\t\t\t\t\t\t\t\t\t\t\t\t-0---0-----0-0-----0---0-",
        "\t\t\t\t\t\t\t\t\t\t\t\t-0---0-----0-0-----0---0-",
        "\t\t\t\t\t\t\t\t\t\t\t\t-00000000000000000000000-",
        "\t\t\t\t\t\t\t\t\t\t\t\t-0---0-0---------0-0---0-",
        "\t\t\t\t\t\t\t\t\t\t\t\t-00000-00000-00000-00000-",
        "\t\t\t\t\t\t\t\t\t\t\t\t-----0-----0-0-----0-----",
        "\t\t\t\t\t\t\t\t\t\t\t\t^^^^-0-00000000000-0-^^^^",
        "\t\t\t\t\t\t\t\t\t\t\t\t^^^^-0-0----*----0-0-^^^^",
        "\t\t\t\t\t\t\t\t\t\t\t\t-----0-0-^^^^^^^-0-0-----",
        "\t\t\t\t\t\t\t\t\t\t\t\t00000000-^^^^^^^-00000000",
        "\t\t\t\t\t\t\t\t\t\t\t\t-----0-0-^^^^^^^-0-0-----",
        "\t\t\t\t\t\t\t\t\t\t\t\t^^^^-0-0---------0-0-^^^^",
        "\t\t\t\t\t\t\t\t\t\t\t\t^^^^-0-00000000000-0-^^^^",
        "\t\t\t\t\t\t\t\t\t\t\t\t-----0-0---------0-0-----",
        "\t\t\t\t\t\t\t\t\t\t\t\t-00000000000-00000000000-",
        "\t\t\t\t\t\t\t\t\t\t\t\t-0---0-----0-0-----0---0-",
        "\t\t\t\t\t\t\t\t\t\t\t\t-000-0000000^0000000-000-",
        "\t\t\t\t\t\t\t\t\t\t\t\t---0-0-0---------0-0-0---",
        "\t\t\t\t\t\t\t\t\t\t\t\t-00000-00000-00000-00000-",
        "\t\t\t\t\t\t\t\t\t\t\t\t-0---------0-0---------0-",
        "\t\t\t\t\t\t\t\t\t\t\t\t-00000000000000000000000-",
        "\t\t\t\t\t\t\t\t\t\t\t\t-------------------------"]

    platform_width = 16
    platform_height = 16

    x = y = 0  # координаты

    for row in level:  # вся строка
        for col in row:  # каждый символ

            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            elif col == "*":
                # создаем блок, заливаем его цветом и рисеум его
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            elif col == "0":
                pfd = Platform_dots(x, y)
                entities_dot.add(pfd)
                platforms_dots.append(pfd)

            x += platform_width  # блоки платформы ставятся на ширине блоков
        y += platform_height  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    tp1 = BlockTeleport(176, 240, 576, 240)

    tp2 = BlockTeleport(592, 240, 192, 240)

    platforms.append(tp1)
    platforms.append(tp2)
    entities_dot.draw(screen)
    entities.draw(screen)  # отображение
    return platforms, entities, platforms_dots, entities_dot