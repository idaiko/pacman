from pygame import *
from model.player.player_create import create_player
from model.levels.block import Platform


def level_create(screen, hero):

   # hero = create_player()
    entities = sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    entities.add(hero)
    #left = right = up = down = False  # по умолчанию — стоим

    level = [
        "                         ",
        "                         ",
        "                         ",
        "                         ",
        "\t\t\t\t\t\t\t\t\t\t\t\t-------------------------",
        "\t\t\t\t\t\t\t\t\t\t\t\t-           -           -",
        "\t\t\t\t\t\t\t\t\t\t\t\t- --- ----- - ----- --- -",
        "\t\t\t\t\t\t\t\t\t\t\t\t- --- ----- - ----- --- -",
        "\t\t\t\t\t\t\t\t\t\t\t\t-                       -",
        "\t\t\t\t\t\t\t\t\t\t\t\t- --- - --------- - --- -",
        "\t\t\t\t\t\t\t\t\t\t\t\t-     -     -     -     -",
        "\t\t\t\t\t\t\t\t\t\t\t\t----- ----- - ----- -----",
        "\t\t\t\t\t\t\t\t\t\t\t\t    - -           - -    ",
        "\t\t\t\t\t\t\t\t\t\t\t\t    - - ----*---- - -    ",
        "\t\t\t\t\t\t\t\t\t\t\t\t----- - -       - - -----",
        "\t\t\t\t\t\t\t\t\t\t\t\t        -       -        ",
        "\t\t\t\t\t\t\t\t\t\t\t\t----- - -       - - -----",
        "\t\t\t\t\t\t\t\t\t\t\t\t    - - --------- - -    ",
        "\t\t\t\t\t\t\t\t\t\t\t\t    - -           - -    ",
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
    platform_color = "#1739C3"

    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            elif col == "*":
                # создаем блок, заливаем его цветом и рисеум его
                pf = Surface((16, 5))
                pf.fill(Color(platform_color))
                screen.blit(pf, (x, (y+7)))

            x += platform_width  # блоки платформы ставятся на ширине блоков
        y += platform_height  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    #hero.update(left, right, up, down, platforms)  # передвижение
    #hero.collide(screen)  # отображение
    entities.draw(screen)  # отображение
    return entities, platforms