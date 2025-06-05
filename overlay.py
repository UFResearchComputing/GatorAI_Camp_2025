import pygame
from settings import *
import os
import game_settings


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

        # load the inventory icon
        inventory_icon = pygame.image.load(
            os.path.join(overlay_path, "backpack.png")
        ).convert_alpha()
        self.inventory_surf = pygame.transform.scale(inventory_icon, (64, 64))

        keyboard_extras = pygame.image.load(
            os.path.join(overlay_path, "Keyboard Extras.png")
        ).convert_alpha()

        keyboard_letters = pygame.image.load(
            os.path.join(overlay_path, "Keyboard Letters and Symbols.png")
        ).convert_alpha()

        spacebar_original = keyboard_extras.subsurface(
            pygame.Rect(64, 32, 32, 16)  # (x, y, width, height) in pixels
        )  # scale the spacebar to be twice as large
        self.spacebar_surf = pygame.transform.scale(spacebar_original, (64, 32))

        ctrl_key_original = keyboard_extras.subsurface(
            pygame.Rect(0, 32, 32, 16)  # (x, y, width, height) in pixels
        )
        self.ctrl_key_surf = pygame.transform.scale(ctrl_key_original, (64, 32))

        # load the letter "Q" for tool switching
        q_key_original = keyboard_letters.subsurface(
            pygame.Rect(0, 64, 16, 16)  # (x, y, width, height) in pixels
        )
        self.q_key_surf = pygame.transform.scale(q_key_original, (32, 32))

        # load the letter "E" for seed switching
        e_key_original = keyboard_letters.subsurface(
            pygame.Rect(64, 32, 16, 16)  # (x, y, width, height) in pixels
        )
        self.e_key_surf = pygame.transform.scale(e_key_original, (32, 32))

        # load the letter "I" for inventory
        i_key_original = keyboard_letters.subsurface(
            pygame.Rect(0, 48, 16, 16)  # (x, y, width, height) in pixels
        )
        self.i_key_surf = pygame.transform.scale(i_key_original, (32, 32))

        # register this overlay globally for audio updates
        game_settings.set_current_overlay(self)

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

        # q key to the right of the rotate icon above the space bar
        q_key_rect = self.q_key_surf.get_rect(
            midleft=(rotate_rect_spacebar.right + 5, rotate_rect_spacebar.centery)
        )
        self.display_surface.blit(self.q_key_surf, q_key_rect)

        # e key to the right of the rotate icon above the ctrl key
        e_key_rect = self.e_key_surf.get_rect(
            midleft=(rotate_rect.centerx + 10, rotate_rect.centery)
        )
        self.display_surface.blit(self.e_key_surf, e_key_rect)

        # seeds
        seed_surf = self.seeds_surf[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom=OVERLAY_POSITIONS["seed"])
        self.display_surface.blit(seed_surf, seed_rect)

        # inventory icon on the bottom right corner
        inventory_rect = self.inventory_surf.get_rect(
            bottomright=(SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        )

        # i key to the left of the inventory icon
        i_key_rect = self.i_key_surf.get_rect(
            midright=(inventory_rect.left - 10, inventory_rect.centery)
        )
        self.display_surface.blit(self.i_key_surf, i_key_rect)

        self.display_surface.blit(self.inventory_surf, inventory_rect)
