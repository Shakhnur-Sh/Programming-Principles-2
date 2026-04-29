import pygame
from ui import main_menu, leaderboard_screen, settings_screen, game_over_screen, get_username
from racer import play_game
from persistence import load_settings

pygame.init()

WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Racer Game")

settings = load_settings()

while True:
    choice = main_menu(screen)

    if choice == "play":
        username = get_username(screen)

        while True:
            score, distance, coins = play_game(screen, username, settings)
            result = game_over_screen(screen, score, distance, coins)

            if result == "retry":
                continue
            else:
                break

    elif choice == "leaderboard":
        leaderboard_screen(screen)

    elif choice == "settings":
        settings_screen(screen, settings)
        settings = load_settings()