"""
PyDew Valley - Dialogue System
=============================
This module manages character dialogue in the game, providing a flexible
framework for conversations with NPCs (Non-Player Characters).

Educational Concepts Covered:
- Data structures (dictionaries, lists)
- Text rendering and display
- User interface design
- State management
- Event handling and input processing
- Modular code organization

This system can be easily extended to support:
- Multiple characters with unique dialogue
- Branching conversations
- Character mood/emotion responses
- Quest-related dialogue
- Dynamic dialogue based on game state
"""

import pygame
from settings import *
from timer import Timer


class DialogueSystem:
    """
    Dialogue System Class - Manages NPC Conversations
    ===============================================
    This class handles displaying and managing conversations with NPCs.
    It provides a flexible framework that can be extended for different
    characters and dialogue types.

    EDUCATIONAL CONCEPTS:
    - Text rendering and word wrapping
    - State management for conversations
    - Input handling for dialogue progression
    - UI layout and positioning
    - Data structure organization for dialogue content
    """

    def __init__(self):
        """Initialize the dialogue system"""
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font("font/LycheeSoda.ttf", 24)
        self.title_font = pygame.font.Font("font/LycheeSoda.ttf", 32)

        # Dialogue state
        self.active = False
        self.current_character = None
        self.current_dialogue = []
        self.current_line = 0
        self.on_complete_callback = None

        # UI settings
        self.dialogue_box_height = 120  # Reduced height
        self.padding = 20
        self.line_spacing = 25  # Reduced spacing

        # Calculate safe positioning to avoid UI overlap
        # Tool/seed UI is at bottom-left, emotions at bottom-right
        self.ui_safe_bottom_margin = 150  # Leave space for tool/seed UI

        # Input handling
        self.input_timer = Timer(300)  # Prevent rapid input

        # Character dialogue data
        self.character_dialogues = {
            "trader": {
                "name": "Merchant Pete",
                "greeting": [
                    "Well hello there, young farmer!",
                    "Welcome to my humble trading post!",
                    "I've got the finest seeds and will buy your crops at fair prices.",
                    "What can I do for you today?",
                ],
                "return_visit": [
                    "Ah, back again I see!",
                    "How's the farming going?",
                    "Ready to do some business?",
                ],
                "rich_player": [
                    "My, my! Look at all that coin you have!",
                    "Business must be booming on your farm!",
                    "What fine goods can I interest you in today?",
                ],
            }
        }

    def start_dialogue(self, character_id, player_money=0, callback=None):
        """
        Start a dialogue with a specific character

        Parameters:
        character_id: The ID of the character to talk to
        player_money: Player's current money (for dynamic dialogue)
        callback: Function to call when dialogue is complete
        """
        if character_id not in self.character_dialogues:
            return False

        self.active = True
        self.current_character = character_id
        self.current_line = 0
        self.on_complete_callback = callback

        # Activate input timer to prevent immediate input processing
        self.input_timer.activate()

        # Choose appropriate dialogue based on conditions
        character_data = self.character_dialogues[character_id]

        if player_money > 1000:  # Rich player
            self.current_dialogue = character_data.get(
                "rich_player", character_data["greeting"]
            )
        else:
            # For now, always use greeting. Could add logic for return visits
            self.current_dialogue = character_data["greeting"]

        return True

    def handle_input(self):
        """Handle user input for dialogue progression"""
        if not self.active:
            return

        keys = pygame.key.get_pressed()
        self.input_timer.update()

        if self.input_timer.active:
            return

        # Advance dialogue on SPACE or ENTER
        if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
            self.current_line += 1
            self.input_timer.activate()

            # Check if dialogue is complete
            if self.current_line >= len(self.current_dialogue):
                self.end_dialogue()

        # Skip dialogue with ESC
        elif keys[pygame.K_ESCAPE]:
            self.end_dialogue()

    def end_dialogue(self):
        """End the current dialogue and call completion callback"""
        self.active = False
        self.current_character = None
        self.current_dialogue = []
        self.current_line = 0

        if self.on_complete_callback:
            self.on_complete_callback()
            self.on_complete_callback = None

    def render_text_wrapped(self, text, max_width):
        """
        Render text with word wrapping

        Parameters:
        text: The text to render
        max_width: Maximum width in pixels before wrapping

        Returns:
        List of rendered text surfaces
        """
        words = text.split(" ")
        lines = []
        current_line = []

        for word in words:
            # Test if adding this word would exceed the width
            test_line = " ".join(current_line + [word])
            test_surface = self.font.render(test_line, True, "White")

            if test_surface.get_width() <= max_width:
                current_line.append(word)
            else:
                if current_line:  # If we have words in the current line
                    lines.append(" ".join(current_line))
                    current_line = [word]
                else:  # Single word is too long, force it
                    lines.append(word)
                    current_line = []

        # Add the last line if it has content
        if current_line:
            lines.append(" ".join(current_line))

        # Render all lines
        rendered_lines = []
        for line in lines:
            surface = self.font.render(line, True, "White")
            rendered_lines.append(surface)

        return rendered_lines

    def display(self):
        """Display the current dialogue on screen"""
        if not self.active or not self.current_dialogue:
            return

        # Get character info
        character_data = self.character_dialogues[self.current_character]
        character_name = character_data["name"]

        # Calculate dialogue box position - position above the tool/seed UI
        box_y = SCREEN_HEIGHT - self.dialogue_box_height - self.ui_safe_bottom_margin
        box_rect = pygame.Rect(0, box_y, SCREEN_WIDTH, self.dialogue_box_height)

        # Draw dialogue box background
        pygame.draw.rect(self.display_surface, (40, 40, 40), box_rect)
        pygame.draw.rect(self.display_surface, "White", box_rect, 3)

        # Draw character name
        name_surface = self.title_font.render(character_name, True, "Yellow")
        name_rect = name_surface.get_rect(topleft=(self.padding, box_y + 10))
        self.display_surface.blit(name_surface, name_rect)

        # Draw current dialogue line
        if self.current_line < len(self.current_dialogue):
            current_text = self.current_dialogue[self.current_line]

            # Render with word wrapping
            max_text_width = SCREEN_WIDTH - (self.padding * 2)
            wrapped_lines = self.render_text_wrapped(current_text, max_text_width)

            # Display wrapped lines
            y_offset = box_y + 50  # Start below the character name
            for line_surface in wrapped_lines:
                line_rect = line_surface.get_rect(topleft=(self.padding, y_offset))
                self.display_surface.blit(line_surface, line_rect)
                y_offset += self.line_spacing

        # Draw progress indicator
        progress_text = f"({self.current_line + 1}/{len(self.current_dialogue)})"
        progress_surface = self.font.render(progress_text, True, "Gray")
        progress_rect = progress_surface.get_rect(
            bottomright=(
                SCREEN_WIDTH - self.padding,
                box_y + self.dialogue_box_height - 5,
            )
        )
        self.display_surface.blit(progress_surface, progress_rect)

        # Draw instructions
        if self.current_line < len(self.current_dialogue) - 1:
            instruction = "Press SPACE to continue, ESC to skip"
        else:
            instruction = "Press SPACE to continue, ESC to skip"

        instruction_surface = self.font.render(instruction, True, "Yellow")
        instruction_rect = instruction_surface.get_rect(
            bottomleft=(self.padding, box_y + self.dialogue_box_height - 5)
        )
        self.display_surface.blit(instruction_surface, instruction_rect)

    def add_character_dialogue(self, character_id, dialogue_data):
        """
        Add dialogue for a new character

        Parameters:
        character_id: Unique identifier for the character
        dialogue_data: Dictionary containing character dialogue information

        Example:
        dialogue_data = {
            "name": "Character Name",
            "greeting": ["Hello!", "Nice to meet you!"],
            "quest_dialogue": ["I need your help!", "Can you find my lost item?"]
        }
        """
        self.character_dialogues[character_id] = dialogue_data

    def update(self):
        """Update the dialogue system"""
        if self.active:
            self.handle_input()
            self.display()
