import pygame
import sys

pygame.init()

# ---------------------------
# SETTINGS
# ---------------------------
WIDTH = 1000
HEIGHT = 700
TOOLBAR_HEIGHT = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 215, 0)
GRAY = (180, 180, 180)
DARKGRAY = (90, 90, 90)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 20)

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

# ---------------------------
# TOOLS AND COLORS
# ---------------------------
current_tool = "brush"
current_color = BLACK
brush_size = 6

drawing = False
start_pos = None
last_pos = None

tool_buttons = {
    "brush": pygame.Rect(20, 20, 100, 40),
    "rect": pygame.Rect(140, 20, 100, 40),
    "circle": pygame.Rect(260, 20, 100, 40),
    "eraser": pygame.Rect(380, 20, 100, 40),
}

color_buttons = {
    BLACK: pygame.Rect(550, 20, 40, 40),
    RED: pygame.Rect(600, 20, 40, 40),
    GREEN: pygame.Rect(650, 20, 40, 40),
    BLUE: pygame.Rect(700, 20, 40, 40),
    YELLOW: pygame.Rect(750, 20, 40, 40),
}

# ---------------------------
# DRAW UI
# ---------------------------
def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))

    # Кнопки инструментов
    for tool_name, rect in tool_buttons.items():
        color = DARKGRAY if current_tool == tool_name else WHITE
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        text = font.render(tool_name, True, BLACK)
        screen.blit(text, (rect.x + 15, rect.y + 10))

    # Кнопки цветов
    for color_value, rect in color_buttons.items():
        pygame.draw.rect(screen, color_value, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    # Показ текущего цвета
    pygame.draw.rect(screen, current_color, (850, 20, 50, 50))
    pygame.draw.rect(screen, BLACK, (850, 20, 50, 50), 2)

# ---------------------------
# MAIN LOOP
# ---------------------------
while True:
    screen.fill(WHITE)
    draw_toolbar()
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # Проверка кнопок инструментов
            for tool_name, rect in tool_buttons.items():
                if rect.collidepoint(mouse_pos):
                    current_tool = tool_name

            # Проверка кнопок цветов
            for color_value, rect in color_buttons.items():
                if rect.collidepoint(mouse_pos):
                    current_color = color_value

            # Если нажали на холст
            if mouse_pos[1] > TOOLBAR_HEIGHT:
                drawing = True
                start_pos = (mouse_pos[0], mouse_pos[1] - TOOLBAR_HEIGHT)
                last_pos = start_pos

                # Для кисти и ластика можно сразу рисовать точку
                if current_tool == "brush":
                    pygame.draw.circle(canvas, current_color, start_pos, brush_size)
                elif current_tool == "eraser":
                    pygame.draw.circle(canvas, WHITE, start_pos, 15)

        # Отпустили мышь
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos is not None:
                end_pos = (event.pos[0], event.pos[1] - TOOLBAR_HEIGHT)

                # Рисование прямоугольника
                if current_tool == "rect":
                    x = min(start_pos[0], end_pos[0])
                    y = min(start_pos[1], end_pos[1])
                    w = abs(start_pos[0] - end_pos[0])
                    h = abs(start_pos[1] - end_pos[1])
                    pygame.draw.rect(canvas, current_color, (x, y, w, h), 2)

                # Рисование круга
                elif current_tool == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

            drawing = False
            start_pos = None
            last_pos = None

        # Движение мыши при зажатой кнопке
        if event.type == pygame.MOUSEMOTION and drawing:
            current_pos = (event.pos[0], event.pos[1] - TOOLBAR_HEIGHT)

            # Кисть
            if current_tool == "brush":
                pygame.draw.line(canvas, current_color, last_pos, current_pos, brush_size * 2)

            # Ластик
            elif current_tool == "eraser":
                pygame.draw.line(canvas, WHITE, last_pos, current_pos, 30)

            last_pos = current_pos

    pygame.display.update()
    clock.tick(60)