from installer import install

install("pygame")
install("pytmx")

import pygame, sys
import os
from settings import *
from level import Level
from main_menu import MainMenu
from character_screen import CharacterScreen
import game_settings


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # Initialize mixer for audio
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PyDew Valley: GAIC 25")
        self.clock = pygame.time.Clock()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # Initialize settings first
        game_settings.load_settings()

        self.level = None
        self.main_menu = MainMenu(self.start_game)
        self.character_screen = None
        self.show_main_menu = True

    def start_game(self):
        self.level = Level()
        self.character_screen = CharacterScreen(self.level.player)
        self.show_main_menu = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (
                    event.type == pygame.KEYDOWN
                    and event.key == pygame.K_i
                    and self.character_screen
                ):
                    self.character_screen.toggle()

            dt = self.clock.tick() / 1000
            if self.show_main_menu:
                self.main_menu.update()
            else:
                self.level.run(dt)
                if self.character_screen and self.character_screen.visible:
                    self.character_screen.update()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
