import pygame
import random
import json
import os
from db import create_tables, save_result, get_top_scores, get_personal_best


pygame.init()

WIDTH = 700
HEIGHT = 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 26)
small_font = pygame.font.SysFont("Arial", 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
DARK_RED = (100, 0, 0)
BLUE = (0, 120, 255)
YELLOW = (230, 230, 0)
PURPLE = (130, 0, 180)
ORANGE = (255, 140, 0)


def load_settings():
    if not os.path.exists("settings.json"):
        data = {
            "snake_color": [0, 200, 0],
            "grid": True,
            "sound": True
        }
        save_settings(data)
        return data

    with open("settings.json", "r") as file:
        return json.load(file)


def save_settings(data):
    with open("settings.json", "w") as file:
        json.dump(data, file, indent=4)


def draw_text(text, x, y, color=BLACK, fnt=font):
    img = fnt.render(text, True, color)
    screen.blit(img, (x, y))


def draw_button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, GRAY, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    draw_text(text, x + 20, y + 12)
    return rect


def random_cell(snake, food, poison, powerup, obstacles):
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(60, HEIGHT, CELL)
        pos = [x, y]

        if pos not in snake and pos != food and pos != poison and pos != powerup and pos not in obstacles:
            return pos


def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, (220, 220, 220), (x, 60), (x, HEIGHT))
    for y in range(60, HEIGHT, CELL):
        pygame.draw.line(screen, (220, 220, 220), (0, y), (WIDTH, y))


def username_menu():
    username = ""

    while True:
        screen.fill(WHITE)
        draw_text("Enter username:", 230, 180)
        pygame.draw.rect(screen, GRAY, (220, 230, 260, 45))
        draw_text(username, 235, 238)
        draw_text("Press ENTER to continue", 210, 310, BLACK, small_font)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if username.strip() != "":
                        return username.strip()

                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

                else:
                    if len(username) < 15:
                        username += event.unicode


