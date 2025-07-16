import pygame
from sprites import Generic
from settings import LAYERS
from support import import_folder


class NPCCharacter(Generic):
    """
    Base class for visual NPC characters
    Handles loading and displaying NPC graphics from files
    """

    def __init__(
        self, pos, character_name, groups, graphics_path=None, target_size=None
    ):
        self.character_name = character_name

        # Load graphics or use placeholder
        if graphics_path:
            try:
                # Try to load the graphics from the specified path
                idle_frames = import_folder(graphics_path)
                if idle_frames:
                    # Use the first frame as the static image
                    npc_image = idle_frames[0]

                    # Resize if target_size is specified
                    if target_size:
                        npc_image = pygame.transform.scale(npc_image, target_size)
                        print(f"🎭 Resized {character_name} graphics to {target_size}")

                    print(
                        f"🎭 Loaded graphics for {character_name} from {graphics_path}"
                    )
                else:
                    npc_image = self._create_placeholder()
                    print(f"⚠️ No graphics found at {graphics_path}, using placeholder")
            except Exception as e:
                print(f"⚠️ Failed to load graphics for {character_name}: {e}")
                npc_image = self._create_placeholder()
        else:
            npc_image = self._create_placeholder()

        # Initialize with Generic class
        super().__init__(pos, npc_image, groups, LAYERS["main"])

        # Smaller hitbox for NPCs
        self.hitbox = self.rect.copy().inflate(-20, -10)

        print(f"🎭 NPC {character_name} created at {pos}")

    def _create_placeholder(self):
        """Create a simple placeholder image for NPCs without graphics"""
        placeholder = pygame.Surface((64, 64))
        placeholder.fill((100, 100, 255))  # Blue background color

        # Draw a simple face to make it look more like a character
        pygame.draw.circle(placeholder, (255, 255, 255), (32, 20), 8)  # Head
        pygame.draw.circle(placeholder, (0, 0, 0), (28, 18), 2)  # Left eye
        pygame.draw.circle(placeholder, (0, 0, 0), (36, 18), 2)  # Right eye
        pygame.draw.arc(placeholder, (0, 0, 0), (25, 22, 14, 8), 0, 3.14)  # Smile

        return placeholder

    def update(self, dt):
        """Update the NPC - basic NPCs don't need complex updates"""
        pass


class Blacksmith(NPCCharacter):
    """Specific blacksmith NPC that uses real graphics"""

    def __init__(self, pos, groups):
        # Initialize with the path to blacksmith graphics and resize to match player
        # Player size is approximately 172x124, so we'll use a similar size
        super().__init__(
            pos,
            "blacksmith",
            groups,
            "graphics/npcs/blacksmith/idle",
            target_size=(80, 120),
        )

        # Blacksmith-specific properties
        self.name = "Magnus the Blacksmith"
        self.role = "tool craftsman"

        print(f"🔨 Blacksmith Magnus created at {pos} using real graphics (resized)")
