import pygame
from datetime import datetime
from tools import draw_toolbar, flood_fill

pygame.init()

WIDTH = 900
HEIGHT = 600
TOOLBAR_HEIGHT = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 180, 0)
WHITE = (255, 255, 255)

current_color = BLACK
current_tool = "pencil"
brush_size = 2

drawing = False
start_pos = None
last_pos = None

text_mode = False
text_position = None
typed_text = ""
font = pygame.font.SysFont("Arial", 28)

running = True

while running:
    screen.fill((255, 255, 255))
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))

    mouse_pos = pygame.mouse.get_pos()
    canvas_mouse_pos = (mouse_pos[0], mouse_pos[1] - TOOLBAR_HEIGHT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                current_tool = "pencil"
            elif event.key == pygame.K_l:
                current_tool = "line"
            elif event.key == pygame.K_r:
                current_tool = "rectangle"
            elif event.key == pygame.K_c:
                current_tool = "circle"
            elif event.key == pygame.K_s:
                current_tool = "square"
            elif event.key == pygame.K_t:
                current_tool = "triangle"
            elif event.key == pygame.K_e:
                current_tool = "equilateral"
            elif event.key == pygame.K_h:
                current_tool = "rhombus"
            elif event.key == pygame.K_f:
                current_tool = "fill"
            elif event.key == pygame.K_x:
                current_tool = "text"

            elif event.key == pygame.K_1:
                brush_size = 2
            elif event.key == pygame.K_2:
                brush_size = 5
            elif event.key == pygame.K_3:
                brush_size = 10

            elif event.key == pygame.K_b:
                current_color = BLACK
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_u:
                current_color = BLUE
            elif event.key == pygame.K_d:
                current_color = RED

            # Ctrl + S save
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                now = datetime.now()
                filename = "paint_" + now.strftime("%Y%m%d_%H%M%S") + ".png"
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            # Text typing
            if text_mode:
                if event.key == pygame.K_RETURN:
                    text_surface = font.render(typed_text, True, current_color)
                    canvas.blit(text_surface, text_position)
                    text_mode = False
                    typed_text = ""

                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    typed_text = ""

                elif event.key == pygame.K_BACKSPACE:
                    typed_text = typed_text[:-1]

                else:
                    typed_text += event.unicode

        # Mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos[1] > TOOLBAR_HEIGHT:
                drawing = True
                start_pos = canvas_mouse_pos
                last_pos = canvas_mouse_pos

                if current_tool == "fill":
                    flood_fill(canvas, canvas_mouse_pos[0], canvas_mouse_pos[1], current_color)

                elif current_tool == "text":
                    text_mode = True
                    text_position = canvas_mouse_pos
                    typed_text = ""

        # Mouse moving
        if event.type == pygame.MOUSEMOTION:
            if drawing and current_tool == "pencil":
                pygame.draw.line(canvas, current_color, last_pos, canvas_mouse_pos, brush_size)
                last_pos = canvas_mouse_pos

        # Mouse up
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = canvas_mouse_pos

                if current_tool == "line":
                    pygame.draw.line(canvas, current_color, start_pos, end_pos, brush_size)

                elif current_tool == "rectangle":
                    x1 = start_pos[0]
                    y1 = start_pos[1]
                    x2 = end_pos[0]
                    y2 = end_pos[1]

                    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(canvas, current_color, rect, brush_size)

                elif current_tool == "circle":
                    x1 = start_pos[0]
                    y1 = start_pos[1]
                    x2 = end_pos[0]
                    y2 = end_pos[1]

                    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, radius, brush_size)

                elif current_tool == "square":
                    x1 = start_pos[0]
                    y1 = start_pos[1]
                    x2 = end_pos[0]
                    y2 = end_pos[1]

                    size = min(abs(x2 - x1), abs(y2 - y1))
                    rect = pygame.Rect(x1, y1, size, size)
                    pygame.draw.rect(canvas, current_color, rect, brush_size)

                elif current_tool == "triangle":
                    x1 = start_pos[0]
                    y1 = start_pos[1]
                    x2 = end_pos[0]
                    y2 = end_pos[1]

                    points = [(x1, y1), (x1, y2), (x2, y2)]
                    pygame.draw.polygon(canvas, current_color, points, brush_size)

                elif current_tool == "equilateral":
                    x1 = start_pos[0]
                    y1 = start_pos[1]
                    x2 = end_pos[0]
                    y2 = end_pos[1]

                    points = [(x1, y2), ((x1 + x2) // 2, y1), (x2, y2)]
                    pygame.draw.polygon(canvas, current_color, points, brush_size)

                elif current_tool == "rhombus":
                    x1 = start_pos[0]
                    y1 = start_pos[1]
                    x2 = end_pos[0]
                    y2 = end_pos[1]

                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2

                    points = [
                        (center_x, y1),
                        (x2, center_y),
                        (center_x, y2),
                        (x1, center_y)
                    ]

                    pygame.draw.polygon(canvas, current_color, points, brush_size)

            drawing = False

    # Live preview while dragging
    if drawing and current_tool != "pencil" and current_tool != "fill" and current_tool != "text":
        preview = canvas.copy()

        end_pos = canvas_mouse_pos

        if current_tool == "line":
            pygame.draw.line(preview, current_color, start_pos, end_pos, brush_size)

        elif current_tool == "rectangle":
            rect = pygame.Rect(
                min(start_pos[0], end_pos[0]),
                min(start_pos[1], end_pos[1]),
                abs(end_pos[0] - start_pos[0]),
                abs(end_pos[1] - start_pos[1])
            )
            pygame.draw.rect(preview, current_color, rect, brush_size)

        elif current_tool == "circle":
            radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
            pygame.draw.circle(preview, current_color, start_pos, radius, brush_size)

        elif current_tool == "square":
            size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
            rect = pygame.Rect(start_pos[0], start_pos[1], size, size)
            pygame.draw.rect(preview, current_color, rect, brush_size)

        elif current_tool == "triangle":
            points = [(start_pos[0], start_pos[1]), (start_pos[0], end_pos[1]), (end_pos[0], end_pos[1])]
            pygame.draw.polygon(preview, current_color, points, brush_size)

        elif current_tool == "equilateral":
            points = [(start_pos[0], end_pos[1]), ((start_pos[0] + end_pos[0]) // 2, start_pos[1]), (end_pos[0], end_pos[1])]
            pygame.draw.polygon(preview, current_color, points, brush_size)

        elif current_tool == "rhombus":
            center_x = (start_pos[0] + end_pos[0]) // 2
            center_y = (start_pos[1] + end_pos[1]) // 2

            points = [
                (center_x, start_pos[1]),
                (end_pos[0], center_y),
                (center_x, end_pos[1]),
                (start_pos[0], center_y)
            ]

            pygame.draw.polygon(preview, current_color, points, brush_size)

        screen.blit(preview, (0, TOOLBAR_HEIGHT))

    # Text preview
    if text_mode:
        text_surface = font.render(typed_text, True, current_color)
        screen.blit(text_surface, (text_position[0], text_position[1] + TOOLBAR_HEIGHT))

    draw_toolbar(screen, current_tool, current_color, brush_size)

    pygame.display.update()
    clock.tick(60)

pygame.quit()