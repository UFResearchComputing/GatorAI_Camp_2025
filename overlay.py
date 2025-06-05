import pygame
from settings import *
import os


class Overlay:
    def __init__(self, player):

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # imports
        base_path = os.path.dirname(os.path.abspath(__file__))
        overlay_path = os.path.join(base_path, "graphics/overlay/")
        self.tools_surf = {
            tool: pygame.image.load(
                os.path.join(overlay_path, f"{tool}.png")
            ).convert_alpha()
            for tool in player.tools
        }
        self.seeds_surf = {
            seed: pygame.image.load(
                os.path.join(overlay_path, f"{seed}.png")
            ).convert_alpha()
            for seed in player.seeds
        }

        # load keyboard graphics
        keyboard_extras = pygame.image.load(
            os.path.join(overlay_path, "Keyboard Extras.png")
        ).convert_alpha()
        # extract space bar from coordinates (40, 80) to (60, 120)
        self.spacebar_surf = keyboard_extras.subsurface(
            pygame.Rect(64, 32, 32, 16)  # (x, y, width, height) in pixels
        )

    def display(self):

        # tool
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom=OVERLAY_POSITIONS["tool"])
        self.display_surface.blit(tool_surf, tool_rect)

        # space bar key next to tool (positioned to the right of the tool icon)
        spacebar_rect = self.spacebar_surf.get_rect(
            midleft=(tool_rect.right // 2, tool_rect.centery - 50)
        )
        self.display_surface.blit(self.spacebar_surf, spacebar_rect)

        # seeds
        seed_surf = self.seeds_surf[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom=OVERLAY_POSITIONS["seed"])
        self.display_surface.blit(seed_surf, seed_rect)
