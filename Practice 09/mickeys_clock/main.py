import pygame
from clock import MickeyClock


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Mickey's Clock")

    app = MickeyClock(screen)
    timer = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        app.draw()
        timer.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()