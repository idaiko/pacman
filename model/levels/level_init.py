from pygame import *


def level_create(screen):
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
                # создаем блок, заливаем его цветом и рисеум его
                pf = Surface((platform_width, platform_height))
                pf.fill(Color(platform_color))
                screen.blit(pf, (x, y))
            elif col == "*":
                # создаем блок, заливаем его цветом и рисеум его
                pf = Surface((16, 5))
                pf.fill(Color(platform_color))
                screen.blit(pf, (x, (y+7)))

            x += platform_width  # блоки платформы ставятся на ширине блоков
        y += platform_height  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля