import pygame
import random
import sys

pygame.init()

# Размер окна
WIDTH = 400
HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (220, 0, 0)
YELLOW = (255, 215, 0)

# Окно игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Racer")

# Часы для скорости игры
clock = pygame.time.Clock()

# Шрифт для текста
font = pygame.font.SysFont("Verdana", 20)

# Счёт
score = 0
coins_collected = 0


# ---------------- PLAYER ----------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Простая синяя машинка
        self.image = pygame.Surface((50, 90))
        self.image.fill(BLUE)

        # Прямоугольник машинки
        self.rect = self.image.get_rect()
        self.rect.center = (200, 500)

    def move(self):
        keys = pygame.key.get_pressed()

        # Движение влево
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5

        # Движение вправо
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Ограничения по границам дороги
        if self.rect.left < 50:
            self.rect.left = 50

        if self.rect.right > 350:
            self.rect.right = 350


# ---------------- ENEMY ----------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Красная машинка
        self.image = pygame.Surface((50, 90))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        # Случайная позиция по X внутри дороги
        self.rect.x = random.randint(50, 300)
        self.rect.y = -100

    def move(self):
        global score

        self.rect.y += 5

        # Если враг ушёл вниз, вернуть наверх
        if self.rect.top > HEIGHT:
            self.reset()
            score += 1


# ---------------- COIN ----------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Монета как круг
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (10, 10), 10)

        self.rect = self.image.get_rect()
        self.active = False
        self.timer = 0
        self.delay = random.randint(60, 150)

    def update(self):
        # Если монета пока не активна, ждём
        if not self.active:
            self.timer += 1
            if self.timer >= self.delay:
                self.rect.x = random.randint(60, 320)
                self.rect.y = -20
                self.active = True
                self.timer = 0
                self.delay = random.randint(60, 150)
        else:
            # Если активна, двигается вниз
            self.rect.y += 5

            # Если ушла за экран, исчезает
            if self.rect.top > HEIGHT:
                self.active = False

    def draw(self):
        if self.active:
            screen.blit(self.image, self.rect)


# Создаём объекты
player = Player()
enemy = Enemy()
coin = Coin()

# Группы спрайтов
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(enemy)
enemies.add(enemy)


# ---------------- GAME OVER ----------------
def game_over():
    screen.fill(WHITE)

    text = font.render("Game Over", True, BLACK)
    screen.blit(text, (150, 280))

    pygame.display.update()
    pygame.time.delay(2000)

    pygame.quit()
    sys.exit()


# ---------------- MAIN LOOP ----------------
while True:
    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Движение объектов
    player.move()
    enemy.move()
    coin.update()

    # Столкновение с врагом
    if pygame.sprite.spritecollideany(player, enemies):
        game_over()

    # Сбор монеты
    if coin.active and player.rect.colliderect(coin.rect):
        coins_collected += 1
        coin.active = False

    # Фон
    screen.fill(WHITE)

    # Границы дороги
    pygame.draw.line(screen, BLACK, (50, 0), (50, HEIGHT), 3)
    pygame.draw.line(screen, BLACK, (350, 0), (350, HEIGHT), 3)

    # Рисуем машинки
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)

    # Рисуем монету
    coin.draw()

    # Текст score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Текст coins справа сверху
    coin_text = font.render("Coins: " + str(coins_collected), True, BLACK)
    screen.blit(coin_text, (280, 10))

    # Обновляем экран
    pygame.display.update()
    clock.tick(60)