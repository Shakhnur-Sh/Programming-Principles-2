import pygame
import random
import sys

pygame.init()

# Размер окна
WIDTH = 600
HEIGHT = 600
CELL = 20

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (220, 0, 0)
GRAY = (120, 120, 120)

# Окно игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake")

# Часы
clock = pygame.time.Clock()

# Шрифт
font = pygame.font.SysFont("Verdana", 20)

# Начальная змейка
snake = [(100, 100), (80, 100), (60, 100)]

# Направление движения
dx = 20
dy = 0

# Счёт и уровень
score = 0
level = 1
speed = 8

# Одна стена
wall = pygame.Rect(250, 250, 100, 20)


# Функция для случайной еды
def random_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)

        food_rect = pygame.Rect(x, y, CELL, CELL)

        # Еда не должна быть на змейке
        if (x, y) in snake:
            continue

        # Еда не должна быть на стене
        if wall.colliderect(food_rect):
            continue

        return (x, y)


food = random_food()


# Функция проигрыша
def game_over():
    screen.fill(WHITE)
    text = font.render("Game Over", True, BLACK)
    screen.blit(text, (240, 280))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()


# Главный цикл
while True:
    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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

    # Новая голова змейки
    head_x = snake[0][0] + dx
    head_y = snake[0][1] + dy
    new_head = (head_x, head_y)

    # Проверка выхода за границы
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        game_over()

    # Проверка столкновения с собой
    if new_head in snake:
        game_over()

    # Проверка столкновения со стеной
    head_rect = pygame.Rect(head_x, head_y, CELL, CELL)
    if wall.colliderect(head_rect):
        game_over()

    # Добавляем новую голову
    snake.insert(0, new_head)

    # Проверка еды
    if new_head == food:
        score += 1
        food = random_food()

        # Новый уровень каждые 3 очка
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # Рисуем фон
    screen.fill(WHITE)

    # Рисуем стену
    pygame.draw.rect(screen, GRAY, wall)

    # Рисуем змейку
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL, CELL))

    # Рисуем еду
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL, CELL))

    # Рисуем текст
    score_text = font.render("Score: " + str(score), True, BLACK)
    level_text = font.render("Level: " + str(level), True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (500, 10))

    pygame.display.update()
    clock.tick(speed)