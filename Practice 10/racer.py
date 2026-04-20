import pygame
import random
import sys

pygame.init()

# SETTINGS
WIDTH = 400
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (120, 120, 120)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
YELLOW = (255, 215, 0)
BLUE = (0, 100, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 40)

enemy_speed = 6
road_line_y = 0
coins_collected = 0
score = 0

# PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # create a simple car shape using rectangles
        self.image = pygame.Surface((50, 90))
        self.image.fill(BLUE)
        pygame.draw.rect(self.image, BLACK, (5, 10, 40, 70), 3)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 60:
            self.rect.move_ip(-6, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH - 60:
            self.rect.move_ip(6, 0)

# ENEMY CLASS
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 90))
        self.image.fill(RED)
        pygame.draw.rect(self.image, BLACK, (5, 10, 40, 70), 3)

        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        # Враг появляется в одной из дорожных полос
        lane_x = random.choice([100, 200, 300])
        self.rect.center = (lane_x, -100)

    def move(self):
        global score
        self.rect.move_ip(0, enemy_speed)

        if self.rect.top > HEIGHT:
            self.reset_position()
            score += 1

# COIN CLASS
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((24, 24), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (12, 12), 12)
        pygame.draw.circle(self.image, BLACK, (12, 12), 12, 2)

        self.rect = self.image.get_rect()
        self.active = False
        self.spawn_delay = random.randint(60, 180)  # задержка перед появлением
        self.timer = 0

    def update(self):
        if not self.active:
            self.timer += 1
            if self.timer >= self.spawn_delay:
                lane_x = random.choice([100, 200, 300])
                self.rect.center = (lane_x, -20)
                self.active = True
                self.timer = 0
                self.spawn_delay = random.randint(60, 180)
        else:
            self.rect.move_ip(0, enemy_speed)
            if self.rect.top > HEIGHT:
                self.active = False

    def draw(self, surface):
        if self.active:
            surface.blit(self.image, self.rect)

# DRAW ROAD
def draw_road():
    global road_line_y

    screen.fill((30, 30, 30))

    # Дорога
    pygame.draw.rect(screen, GRAY, (50, 0, 300, HEIGHT))

    # Левая и правая граница дороги
    pygame.draw.line(screen, WHITE, (50, 0), (50, HEIGHT), 5)
    pygame.draw.line(screen, WHITE, (350, 0), (350, HEIGHT), 5)

    # Разделительные линии
    for y in range(-40, HEIGHT, 80):
        pygame.draw.rect(screen, WHITE, (195, y + road_line_y, 10, 40))

    road_line_y += enemy_speed
    if road_line_y >= 80:
        road_line_y = 0

# GAME OBJECTS
player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(enemy)
enemies.add(enemy)

# GAME OVER SCREEN
def game_over():
    text = font_big.render("Game Over", True, WHITE)
    screen.fill(BLACK)
    screen.blit(text, (100, 250))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# MAIN LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Движение игрока
    player.move()

    # Движение врага
    enemy.move()

    # Обновление монеты
    coin.update()

    # Проверка столкновения с врагом
    if pygame.sprite.spritecollideany(player, enemies):
        game_over()

    # Проверка сбора монеты
    if coin.active and player.rect.colliderect(coin.rect):
        coins_collected += 1
        coin.active = False

    # Рисуем фон дороги
    draw_road()

    # Рисуем спрайты
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)

    # Рисуем монету, если она активна
    coin.draw(screen)

    # Текст: score слева сверху
    score_text = font_small.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Текст: coins справа сверху
    coin_text = font_small.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(coin_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(FPS)