import pygame


def draw_toolbar(screen, current_tool, current_color, brush_size):
    pygame.draw.rect(screen, (220, 220, 220), (0, 0, 900, 60))

    font = pygame.font.SysFont("Arial", 18)

    text1 = font.render("Tools: P Pencil | L Line | R Rect | C Circle | S Square | T Triangle | E Equilateral | H Rhombus | F Fill | X Text", True, (0, 0, 0))
    text2 = font.render("Sizes: 1 Small | 2 Medium | 3 Large     Ctrl+S Save", True, (0, 0, 0))
    text3 = font.render("Current: " + current_tool + " | Size: " + str(brush_size), True, current_color)

    screen.blit(text1, (10, 5))
    screen.blit(text2, (10, 27))
    screen.blit(text3, (650, 27))


def flood_fill(canvas, x, y, new_color):
    old_color = canvas.get_at((x, y))

    if old_color == new_color:
        return

    width = canvas.get_width()
    height = canvas.get_height()

    pixels = [(x, y)]

    while len(pixels) > 0:
        px, py = pixels.pop()

        if px < 0 or px >= width or py < 0 or py >= height:
            continue

        if canvas.get_at((px, py)) != old_color:
            continue

        canvas.set_at((px, py), new_color)

        pixels.append((px + 1, py))
        pixels.append((px - 1, py))
        pixels.append((px, py + 1))
        pixels.append((px, py - 1))