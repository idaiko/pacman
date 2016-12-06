from pygame import *
from model.player.player_create import create_player
from model.levels.block import Platform
from model.levels.teleports import BlockTeleport
from model.levels.dots import Platform_dots
from model.player.pacman import Player


def level_create(screen, hero, mn):

   # hero = create_player()
    monsters = sprite.Group()  # Все передвигающиеся объекты




    entities = sprite.Group()  # Все объекты
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
        "\t\t\t\t\t\t\t\t\t\t\t\t-           -           -",
        "\t\t\t\t\t\t\t\t\t\t\t\t- --- ----- - ----- --- -",
        "\t\t\t\t\t\t\t\t\t\t\t\t- --- ----- - ----- --- -",
        "\t\t\t\t\t\t\t\t\t\t\t\t-                       -",
        "\t\t\t\t\t\t\t\t\t\t\t\t- --- - --------- - --- -",
        "\t\t\t\t\t\t\t\t\t\t\t\t-     -     -     -     -",
        "\t\t\t\t\t\t\t\t\t\t\t\t----- ----- - ----- -----",
        "\t\t\t\t\t\t\t\t\t\t\t\t^^^^- -           - -^^^^",
        "\t\t\t\t\t\t\t\t\t\t\t\t^^^^- - ----*---- - -^^^^",
        "\t\t\t\t\t\t\t\t\t\t\t\t----- - -^^^^^^^- - -----",
        "\t\t\t\t\t\t\t\t\t\t\t\t        -^^^^^^^-        ",
        "\t\t\t\t\t\t\t\t\t\t\t\t----- - -^^^^^^^- - -----",
        "\t\t\t\t\t\t\t\t\t\t\t\t^^^^- - --------- - -^^^^",
        "\t\t\t\t\t\t\t\t\t\t\t\t^^^^- -           - -^^^^",
        "\t\t\t\t\t\t\t\t\t\t\t\t----- - --------- - -----",
        "\t\t\t\t\t\t\t\t\t\t\t\t-           -           -",
        "\t\t\t\t\t\t\t\t\t\t\t\t- --- ----- - ----- --- -",
        "\t\t\t\t\t\t\t\t\t\t\t\t-   -       ^       -   -",
        "\t\t\t\t\t\t\t\t\t\t\t\t--- - - --------- - - ---",
        "\t\t\t\t\t\t\t\t\t\t\t\t-     -     -     -     -",
        "\t\t\t\t\t\t\t\t\t\t\t\t- --------- - --------- -",
        "\t\t\t\t\t\t\t\t\t\t\t\t-                       -",
        "\t\t\t\t\t\t\t\t\t\t\t\t-------------------------"]
    platform_width = 16
    platform_height = 16
    #platform_color = "#1739C3"

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

            elif col == " ":

                #print(str(x))
                pfd = Platform_dots(x, y)
                entities.add(pfd)
                platforms_dots.append(pfd)


            x += platform_width  # блоки платформы ставятся на ширине блоков
        y += platform_height  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    #hero.update(left, right, up, down, platforms)  # передвижение
    #hero.collide(screen)  # отображение
    tp1 = BlockTeleport(176, 240, 576, 240)


    tp2 = BlockTeleport(592, 240, 192, 240)

    #entities.add(tp1)
    #entities.add(tp2)
    platforms.append(tp1)
    platforms.append(tp2)
    entities.draw(screen)  # отображение
    return platforms, entities, platforms_dots