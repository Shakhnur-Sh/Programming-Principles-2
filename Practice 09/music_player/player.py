import pygame
import os


class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        self.playlist = [
            "music/track1.mp3",
            "music/track2.mp3"
        ]

        self.current_index = 0
        self.is_playing = False

    def load_current_track(self):
        track_path = self.playlist[self.current_index]
        pygame.mixer.music.load(track_path)
        return os.path.basename(track_path)

    def play(self):
        pygame.mixer.music.load(self.playlist[self.current_index])
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_current_track_name(self):
        return os.path.basename(self.playlist[self.current_index])

    def get_position_seconds(self):
        pos_ms = pygame.mixer.music.get_pos()
        if pos_ms < 0:
            return 0
        return pos_ms // 1000