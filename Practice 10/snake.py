import pygame
import random
import sys

pygame.init()

# ---------------------------
# SETTINGS
# ---------------------------
WIDTH = 600
HEIGHT = 600
CELL = 20
FPS = 8

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (220, 0, 0)
GRAY = (100, 100, 100)
BLUE = (0, 120, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 24)

# ---------------------------
# INITIAL STATE
# ---------------------------
snake = [(100, 100), (80, 100), (60, 100)]
dx = CELL
dy = 0

score = 0
level = 1
speed = FPS

# Несколько стен
walls = []
for x in range(0, WIDTH, CELL):
    walls.append((x, 0))
    walls.append((x, HEIGHT - CELL))

for y in range(0, HEIGHT, CELL):
    walls.append((0, y))
    walls.append((WIDTH - CELL, y))

# Внутренние препятствия
for x in range(200, 400, CELL):
    walls.append((x, 200))

for y in range(300, 500, CELL):
    walls.append((300, y))

# ---------------------------
# FOOD GENERATION
# ---------------------------
def random_food():
    while True:
        x = random.randrange(CELL, WIDTH - CELL, CELL)
        y = random.randrange(CELL, HEIGHT - CELL, CELL)

        # Еда не должна быть на змейке и на стенах
        if (x, y) not in snake and (x, y) not in walls:
            return (x, y)

food = random_food()

# ---------------------------
# DRAW FUNCTION
# ---------------------------
def draw_game():
    screen.fill(BLACK)

    # Рисуем стены
    for wall in walls:
        pygame.draw.rect(screen, GRAY, (wall[0], wall[1], CELL, CELL))

    # Рисуем змейку
    for i, segment in enumerate(snake):
        color = BLUE if i == 0 else GREEN
        pygame.draw.rect(screen, color, (segment[0], segment[1], CELL, CELL))

    # Рисуем еду
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL, CELL))

    # Текст score и level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (450, 10))

    pygame.display.update()

# ---------------------------
# GAME OVER
# ---------------------------
def game_over():
    text = font.render("Game Over", True, WHITE)
    screen.fill(BLACK)
    screen.blit(text, (240, 280))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# ---------------------------
# MAIN LOOP
# ---------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Запрещаем разворот на 180 градусов
            if event.key == pygame.K_LEFT and dx == 0:
                dx = -CELL
                dy = 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = CELL
                dy = 0
            elif event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -CELL
            elif event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = CELL

    # Новая голова змейки
    head_x = snake[0][0] + dx
    head_y = snake[0][1] + dy
    new_head = (head_x, head_y)

    # Проверка выхода за границы
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        game_over()

    # Проверка столкновения со своим телом
    if new_head in snake:
        game_over()

    # Проверка столкновения со стенами
    if new_head in walls:
        game_over()

    # Добавляем новую голову
    snake.insert(0, new_head)

    # Проверка еды
    if new_head == food:
        score += 1
        food = random_food()

        # Новый уровень каждые 4 очка
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        # Если еду не съели, хвост убираем
        snake.pop()

    draw_game()
    clock.tick(speed)