import pygame
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

WHITE = (255, 255, 255)
GREEN = (0, 180, 0)
RED = (220, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 26)

snake = [(100, 100), (80, 100), (60, 100)]
dx = CELL
dy = 0

food_x = random.randrange(0, WIDTH, CELL)
food_y = random.randrange(0, HEIGHT, CELL)
food_weight = random.choice([1, 2, 3])

food_timer = 0
food_limit = 150

score = 0
running = True

while running:
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx = -CELL
                dy = 0
            if event.key == pygame.K_RIGHT and dx == 0:
                dx = CELL
                dy = 0
            if event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -CELL
            if event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = CELL

    # New head position
    head_x = snake[0][0] + dx
    head_y = snake[0][1] + dy
    new_head = (head_x, head_y)

    snake.insert(0, new_head)

    # If snake eats food
    if head_x == food_x and head_y == food_y:
        score += food_weight

        food_x = random.randrange(0, WIDTH, CELL)
        food_y = random.randrange(0, HEIGHT, CELL)
        food_weight = random.choice([1, 2, 3])
        food_timer = 0
    else:
        snake.pop()

    # Food timer
    food_timer += 1

    if food_timer > food_limit:
        food_x = random.randrange(0, WIDTH, CELL)
        food_y = random.randrange(0, HEIGHT, CELL)
        food_weight = random.choice([1, 2, 3])
        food_timer = 0

    # Wall collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False

    # Snake collision with itself
    if new_head in snake[1:]:
        running = False

    # Draw snake
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL, CELL))

    # Draw food
    pygame.draw.rect(screen, RED, (food_x, food_y, CELL, CELL))

    # Text
    score_text = font.render("Score: " + str(score), True, BLACK)
    weight_text = font.render("Food weight: " + str(food_weight), True, BLACK)
    timer_text = font.render("Timer: " + str(food_limit - food_timer), True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(weight_text, (10, 40))
    screen.blit(timer_text, (10, 70))

    pygame.display.update()
    clock.tick(10)

pygame.quit()