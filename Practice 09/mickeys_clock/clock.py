import pygame
import math
from datetime import datetime
from pathlib import Path


class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.width = 800
        self.height = 800

        self.bg_color = (240, 240, 240)
        self.clock_center = (self.width // 2, self.height // 2 + 70)

        base_path = Path(__file__).resolve().parent
        images_path = base_path / "images"

        self.clock_face = pygame.image.load(images_path / "clock.png").convert_alpha()
        self.mickey = pygame.image.load(images_path / "mikkey.png").convert_alpha()
        self.right_hand = pygame.image.load(images_path / "hand_right_centered.png").convert_alpha()
        self.left_hand = pygame.image.load(images_path / "hand_left_centered.png").convert_alpha()

        self.clock_face = pygame.transform.scale(self.clock_face, (420, 420))
        self.mickey = pygame.transform.scale(self.mickey, (170, 250))
        self.right_hand = pygame.transform.scale(self.right_hand, (120, 120))
        self.left_hand = pygame.transform.scale(self.left_hand, (120, 120))

        self.font = pygame.font.SysFont("Arial", 42)

    def draw_hand(self, image, value):
        angle_deg = value * 6
        rotated_image = pygame.transform.rotate(image, -angle_deg)

        distance = 58
        angle_rad = math.radians(angle_deg)

        x = self.clock_center[0] + math.sin(angle_rad) * distance # Shifting by x
        y = self.clock_center[1] - math.cos(angle_rad) * distance # Shifting by y

        rect = rotated_image.get_rect(center=(x, y))
        self.screen.blit(rotated_image, rect)

    def draw(self):
        self.screen.fill(self.bg_color)

        now = datetime.now() # Get current time
        minutes = now.minute
        seconds = now.second

        time_text = self.font.render(f"{minutes:02}:{seconds:02}", True, (0, 0, 0))
        time_rect = time_text.get_rect(center=(self.width // 2, 70))
        self.screen.blit(time_text, time_rect)

        # Clock face
        clock_rect = self.clock_face.get_rect(center=self.clock_center)
        self.screen.blit(self.clock_face, clock_rect)

        # Mickey in the center
        mickey_rect = self.mickey.get_rect(center=(self.clock_center[0], self.clock_center[1] -10))
        self.screen.blit(self.mickey, mickey_rect)

        # Hands on top of Mickey
        self.draw_hand(self.right_hand, minutes)   # right hand = minutes
        self.draw_hand(self.left_hand, seconds)    # left hand = seconds

        pygame.display.flip()