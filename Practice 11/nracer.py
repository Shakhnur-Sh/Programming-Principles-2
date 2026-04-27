import pygame
import random

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 220, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

# Player
player = pygame.Rect(180, 500, 40, 60)
player_speed = 6

# Enemy
enemy = pygame.Rect(random.randint(60, 300), -80, 50, 70)
enemy_speed = 5

# Coin
coin = pygame.Rect(random.randint(60, 320), -40, 25, 25)
coin_weight = random.choice([1, 2, 3])

score = 0
coin_count = 0

running = True

while running:
    screen.fill(WHITE)

    # Event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed

    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # Borders
    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    # Enemy movement
    enemy.y += enemy_speed

    if enemy.top > HEIGHT:
        enemy.x = random.randint(60, 300)
        enemy.y = -80

    # Coin movement
    coin.y += 4

    if coin.top > HEIGHT:
        coin.x = random.randint(60, 320)
        coin.y = -40
        coin_weight = random.choice([1, 2, 3])

    # Collision with coin
    if player.colliderect(coin):
        score += coin_weight
        coin_count += 1

        coin.x = random.randint(60, 320)
        coin.y = -40
        coin_weight = random.choice([1, 2, 3])

        # Every 5 coins enemy becomes faster
        if coin_count % 5 == 0:
            enemy_speed += 1

    # Collision with enemy
    if player.colliderect(enemy):
        running = False

    # Drawing
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)
    pygame.draw.ellipse(screen, YELLOW, coin)

    # Text
    score_text = font.render("Score: " + str(score), True, BLACK)
    speed_text = font.render("Enemy speed: " + str(enemy_speed), True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(speed_text, (10, 40))

    pygame.display.update()
    clock.tick(60)

pygame.quit()