import asyncio
import sys

import pygame

COLORS = [
    ['aqua', 'indigo', 'brown'],
    ['coral', 'crimson', 'yellowgreen'],
]
FPS = 25


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()

    color_index_column = 0
    color_index_line = 0
    color_len_column = len(COLORS)
    color_len_line = len(COLORS[0])

    while True:  # EVENT LOOP
        for event in pygame.event.get():
            if not event.type == pygame.KEYUP:
                continue

            if event.key == pygame.K_a:
                color_index_line = (color_index_line - 1) % color_len_line
                new_color = COLORS[color_index_column][color_index_line]
                screen.fill(new_color)
                pygame.display.update()

            if event.key == pygame.K_d:
                color_index_line = (color_index_line + 1) % color_len_line
                new_color = COLORS[color_index_column][color_index_line]
                screen.fill(new_color)
                pygame.display.update()

            if event.key == pygame.K_w:
                color_index_column = (color_index_column + 1) % color_len_column
                new_color = COLORS[color_index_column][color_index_line]
                screen.fill(new_color)
                pygame.display.update()

            if event.key == pygame.K_s:
                color_index_column = (color_index_column - 1) % color_len_column
                new_color = COLORS[color_index_column][color_index_line]
                screen.fill(new_color)
                pygame.display.update()

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        clock.tick(FPS)  # Frames per second, 25 fps
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
