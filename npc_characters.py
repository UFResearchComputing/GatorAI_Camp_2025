import pygame
from sprites import Generic
from settings import LAYERS
from support import import_folder
import os

class NPCCharacter(Generic):
    """
    Base class for visual NPC characters
    Handles animation and basic display
    """
    
    def __init__(self, pos, character_name, groups):
        # Load the character sprite
        self.character_name = character_name
        self.animations = self.load_animations()
        self.frame_index = 0
        self.animation_speed = 4
        
        # Set initial image
        self.current_animation = "idle"
        initial_image = self.animations[self.current_animation][0]
        
        # Initialize with Generic class
        super().__init__(pos, initial_image, groups, LAYERS['main'])
        
        # Smaller hitbox for NPCs (they don't move)
        self.hitbox = self.rect.copy().inflate(-20, -10)
    
    def load_animations(self):
        """Load animation frames for this NPC"""
        animations = {
            "idle": [],
        }
        
        base_path = os.path.dirname(os.path.abspath(__file__))
        character_path = f"graphics/npcs/{self.character_name}"
        
        # Try to load animations, use placeholder if not found
        try:
            animations["idle"] = import_folder(f"{character_path}/idle")
        except:
            # Create placeholder image if no sprites found
            placeholder = pygame.Surface((32, 48))
            placeholder.fill((100, 100, 200))  # Blue placeholder
            animations["idle"] = [placeholder]
        
        return animations
    
    def animate(self, dt):
        """Update animation frame"""
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.animations[self.current_animation]):
            self.frame_index = 0
        
        self.image = self.animations[self.current_animation][int(self.frame_index)]
    
    def update(self, dt):
        """Update the NPC"""
        self.animate(dt)

class Blacksmith(NPCCharacter):
    """Specific blacksmith NPC"""
    
    def __init__(self, pos, groups):
        super().__init__(pos, "blacksmith", groups)
        
        # Blacksmith-specific properties
        self.name = "Magnus the Blacksmith"
        self.role = "tool craftsman"
