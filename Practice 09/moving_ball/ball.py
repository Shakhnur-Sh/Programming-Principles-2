import pygame


class Ball:
    def __init__(self, screen_width, screen_height):
        self.radius = 25
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.step = 20
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = (255, 0, 0)

    def move_left(self):
        if self.x - self.step - self.radius >= 0:
            self.x -= self.step

    def move_right(self):
        if self.x + self.step + self.radius <= self.screen_width:
            self.x += self.step

    def move_up(self):
        if self.y - self.step - self.radius >= 0:
            self.y -= self.step

    def move_down(self):
        if self.y + self.step + self.radius <= self.screen_height:
            self.y += self.step

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)