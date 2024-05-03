import asyncio
import sys

import pygame

COLORS = [
    ['aqua', 'indigo', 'brown'],
    ['coral', 'crimson', 'yellowgreen'],
]

COLOR_LEN_COLUMN = len(COLORS)
COLOR_LEN_LINE = len(COLORS[0])
FPS = 25


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()

    color_index_column = 0
    color_index_line = 0

    def change_color(current_index: int, increment: int, is_line: bool):
        if is_line:
            current_index = (current_index + increment) % COLOR_LEN_LINE
            new_color = COLORS[color_index_column][current_index]
            screen.fill(new_color)
            pygame.display.update()
            return current_index
        else:
            current_index = (current_index + increment) % COLOR_LEN_COLUMN
            new_color = COLORS[current_index][color_index_line]
            screen.fill(new_color)
            pygame.display.update()
            return current_index

    while True:  # EVENT LOOP
        for event in pygame.event.get():
            if not event.type == pygame.KEYUP:
                continue

            if event.key == pygame.K_a:
                color_index_line = change_color(color_index_line, -1, True)

            if event.key == pygame.K_d:
                color_index_line = change_color(color_index_line, 1, True)

            if event.key == pygame.K_w:
                color_index_column = change_color(color_index_column, -1, False)

            if event.key == pygame.K_s:
                color_index_column = change_color(color_index_column, 1, False)

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        clock.tick(FPS)
        await asyncio.sleep(0)

if __name__ == '__main__':
    asyncio.run(main())
