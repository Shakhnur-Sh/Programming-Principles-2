import pygame
from ball import Ball


def main():
    pygame.init()

    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Moving Ball")

    ball = Ball(width, height)
    timer = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball.move_left()
                elif event.key == pygame.K_RIGHT:
                    ball.move_right()
                elif event.key == pygame.K_UP:
                    ball.move_up()
                elif event.key == pygame.K_DOWN:
                    ball.move_down()

        screen.fill((255, 255, 255))
        ball.draw(screen)

        pygame.display.flip()
        timer.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()