def main_menu(username):
    while True:
        screen.fill(WHITE)

        draw_text("SNAKE GAME", 260, 100)
        draw_text("Player: " + username, 260, 145, BLACK, small_font)

        play_btn = draw_button("Play", 250, 210, 200, 50)
        lead_btn = draw_button("Leaderboard", 250, 280, 200, 50)
        set_btn = draw_button("Settings", 250, 350, 200, 50)
        quit_btn = draw_button("Quit", 250, 420, 200, 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(event.pos):
                    play_game(username)
                elif lead_btn.collidepoint(event.pos):
                    leaderboard_screen()
                elif set_btn.collidepoint(event.pos):
                    settings_screen()
                elif quit_btn.collidepoint(event.pos):
                    pygame.quit()
                    exit()


def leaderboard_screen():
    while True:
        screen.fill(WHITE)
        draw_text("LEADERBOARD TOP 10", 220, 40)

        rows = get_top_scores()

        draw_text("Rank", 40, 100, BLACK, small_font)
        draw_text("Name", 110, 100, BLACK, small_font)
        draw_text("Score", 260, 100, BLACK, small_font)
        draw_text("Level", 360, 100, BLACK, small_font)
        draw_text("Date", 460, 100, BLACK, small_font)

        y = 135
        rank = 1

        for row in rows:
            username = row[0]
            score = row[1]
            level = row[2]
            date = str(row[3])[:16]

            draw_text(str(rank), 40, y, BLACK, small_font)
            draw_text(username, 110, y, BLACK, small_font)
            draw_text(str(score), 260, y, BLACK, small_font)
            draw_text(str(level), 360, y, BLACK, small_font)
            draw_text(date, 460, y, BLACK, small_font)

            y += 35
            rank += 1

        back_btn = draw_button("Back", 250, 520, 200, 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    return


def settings_screen():
    settings = load_settings()

    colors = [
        [0, 200, 0],
        [0, 120, 255],
        [255, 140, 0],
        [130, 0, 180]
    ]

    color_index = 0

    while True:
        screen.fill(WHITE)

        draw_text("SETTINGS", 280, 60)

        grid_text = "Grid: ON" if settings["grid"] else "Grid: OFF"
        sound_text = "Sound: ON" if settings["sound"] else "Sound: OFF"

        grid_btn = draw_button(grid_text, 230, 160, 240, 50)
        sound_btn = draw_button(sound_text, 230, 230, 240, 50)
        color_btn = draw_button("Change Snake Color", 230, 300, 240, 50)
        save_btn = draw_button("Save & Back", 230, 430, 240, 50)

        pygame.draw.rect(screen, settings["snake_color"], (330, 370, 40, 40))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if grid_btn.collidepoint(event.pos):
                    settings["grid"] = not settings["grid"]

                elif sound_btn.collidepoint(event.pos):
                    settings["sound"] = not settings["sound"]

                elif color_btn.collidepoint(event.pos):
                    color_index += 1
                    if color_index >= len(colors):
                        color_index = 0
                    settings["snake_color"] = colors[color_index]

                elif save_btn.collidepoint(event.pos):
                    save_settings(settings)
                    return


def make_obstacles(snake, level):
    obstacles = []

    if level < 3:
        return obstacles

    count = level + 2

    while len(obstacles) < count:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(80, HEIGHT, CELL)
        block = [x, y]

        head = snake[0]
        too_close = abs(block[0] - head[0]) <= CELL * 2 and abs(block[1] - head[1]) <= CELL * 2

        if block not in snake and not too_close and block not in obstacles:
            obstacles.append(block)

    return obstacles


def play_game(username):
    settings = load_settings()

    snake_color = tuple(settings["snake_color"])
    personal_best = get_personal_best(username)

    snake = [[300, 300], [280, 300], [260, 300]]
    direction = "RIGHT"

    food = [400, 300]
    food_weight = 1
    food_time = pygame.time.get_ticks()

    poison = [200, 300]

    powerup = None
    powerup_type = None
    powerup_spawn_time = 0

    active_power = None
    active_power_start = 0
    shield = False

    score = 0
    level = 1
    speed = 8

    obstacles = []

    running = True

    while running:
        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        head = snake[0].copy()

        if direction == "UP":
            head[1] -= CELL
        elif direction == "DOWN":
            head[1] += CELL
        elif direction == "LEFT":
            head[0] -= CELL
        elif direction == "RIGHT":
            head[0] += CELL

        snake.insert(0, head)

        ate_food = False

        if head == food:
            score += food_weight
            ate_food = True
            food_weight = random.choice([1, 2, 3])
            food = random_cell(snake, food, poison, powerup, obstacles)
            food_time = now

            old_level = level
            level = score // 5 + 1

            if level != old_level:
                obstacles = make_obstacles(snake, level)

        if not ate_food:
            snake.pop()

        if now - food_time > 7000:
            food = random_cell(snake, food, poison, powerup, obstacles)
            food_weight = random.choice([1, 2, 3])
            food_time = now

        if head == poison:
            if len(snake) > 0:
                snake.pop()
            if len(snake) > 0:
                snake.pop()

            poison = random_cell(snake, food, poison, powerup, obstacles)

            if len(snake) <= 1:
                save_result(username, score, level)
                game_over_screen(username, score, level, personal_best)
                return

        if powerup is None and random.randint(1, 120) == 1:
            powerup = random_cell(snake, food, poison, powerup, obstacles)
            powerup_type = random.choice(["speed", "slow", "shield"])
            powerup_spawn_time = now

        if powerup is not None:
            if now - powerup_spawn_time > 8000:
                powerup = None
                powerup_type = None

        if powerup is not None and head == powerup:
            active_power = powerup_type
            active_power_start = now

            if active_power == "shield":
                shield = True

            powerup = None
            powerup_type = None

        speed = 8 + level

        if active_power == "speed":
            speed += 5
            if now - active_power_start > 5000:
                active_power = None

        elif active_power == "slow":
            speed -= 4
            if speed < 4:
                speed = 4
            if now - active_power_start > 5000:
                active_power = None

        hit_wall = head[0] < 0 or head[0] >= WIDTH or head[1] < 60 or head[1] >= HEIGHT
        hit_self = head in snake[1:]
        hit_obstacle = head in obstacles

        if hit_wall or hit_self or hit_obstacle:
            if shield:
                shield = False
                active_power = None

                if hit_wall:
                    snake[0] = [300, 300]
                else:
                    snake.pop(0)
            else:
                save_result(username, score, level)
                game_over_screen(username, score, level, personal_best)
                return

        screen.fill(WHITE)

        if settings["grid"]:
            draw_grid()

        pygame.draw.rect(screen, BLACK, (0, 55, WIDTH, 5))

        draw_text("Score: " + str(score), 10, 15, BLACK, small_font)
        draw_text("Level: " + str(level), 130, 15, BLACK, small_font)
        draw_text("Best: " + str(personal_best), 240, 15, BLACK, small_font)

        if active_power:
            draw_text("Power: " + active_power, 360, 15, BLACK, small_font)

        if shield:
            draw_text("Shield ready", 510, 15, BLACK, small_font)

        for part in snake:
            pygame.draw.rect(screen, snake_color, (part[0], part[1], CELL, CELL))

        pygame.draw.rect(screen, RED, (food[0], food[1], CELL, CELL))
        draw_text(str(food_weight), food[0] + 5, food[1] - 2, WHITE, small_font)

        pygame.draw.rect(screen, DARK_RED, (poison[0], poison[1], CELL, CELL))

        for block in obstacles:
            pygame.draw.rect(screen, BLACK, (block[0], block[1], CELL, CELL))

        if powerup is not None:
            if powerup_type == "speed":
                color = YELLOW
            elif powerup_type == "slow":
                color = BLUE
            else:
                color = PURPLE

            pygame.draw.rect(screen, color, (powerup[0], powerup[1], CELL, CELL))

        pygame.display.update()
        clock.tick(speed)


def game_over_screen(username, score, level, old_best):
    new_best = get_personal_best(username)

    while True:
        screen.fill(WHITE)

        draw_text("GAME OVER", 260, 110)
        draw_text("Final score: " + str(score), 250, 180)
        draw_text("Level reached: " + str(level), 250, 220)
        draw_text("Personal best: " + str(new_best), 250, 260)

        retry_btn = draw_button("Retry", 250, 350, 200, 50)
        menu_btn = draw_button("Main Menu", 250, 420, 200, 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_btn.collidepoint(event.pos):
                    play_game(username)
                    return
                elif menu_btn.collidepoint(event.pos):
                    return


def main():
    create_tables()
    username = username_menu()
    main_menu(username)