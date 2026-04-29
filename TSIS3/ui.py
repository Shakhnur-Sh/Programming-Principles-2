import pygame
from persistence import load_leaderboard, save_settings

WIDTH = 500
HEIGHT = 700

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
DARK = (40, 40, 40)
GREEN = (0, 180, 0)


def draw_text(screen, text, size, x, y, color=BLACK):
    font = pygame.font.SysFont("Arial", size)
    image = font.render(text, True, color)
    screen.blit(image, (x, y))


def button(screen, text, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, w, h)

    if rect.collidepoint(mouse):
        pygame.draw.rect(screen, GREEN, rect)
        if click[0]:
            pygame.time.delay(200)
            return True
    else:
        pygame.draw.rect(screen, GRAY, rect)

    pygame.draw.rect(screen, BLACK, rect, 2)
    draw_text(screen, text, 28, x + 20, y + 12)
    return False


def get_username(screen):
    name = ""
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        draw_text(screen, "Enter your name:", 32, 120, 200)
        draw_text(screen, name, 32, 120, 260)
        draw_text(screen, "Press ENTER to start", 24, 120, 330)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name != "":
                    return name

                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                else:
                    if len(name) < 10:
                        name += event.unicode

        clock.tick(30)


def main_menu(screen):
    while True:
        screen.fill(WHITE)
        draw_text(screen, "RACER GAME", 45, 115, 100)

        if button(screen, "Play", 150, 220, 200, 60):
            return "play"

        if button(screen, "Leaderboard", 150, 300, 200, 60):
            return "leaderboard"

        if button(screen, "Settings", 150, 380, 200, 60):
            return "settings"

        if button(screen, "Quit", 150, 460, 200, 60):
            pygame.quit()
            quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()


def leaderboard_screen(screen):
    while True:
        screen.fill(WHITE)
        draw_text(screen, "TOP 10 SCORES", 36, 120, 50)

        scores = load_leaderboard()

        y = 120
        rank = 1

        for item in scores:
            line = str(rank) + ". " + item["name"] + " | Score: " + str(item["score"]) + " | Dist: " + str(item["distance"])
            draw_text(screen, line, 22, 40, y)
            y += 40
            rank += 1

        if button(screen, "Back", 160, 600, 180, 50):
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()


def settings_screen(screen, settings):
    colors = ["blue", "red", "green"]
    difficulties = ["easy", "normal", "hard"]

    while True:
        screen.fill(WHITE)

        draw_text(screen, "SETTINGS", 40, 150, 60)
        draw_text(screen, "Sound: " + str(settings["sound"]), 26, 120, 160)
        draw_text(screen, "Car color: " + settings["car_color"], 26, 120, 240)
        draw_text(screen, "Difficulty: " + settings["difficulty"], 26, 120, 320)

        if button(screen, "Toggle Sound", 140, 190, 220, 45):
            settings["sound"] = not settings["sound"]
            save_settings(settings)

        if button(screen, "Change Color", 140, 270, 220, 45):
            i = colors.index(settings["car_color"])
            settings["car_color"] = colors[(i + 1) % len(colors)]
            save_settings(settings)

        if button(screen, "Change Difficulty", 140, 350, 220, 45):
            i = difficulties.index(settings["difficulty"])
            settings["difficulty"] = difficulties[(i + 1) % len(difficulties)]
            save_settings(settings)

        if button(screen, "Back", 160, 600, 180, 50):
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()


def game_over_screen(screen, score, distance, coins):
    while True:
        screen.fill(WHITE)

        draw_text(screen, "GAME OVER", 45, 120, 120)
        draw_text(screen, "Score: " + str(score), 28, 160, 220)
        draw_text(screen, "Distance: " + str(distance), 28, 160, 260)
        draw_text(screen, "Coins: " + str(coins), 28, 160, 300)

        if button(screen, "Retry", 150, 400, 200, 60):
            return "retry"

        if button(screen, "Main Menu", 150, 480, 200, 60):
            return "menu"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()