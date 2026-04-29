import pygame
import random
import time
from persistence import save_score

WIDTH = 500
HEIGHT = 700

ROAD_LEFT = 70
ROAD_RIGHT = 430
LANES = [115, 205, 295, 385]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ROAD = (70, 70, 70)
YELLOW = (255, 220, 0)
RED = (200, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 180, 0)
ORANGE = (255, 130, 0)
PURPLE = (150, 0, 200)
GRAY = (120, 120, 120)


def get_car_color(name):
    if name == "red":
        return RED
    if name == "green":
        return GREEN
    return BLUE


def draw_text(screen, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont("Arial", size)
    image = font.render(text, True, color)
    screen.blit(image, (x, y))


def safe_x(player_rect):
    lane = random.choice(LANES)
    x = lane - 20

    while abs(x - player_rect.x) < 70:
        lane = random.choice(LANES)
        x = lane - 20

    return x


def play_game(screen, username, settings):
    clock = pygame.time.Clock()

    player = pygame.Rect(225, 580, 45, 75)

    cars = []
    obstacles = []
    coins_list = []
    powers = []
    events = []

    coins = 0
    distance = 0
    finish_distance = 3000

    shield = False
    active_power = "None"
    power_end_time = 0

    spawn_timer = 0
    coin_timer = 0
    power_timer = 0
    event_timer = 0

    base_speed = 5

    if settings["difficulty"] == "easy":
        base_speed = 4
    elif settings["difficulty"] == "hard":
        base_speed = 7

    car_color = get_car_color(settings["car_color"])

    running = True
    game_over = False

    while running:
        screen.fill((30, 130, 30))

        pygame.draw.rect(screen, ROAD, (ROAD_LEFT, 0, ROAD_RIGHT - ROAD_LEFT, HEIGHT))

        for x in LANES:
            pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT), 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        move_speed = 6

        if active_power == "Nitro":
            move_speed = 9

        if keys[pygame.K_LEFT] and player.left > ROAD_LEFT:
            player.x -= move_speed

        if keys[pygame.K_RIGHT] and player.right < ROAD_RIGHT:
            player.x += move_speed

        if keys[pygame.K_UP] and player.top > 0:
            player.y -= move_speed

        if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
            player.y += move_speed

        distance += 1

        level_bonus = distance // 500
        speed = base_speed + level_bonus

        spawn_timer += 1
        coin_timer += 1
        power_timer += 1
        event_timer += 1

        spawn_limit = 70 - level_bonus * 5
        if spawn_limit < 30:
            spawn_limit = 30

        if spawn_timer > spawn_limit:
            spawn_timer = 0

            kind = random.choice(["car", "obstacle", "oil", "pothole"])

            x = safe_x(player)

            if kind == "car":
                cars.append(pygame.Rect(x, -90, 45, 75))
            else:
                obstacles.append([pygame.Rect(x, -50, 45, 45), kind])

        if coin_timer > 80:
            coin_timer = 0
            x = safe_x(player)
            coins_list.append(pygame.Rect(x + 10, -30, 25, 25))

        if power_timer > 350:
            power_timer = 0
            x = safe_x(player)
            p_type = random.choice(["Nitro", "Shield", "Repair"])
            powers.append([pygame.Rect(x, -40, 35, 35), p_type, time.time()])

        if event_timer > 450:
            event_timer = 0
            x = random.choice(LANES) - 35
            events.append([pygame.Rect(x, -50, 70, 25), "barrier"])

        for car in cars[:]:
            car.y += speed
            pygame.draw.rect(screen, RED, car)

            if car.top > HEIGHT:
                cars.remove(car)

            if player.colliderect(car):
                if shield:
                    shield = False
                    active_power = "None"
                    cars.remove(car)
                else:
                    game_over = True

        for item in obstacles[:]:
            rect = item[0]
            kind = item[1]
            rect.y += speed

            if kind == "oil":
                color = BLACK
            elif kind == "pothole":
                color = GRAY
            else:
                color = ORANGE

            pygame.draw.rect(screen, color, rect)

            if rect.top > HEIGHT:
                obstacles.remove(item)

            if player.colliderect(rect):
                if shield:
                    shield = False
                    active_power = "None"
                    obstacles.remove(item)
                else:
                    if kind == "oil":
                        player.y += 35
                        obstacles.remove(item)
                    else:
                        game_over = True

        for coin in coins_list[:]:
            coin.y += speed
            pygame.draw.circle(screen, YELLOW, coin.center, 13)

            if coin.top > HEIGHT:
                coins_list.remove(coin)

            if player.colliderect(coin):
                coins += 1
                coins_list.remove(coin)

        for p in powers[:]:
            rect = p[0]
            p_type = p[1]
            born_time = p[2]

            rect.y += speed

            if p_type == "Nitro":
                color = PURPLE
            elif p_type == "Shield":
                color = BLUE
            else:
                color = GREEN

            pygame.draw.rect(screen, color, rect)

            if time.time() - born_time > 6:
                powers.remove(p)

            elif player.colliderect(rect):
                if active_power == "None":
                    active_power = p_type

                    if p_type == "Nitro":
                        power_end_time = time.time() + 4

                    elif p_type == "Shield":
                        shield = True

                    elif p_type == "Repair":
                        if len(obstacles) > 0:
                            obstacles.pop(0)
                        active_power = "None"

                powers.remove(p)

        for e in events[:]:
            rect = e[0]
            rect.y += speed + 1
            rect.x += random.choice([-1, 1])

            pygame.draw.rect(screen, (90, 30, 30), rect)

            if rect.top > HEIGHT:
                events.remove(e)

            if player.colliderect(rect):
                if shield:
                    shield = False
                    active_power = "None"
                    events.remove(e)
                else:
                    game_over = True

        if active_power == "Nitro":
            if time.time() > power_end_time:
                active_power = "None"

        pygame.draw.rect(screen, car_color, player)

        score = coins * 10 + distance + level_bonus * 20

        remaining = finish_distance - distance
        if remaining < 0:
            remaining = 0

        draw_text(screen, "Name: " + username, 20, 10, 10)
        draw_text(screen, "Score: " + str(score), 20, 10, 35)
        draw_text(screen, "Coins: " + str(coins), 20, 10, 60)
        draw_text(screen, "Distance: " + str(distance), 20, 10, 85)
        draw_text(screen, "Remaining: " + str(remaining), 20, 10, 110)
        draw_text(screen, "Power: " + active_power, 20, 10, 135)

        if active_power == "Nitro":
            left = int(power_end_time - time.time())
            draw_text(screen, "Time: " + str(left), 20, 10, 160)

        if shield:
            draw_text(screen, "Shield ready", 20, 10, 185)

        pygame.display.update()
        clock.tick(60)

        if game_over or distance >= finish_distance:
            save_score(username, score, distance)
            return score, distance, coins