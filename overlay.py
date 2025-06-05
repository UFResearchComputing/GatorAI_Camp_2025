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
        rotate_graphic = pygame.image.load(
            os.path.join(overlay_path, "rotate-32.png")
        ).convert_alpha()
        self.rotate_surf = pygame.transform.scale(rotate_graphic, (20, 20))

        keyboard_extras = pygame.image.load(
            os.path.join(overlay_path, "Keyboard Extras.png")
        ).convert_alpha()
        spacebar_original = keyboard_extras.subsurface(
            pygame.Rect(64, 32, 32, 16)  # (x, y, width, height) in pixels
        )
        # scale the spacebar to be twice as large
        self.spacebar_surf = pygame.transform.scale(spacebar_original, (64, 32))

        ctrl_key_original = keyboard_extras.subsurface(
            pygame.Rect(0, 32, 32, 16)  # (x, y, width, height) in pixels
        )
        self.ctrl_key_surf = pygame.transform.scale(ctrl_key_original, (64, 32))

    def display(self):

        # tool
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom=OVERLAY_POSITIONS["tool"])
        self.display_surface.blit(tool_surf, tool_rect)

        # space bar key next to tool (positioned to the right of the tool icon)
        spacebar_rect = self.spacebar_surf.get_rect(
            midleft=(tool_rect.right // 3, tool_rect.centery - 50)
        )
        self.display_surface.blit(self.spacebar_surf, spacebar_rect)

        # ctrl key to the right of the seed icon
        ctrl_key_rect = self.ctrl_key_surf.get_rect(
            midleft=(
                OVERLAY_POSITIONS["seed"][0] + 20,
                OVERLAY_POSITIONS["seed"][1] - 20,
            )
        )
        self.display_surface.blit(
            self.ctrl_key_surf, ctrl_key_rect
        )  # place a rotate icon above the ctrl key and another above the space bar
        rotate_rect = self.rotate_surf.get_rect(
            midbottom=(ctrl_key_rect.centerx - 12, ctrl_key_rect.top - 5)
        )
        self.display_surface.blit(self.rotate_surf, rotate_rect)
        rotate_rect_spacebar = self.rotate_surf.get_rect(
            midbottom=(spacebar_rect.centerx - 12, spacebar_rect.top - 5)
        )
        self.display_surface.blit(self.rotate_surf, rotate_rect_spacebar)

        # seeds
        seed_surf = self.seeds_surf[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom=OVERLAY_POSITIONS["seed"])
        self.display_surface.blit(seed_surf, seed_rect)
