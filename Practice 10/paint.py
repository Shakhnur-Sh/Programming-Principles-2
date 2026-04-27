import pygame
import sys

pygame.init()

# Размер окна
WIDTH = 900
HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 100, 255)
GRAY = (200, 200, 200)

# Окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

# Шрифт
font = pygame.font.SysFont("Verdana", 20)

# Холст
screen.fill(WHITE)

# Начальные значения
tool = "brush"
color = BLACK
drawing = False
start_pos = None
last_pos = None

# Главный цикл
while True:
    # Верхняя панель
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 50))

    # Текст подсказки
    info1 = font.render("B-brush  R-rect  C-circle  E-eraser", True, BLACK)
    info2 = font.render("1-black  2-red  3-green  4-blue", True, BLACK)
    screen.blit(info1, (10, 5))
    screen.blit(info2, (10, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Нажатия клавиш для инструментов
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_c:
                tool = "circle"
            if event.key == pygame.K_e:
                tool = "eraser"

            # Нажатия клавиш для цвета
            if event.key == pygame.K_1:
                color = BLACK
            if event.key == pygame.K_2:
                color = RED
            if event.key == pygame.K_3:
                color = GREEN
            if event.key == pygame.K_4:
                color = BLUE

        # Нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] > 50:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos

                # Сразу поставить точку кистью
                if tool == "brush":
                    pygame.draw.circle(screen, color, event.pos, 5)

                # Сразу поставить точку ластиком
                if tool == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, 12)

        # Движение мыши
        if event.type == pygame.MOUSEMOTION and drawing:
            if event.pos[1] > 50:
                if tool == "brush":
                    pygame.draw.line(screen, color, last_pos, event.pos, 10)

                if tool == "eraser":
                    pygame.draw.line(screen, WHITE, last_pos, event.pos, 25)

                last_pos = event.pos

        # Отпускание мыши
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos is not None and event.pos[1] > 50:
                end_pos = event.pos

                # Прямоугольник
                if tool == "rect":
                    x = min(start_pos[0], end_pos[0])
                    y = min(start_pos[1], end_pos[1])
                    w = abs(start_pos[0] - end_pos[0])
                    h = abs(start_pos[1] - end_pos[1])
                    pygame.draw.rect(screen, color, (x, y, w, h), 2)

                # Круг
                if tool == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, radius, 2)

            drawing = False
            start_pos = None
            last_pos = None

    pygame.display.update()