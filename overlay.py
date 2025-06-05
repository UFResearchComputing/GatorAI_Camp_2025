"""
PyDew Valley - UI Overlay System
================================
This module manages the game's user interface (UI) overlay that appears on top
of the game world. It shows the player's currently selected tools, seeds,
keyboard controls, and inventory access.

Educational Concepts Covered:
- User Interface (UI) design and implementation
- Image loading and manipulation
- Surface positioning and blitting
- File path management
- Dictionary comprehensions
- Coordinate system for UI positioning
- Visual feedback for user interactions

This file demonstrates how games create informative and intuitive user interfaces
that help players understand what they can do and what they have available.
"""

import pygame
from settings import *
import os
import game_settings


class Overlay:
    """
    UI Overlay Class - Game Interface Manager
    ========================================
    This class manages all the visual elements that appear on top of the game world,
    including tool indicators, seed indicators, keyboard hints, and inventory access.

    EDUCATIONAL CONCEPTS:
    - User Interface design principles
    - Image resource management
    - Coordinate positioning systems
    - Visual communication in games
    - File organization and loading
    - Surface manipulation and scaling

    The overlay helps players understand:
    - What tool they currently have selected
    - What seed they currently have selected
    - What keyboard controls are available
    - How to access their inventory
    """

    def __init__(self, player):
        """
        Initialize the UI Overlay System
        ===============================
        Loads all the necessary graphics for the UI and sets up positioning.

        EDUCATIONAL CONCEPTS:
        - Constructor initialization with dependencies
        - File path construction and management
        - Dictionary comprehensions for bulk operations
        - Image loading and format optimization
        - Surface scaling and transformation
        - Resource management and organization

        Parameters:
        player: The player object to get tool/seed information from
        """
        # BASIC SETUP
        # Get the main game display surface
        self.display_surface = pygame.display.get_surface()
        self.player = player  # Reference to player for current tool/seed info

        # GRAPHICS LOADING
        # Construct the path to overlay graphics folder
        base_path = os.path.dirname(os.path.abspath(__file__))
        overlay_path = os.path.join(base_path, "graphics/overlay/")

        # Load tool icons using dictionary comprehension
        # This creates a dictionary mapping tool names to their images
        self.tools_surf = {
            tool: pygame.image.load(
                os.path.join(overlay_path, f"{tool}.png")
            ).convert_alpha()  # convert_alpha() optimizes the image format
            for tool in player.tools
        }

        # Load seed icons the same way
        self.seeds_surf = {
            seed: pygame.image.load(
                os.path.join(overlay_path, f"{seed}.png")
            ).convert_alpha()
            for seed in player.seeds
        }

        # SPECIAL UI GRAPHICS
        # Load and scale the rotation indicator graphic
        rotate_graphic = pygame.image.load(
            os.path.join(overlay_path, "rotate-32.png")
        ).convert_alpha()
        self.rotate_surf = pygame.transform.scale(rotate_graphic, (20, 20))

        # Load and scale the inventory icon
        inventory_icon = pygame.image.load(
            os.path.join(overlay_path, "backpack.png")
        ).convert_alpha()
        self.inventory_surf = pygame.transform.scale(inventory_icon, (64, 64))

        # KEYBOARD KEY GRAPHICS
        # Load keyboard sprite sheets for showing key controls
        keyboard_extras = pygame.image.load(
            os.path.join(overlay_path, "Keyboard Extras.png")
        ).convert_alpha()

        keyboard_letters = pygame.image.load(
            os.path.join(overlay_path, "Keyboard Letters and Symbols.png")
        ).convert_alpha()

        # Extract and scale specific keys from the sprite sheets
        # Spacebar key (for tool usage)
        spacebar_original = keyboard_extras.subsurface(
            pygame.Rect(64, 32, 32, 16)  # (x, y, width, height) in pixels
        )
        self.spacebar_surf = pygame.transform.scale(spacebar_original, (64, 32))

        # Ctrl key (for seed planting)
        ctrl_key_original = keyboard_extras.subsurface(
            pygame.Rect(0, 32, 32, 16)  # (x, y, width, height) in pixels
        )
        self.ctrl_key_surf = pygame.transform.scale(ctrl_key_original, (64, 32))

        # Q key (for tool switching)
        q_key_original = keyboard_letters.subsurface(
            pygame.Rect(0, 64, 16, 16)  # (x, y, width, height) in pixels
        )
        self.q_key_surf = pygame.transform.scale(q_key_original, (32, 32))

        # E key (for seed switching)
        e_key_original = keyboard_letters.subsurface(
            pygame.Rect(64, 32, 16, 16)  # (x, y, width, height) in pixels
        )
        self.e_key_surf = pygame.transform.scale(e_key_original, (32, 32))

        # I key (for inventory)
        i_key_original = keyboard_letters.subsurface(
            pygame.Rect(0, 48, 16, 16)  # (x, y, width, height) in pixels
        )
        self.i_key_surf = pygame.transform.scale(i_key_original, (32, 32))

        # Register this overlay globally for audio updates
        game_settings.set_current_overlay(self)

    def display(self):
        """
        Draw the UI Overlay
        ==================
        This method draws all the UI elements on top of the game world.
        Called every frame to show current tool, seed, and control hints.

        EDUCATIONAL CONCEPTS:
        - UI rendering and positioning
        - Surface blitting (drawing one image onto another)
        - Rectangle positioning and alignment
        - Visual layout and organization
        - Real-time UI updates
        - Coordinate calculation for positioning

        This method demonstrates how to create a clean, informative UI that
        helps players understand the game controls and their current state.
        """
        # CURRENT TOOL DISPLAY
        # Show the currently selected tool icon
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom=OVERLAY_POSITIONS["tool"])
        self.display_surface.blit(tool_surf, tool_rect)

        # SPACEBAR KEY DISPLAY (for using tools)
        # Position spacebar key next to the tool (shows how to use the tool)
        spacebar_rect = self.spacebar_surf.get_rect(
            midleft=(tool_rect.right // 3, tool_rect.centery - 50)
        )
        self.display_surface.blit(self.spacebar_surf, spacebar_rect)

        # CURRENT SEED DISPLAY
        # Show the currently selected seed icon
        seed_surf = self.seeds_surf[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom=OVERLAY_POSITIONS["seed"])
        self.display_surface.blit(seed_surf, seed_rect)

        # CTRL KEY DISPLAY (for planting seeds)
        # Position ctrl key next to the seed (shows how to plant)
        ctrl_key_rect = self.ctrl_key_surf.get_rect(
            midleft=(
                OVERLAY_POSITIONS["seed"][0] + 20,
                OVERLAY_POSITIONS["seed"][1] - 20,
            )
        )
        self.display_surface.blit(self.ctrl_key_surf, ctrl_key_rect)

        # ROTATION INDICATORS
        # Show rotate symbols above ctrl and spacebar to indicate switching
        rotate_rect = self.rotate_surf.get_rect(
            midbottom=(ctrl_key_rect.centerx - 12, ctrl_key_rect.top - 5)
        )
        self.display_surface.blit(self.rotate_surf, rotate_rect)

        rotate_rect_spacebar = self.rotate_surf.get_rect(
            midbottom=(spacebar_rect.centerx - 12, spacebar_rect.top - 5)
        )
        self.display_surface.blit(self.rotate_surf, rotate_rect_spacebar)

        # Q KEY DISPLAY (for tool switching)
        # Position Q key next to rotation symbol to show tool switching control
        q_key_rect = self.q_key_surf.get_rect(
            midleft=(rotate_rect_spacebar.right + 5, rotate_rect_spacebar.centery)
        )
        self.display_surface.blit(self.q_key_surf, q_key_rect)

        # E KEY DISPLAY (for seed switching)
        # Position E key next to rotation symbol to show seed switching control
        e_key_rect = self.e_key_surf.get_rect(
            midleft=(rotate_rect.centerx + 10, rotate_rect.centery)
        )
        self.display_surface.blit(self.e_key_surf, e_key_rect)

        # INVENTORY ACCESS DISPLAY
        # Show inventory icon and I key in bottom right corner
        inventory_rect = self.inventory_surf.get_rect(
            bottomright=(SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        )

        # I KEY DISPLAY (for inventory access)
        # Position I key next to inventory icon
        i_key_rect = self.i_key_surf.get_rect(
            midright=(inventory_rect.left - 10, inventory_rect.centery)
        )
        self.display_surface.blit(self.i_key_surf, i_key_rect)

        # Draw the inventory icon
        self.display_surface.blit(self.inventory_surf, inventory_rect)
