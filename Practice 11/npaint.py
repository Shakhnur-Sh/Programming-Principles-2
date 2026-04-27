import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 180, 0)
PURPLE = (160, 0, 200)

screen.fill(WHITE)

clock = pygame.time.Clock()

color = BLACK
tool = "square"

start_pos = None
drawing = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = "square"
            if event.key == pygame.K_2:
                tool = "right_triangle"
            if event.key == pygame.K_3:
                tool = "equilateral_triangle"
            if event.key == pygame.K_4:
                tool = "rhombus"

            if event.key == pygame.K_r:
                color = RED
            if event.key == pygame.K_b:
                color = BLUE
            if event.key == pygame.K_g:
                color = GREEN
            if event.key == pygame.K_p:
                color = PURPLE
            if event.key == pygame.K_k:
                color = BLACK

            # Clear screen
            if event.key == pygame.K_c:
                screen.fill(WHITE)

        # Start drawing
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            drawing = True

        # Finish drawing
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            drawing = False

            x1, y1 = start_pos
            x2, y2 = end_pos

            width = x2 - x1
            height = y2 - y1

            # Draw square
            if tool == "square":
                size = min(abs(width), abs(height))
                pygame.draw.rect(screen, color, (x1, y1, size, size), 3)

            # Draw right triangle
            if tool == "right_triangle":
                points = [
                    (x1, y1),
                    (x1, y2),
                    (x2, y2)
                ]
                pygame.draw.polygon(screen, color, points, 3)

            # Draw equilateral triangle
            if tool == "equilateral_triangle":
                side = abs(width)
                height_triangle = int(side * math.sqrt(3) / 2)

                points = [
                    (x1, y1 + height_triangle),
                    (x1 + side, y1 + height_triangle),
                    (x1 + side // 2, y1)
                ]

                pygame.draw.polygon(screen, color, points, 3)

            # Draw rhombus
            if tool == "rhombus":
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2

                points = [
                    (center_x, y1),
                    (x2, center_y),
                    (center_x, y2),
                    (x1, center_y)
                ]

                pygame.draw.polygon(screen, color, points, 3)

    pygame.display.update()
    clock.tick(60)

pygame.quit()