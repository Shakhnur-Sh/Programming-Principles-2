import pygame
from player import MusicPlayer


def main():
    pygame.init()

    screen = pygame.display.set_mode((700, 300))
    pygame.display.set_caption("Music Player")

    font = pygame.font.SysFont("Arial", 32)
    small_font = pygame.font.SysFont("Arial", 24)
    timer = pygame.time.Clock()

    player = MusicPlayer()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.previous_track()
                elif event.key == pygame.K_q:
                    running = False

        screen.fill((245, 245, 245))

        title = font.render("Music Player", True, (0, 0, 0))
        screen.blit(title, (260, 30))

        track_text = small_font.render(
            f"Current track: {player.get_current_track_name()}",
            True,
            (0, 0, 180)
        )
        screen.blit(track_text, (170, 100))

        status = "Playing" if player.is_playing and pygame.mixer.music.get_busy() else "Stopped"
        status_text = small_font.render(f"Status: {status}", True, (0, 0, 0))
        screen.blit(status_text, (170, 140))

        pos_text = small_font.render(
            f"Position: {player.get_position_seconds()} sec",
            True,
            (0, 0, 0)
        )
        screen.blit(pos_text, (170, 180))

        controls = small_font.render(
            "P = Play | S = Stop | N = Next | B = Back | Q = Quit",
            True,
            (0, 0, 0)
        )
        screen.blit(controls, (55, 240))

        pygame.display.flip()
        timer.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()