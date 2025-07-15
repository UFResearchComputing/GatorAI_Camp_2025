# 🧙‍♂️ Adding New Characters/NPCs to PyDew Valley

## 📋 Table of Contents
1. [Understanding the NPC System](#understanding-the-npc-system)
2. [Adding a Simple Interactable NPC](#adding-a-simple-interactable-npc)
3. [Creating Visual NPC Characters](#creating-visual-npc-characters)
4. [Adding Custom Dialogues and Interactions](#adding-custom-dialogues-and-interactions)
5. [Advanced NPC Features](#advanced-npc-features)
6. [Complete Example: Adding a Blacksmith](#complete-example-adding-a-blacksmith)

---

## 🔍 Understanding the NPC System

The current game has a trader NPC that works through:

### Current NPC Architecture
```
📍 Map Position (TMX file) → 🔲 Interaction Area → 💬 Dialogue System → 🛒 Custom Menu
```

### How the Trader Works
1. **Map Definition**: The trader position is defined in `data/map.tmx`
2. **Interaction Area**: An invisible `Interaction` sprite is created at that position
3. **Player Detection**: When player presses Enter near the area, it triggers
4. **Dialogue**: AI-generated dialogue plays first
5. **Menu**: After dialogue, the trading menu opens

### Key Files Involved
- **`level.py`**: Creates interaction areas and handles NPC logic
- **`sprites.py`**: Contains the `Interaction` class for NPC areas
- **`dialogue_system.py`**: Handles NPC conversations
- **`trader_menu.py`**: Custom interface for the trader
- **`data/map.tmx`**: Map file defining NPC positions

---

## 🎯 Adding a Simple Interactable NPC

Let's start by adding a simple NPC that shows a message when interacted with.

### Step 1: Add NPC to Map File

First, you need to add your NPC position to the map. For now, we'll add it directly in the code:

```python
# In level.py, find the setup() method around line 225
# Add this after the existing Trader interaction:

if obj.name == "Blacksmith":
    # Create blacksmith interaction area
    Interaction(
        (obj.x, obj.y),
        (obj.width, obj.height),
        self.interaction_sprites,
        obj.name,
    )
```

### Step 2: Handle NPC Interaction

In `player.py`, find the interaction handling code (around line 439):

```python
# Find this section in player.py:
if collided_interaction_sprite:
    # Check what type of object it is
    if collided_interaction_sprite[0].name == "Trader":
        # Open the shop interface
        self.toggle_shop()
    elif collided_interaction_sprite[0].name == "Blacksmith":
        # Add blacksmith interaction
        self.interact_with_blacksmith()
    else:  # For beds or other objects, make the player sleep
        self.status = "left_idle"
        self.sleep = True
```

### Step 3: Create the Interaction Method

Add this method to the `Player` class in `player.py`:

```python
def interact_with_blacksmith(self):
    """Interact with the blacksmith NPC"""
    print("🔨 Blacksmith: 'Welcome to my forge! I can upgrade your tools.'")
    # For now, just print a message
    # Later we'll add proper dialogue and menus
```

### Step 4: Test Position Manually

Since we don't have easy map editing access, let's add a temporary NPC at a fixed position:

```python
# In level.py setup() method, after the Ground tile creation (around line 255):

# TEMPORARY BLACKSMITH NPC (for testing)
Interaction(
    (400, 300),  # Fixed position on the map
    (64, 64),    # Size of interaction area
    self.interaction_sprites,
    "Blacksmith"
)
```

**⚠️ IMPORTANT: Update Player Interaction Handling**

You also need to add the Blacksmith case to the player's interaction handling in `player.py`. Find the interaction code (around line 442) and update it:

```python
# In player.py, find this section and UPDATE it:
if collided_interaction_sprite:
    # Check what type of object it is
    if collided_interaction_sprite[0].name == "Trader":
        # Open the shop interface
        self.toggle_shop()
    elif collided_interaction_sprite[0].name == "Blacksmith":
        # Interact with the blacksmith
        self.interact_with_blacksmith()
    else:  # For beds or other objects, make the player sleep
        self.status = "left_idle"
        self.sleep = True
```

### 🎮 Testing Your NPC

**What you should see:**
1. **In Game**: Nothing visual yet - just an invisible interaction area
2. **Walk** to approximately the center-left area of the map (coordinates 400, 300)
3. **Press Enter** when you're near that area
4. **In Console/Terminal**: You should see the message: `🔨 Blacksmith: 'Welcome to my forge! I can upgrade your tools.'`

**If it's not working:**
- Make sure you're close enough to the interaction area (try walking around near x=400, y=300)
- Check that both the level.py AND player.py changes are saved
- Look for any error messages in the console

---

## 🎨 Creating Visual NPC Characters

Now let's add a visible character sprite for our NPC.

### Step 1: Create NPC Sprite Class

Create a new file `npc_characters.py`:

```python
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
```

### Step 2: Create NPC Graphics

Create the directory structure:
```
graphics/
└── npcs/
    └── blacksmith/
        └── idle/
            ├── 0.png
            ├── 1.png
            ├── 2.png
            └── 3.png
```

For now, you can create simple placeholder sprites or reuse existing character graphics.

### Step 3: Add Visual NPC to Level

Modify `level.py` to create visual NPCs:

```python
# Add this import at the top of level.py
from npc_characters import Blacksmith

# In the setup() method, after creating the interaction area:
if obj.name == "Blacksmith":
    # Create interaction area
    Interaction(
        (obj.x, obj.y),
        (obj.width, obj.height),
        self.interaction_sprites,
        obj.name,
    )
    
    # Create visual NPC character
    self.blacksmith_npc = Blacksmith(
        (obj.x, obj.y - 20),  # Slightly above interaction area
        self.all_sprites
    )
```

For the temporary version:
```python
# TEMPORARY BLACKSMITH NPC (visual + interaction)
interaction_pos = (400, 300)
Interaction(
    interaction_pos,
    (64, 64),
    self.interaction_sprites,
    "Blacksmith"
)

# Add visual character
self.blacksmith_npc = Blacksmith(
    (interaction_pos[0], interaction_pos[1] - 20),
    self.all_sprites
)
```

---

## 💬 Adding Custom Dialogues and Interactions

Let's make our blacksmith have proper AI-powered dialogues.

### Step 1: Add Blacksmith to Dialogue System

In `dialogue_system.py`, find the `_get_static_fallback` method:

```python
def _get_static_fallback(self, character_id: str) -> str:
    """Provides a simple, static fallback dialogue for NPCs."""
    fallbacks = {
        "trader": "Welcome, friend! I have many fine goods for a hardworking farmer like you. Let's see what you need.",
        "blacksmith": "Greetings, farmer! I can forge better tools for your farm work. Bring me some metal and I'll craft you something special!"
    }
    return fallbacks.get(character_id, "Hello there! Nice day for farming.")
```

### Step 2: Create Blacksmith Interaction System

In `level.py`, add a blacksmith toggle method similar to `toggle_shop()`:

```python
def toggle_blacksmith(self):
    """Start Blacksmith Dialogue and Interaction"""
    # Get current emotion for context-aware dialogue
    recent_emotions = (
        list(self.emotions_deque) if self.emotions_deque else ["neutral"]
    )
    current_emotion = recent_emotions[0] if recent_emotions else "neutral"
    
    # Determine player context for blacksmith
    if len([tool for tool in self.player.tools if tool != "basic"]) > 0:
        situation = "player has some upgraded tools and is progressing well"
    elif self.player.item_inventory.get("wood", 0) > 10:
        situation = "player has materials for tool upgrades"
    else:
        situation = "player is new and needs better tools"
    
    player_context = {
        "npc_name": "Magnus the Blacksmith",
        "npc_role": "skilled tool craftsman",
        "situation": situation,
        "emotion": current_emotion,
        "player_money": self.player.money,
    }
    
    # Start dialogue with blacksmith
    self.dialogue_system.start_dialogue(
        "blacksmith", 
        player_context=player_context, 
        on_finish=self.open_blacksmith_menu
    )

def open_blacksmith_menu(self):
    """Open the Blacksmith Menu"""
    self.blacksmith_active = True
```

### Step 3: Update Player Interaction

In `player.py`, modify the interaction code:

```python
# Update the __init__ method to add blacksmith toggle
def __init__(self, pos, group, collision_sprites, tree_sprites, interaction, soil_layer, toggle_shop, toggle_blacksmith=None):
    # ... existing code ...
    self.toggle_blacksmith = toggle_blacksmith

# Update the interaction handling
if collided_interaction_sprite:
    if collided_interaction_sprite[0].name == "Trader":
        self.toggle_shop()
    elif collided_interaction_sprite[0].name == "Blacksmith":
        if self.toggle_blacksmith:
            self.toggle_blacksmith()
    else:
        self.status = "left_idle"
        self.sleep = True
```

### Step 4: Update Level Player Creation

In `level.py`, update the player creation:

```python
self.player = Player(
    pos=(obj.x, obj.y),
    group=self.all_sprites,
    collision_sprites=self.collision_sprites,
    tree_sprites=self.tree_sprites,
    interaction=self.interaction_sprites,
    soil_layer=self.soil_layer,
    toggle_shop=self.toggle_shop,
    toggle_blacksmith=self.toggle_blacksmith,  # Add this line
)
```

---

## 🔧 Advanced NPC Features

### Custom NPC Menu System

Create `blacksmith_menu.py`:

```python
import pygame
from settings import *
from timer import Timer

class BlacksmithMenu:
    def __init__(self, player):
        self.player = player
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font("font/LycheeSoda.ttf", 30)
        
        # Tool upgrade options
        self.upgrades = {
            "better_hoe": {"price": 100, "description": "Upgraded Hoe - Works faster!"},
            "better_axe": {"price": 150, "description": "Sharp Axe - Cuts trees quicker!"},
            "better_watering_can": {"price": 120, "description": "Large Watering Can - Waters more area!"}
        }
        
        self.options = list(self.upgrades.keys())
        self.index = 0
        self.timer = Timer(200)
        
        # Menu appearance
        self.width = 600
        self.height = 400
        self.main_rect = pygame.Rect(
            SCREEN_WIDTH // 2 - self.width // 2,
            SCREEN_HEIGHT // 2 - self.height // 2,
            self.width,
            self.height
        )
    
    def input(self):
        keys = pygame.key.get_pressed()
        self.timer.update()
        
        if not self.timer.active:
            if keys[pygame.K_UP]:
                self.index = (self.index - 1) % len(self.options)
                self.timer.activate()
            
            if keys[pygame.K_DOWN]:
                self.index = (self.index + 1) % len(self.options)
                self.timer.activate()
            
            if keys[pygame.K_SPACE]:
                self.purchase_upgrade()
                self.timer.activate()
    
    def purchase_upgrade(self):
        """Handle upgrade purchase"""
        upgrade_key = self.options[self.index]
        upgrade_info = self.upgrades[upgrade_key]
        
        if self.player.money >= upgrade_info["price"]:
            self.player.money -= upgrade_info["price"]
            # Add upgrade logic here
            print(f"🔨 Purchased {upgrade_info['description']}!")
        else:
            print("💰 Not enough money for this upgrade!")
    
    def display(self):
        """Draw the blacksmith menu"""
        # Background
        pygame.draw.rect(self.display_surface, (50, 50, 50), self.main_rect)
        pygame.draw.rect(self.display_surface, "white", self.main_rect, 5)
        
        # Title
        title_surf = self.font.render("🔨 Blacksmith Upgrades", True, "white")
        title_rect = title_surf.get_rect(centerx=self.main_rect.centerx, y=self.main_rect.y + 20)
        self.display_surface.blit(title_surf, title_rect)
        
        # Money display
        money_surf = self.font.render(f"Money: ${self.player.money}", True, "yellow")
        money_rect = money_surf.get_rect(centerx=self.main_rect.centerx, y=title_rect.bottom + 20)
        self.display_surface.blit(money_surf, money_rect)
        
        # Upgrade options
        start_y = money_rect.bottom + 40
        for i, upgrade_key in enumerate(self.options):
            upgrade_info = self.upgrades[upgrade_key]
            color = "yellow" if i == self.index else "white"
            
            # Upgrade name and price
            text = f"{upgrade_info['description']} - ${upgrade_info['price']}"
            text_surf = pygame.font.Font("font/LycheeSoda.ttf", 24).render(text, True, color)
            text_rect = text_surf.get_rect(centerx=self.main_rect.centerx, y=start_y + i * 60)
            self.display_surface.blit(text_surf, text_rect)
            
            # Selection indicator
            if i == self.index:
                pygame.draw.rect(self.display_surface, "yellow", text_rect.inflate(20, 10), 2)
        
        # Instructions
        inst_surf = pygame.font.Font("font/LycheeSoda.ttf", 20).render("SPACE: Buy | ESC: Exit", True, "white")
        inst_rect = inst_surf.get_rect(centerx=self.main_rect.centerx, y=self.main_rect.bottom - 30)
        self.display_surface.blit(inst_surf, inst_rect)
    
    def update(self):
        self.input()
        self.display()
```

### Multiple Character Types

Create a character factory system in `npc_characters.py`:

```python
class NPCFactory:
    """Factory for creating different types of NPCs"""
    
    @staticmethod
    def create_npc(npc_type, pos, groups):
        if npc_type == "blacksmith":
            return Blacksmith(pos, groups)
        elif npc_type == "librarian":
            return Librarian(pos, groups)
        elif npc_type == "fisherman":
            return Fisherman(pos, groups)
        else:
            return NPCCharacter(pos, npc_type, groups)

class Librarian(NPCCharacter):
    """Librarian NPC who gives farming tips"""
    
    def __init__(self, pos, groups):
        super().__init__(pos, "librarian", groups)
        self.name = "Sarah the Librarian"
        self.role = "farming knowledge keeper"

class Fisherman(NPCCharacter):
    """Fisherman NPC who trades fish"""
    
    def __init__(self, pos, groups):
        super().__init__(pos, "fisherman", groups)
        self.name = "Old Pete the Fisherman"
        self.role = "fish trader"
```

---

## 🛠️ Complete Example: Adding a Blacksmith

Here's the complete step-by-step process to add a functional blacksmith NPC:

### Step 1: Create the Files

**`npc_characters.py`** (new file):
```python
import pygame
from sprites import Generic
from settings import LAYERS
import os

class NPCCharacter(Generic):
    def __init__(self, pos, character_name, groups):
        # Create placeholder image
        placeholder = pygame.Surface((32, 48))
        placeholder.fill((100, 100, 200))
        
        super().__init__(pos, placeholder, groups, LAYERS['main'])
        
        self.character_name = character_name
        self.frame_index = 0
        self.hitbox = self.rect.copy().inflate(-20, -10)
    
    def update(self, dt):
        pass  # NPCs don't need complex updates yet

class Blacksmith(NPCCharacter):
    def __init__(self, pos, groups):
        super().__init__(pos, "blacksmith", groups)
        self.name = "Magnus the Blacksmith"
        self.role = "tool craftsman"
        
        # Different color for blacksmith
        self.image.fill((150, 75, 0))  # Brown color
```

**`blacksmith_menu.py`** (new file):
```python
import pygame
from settings import *
from timer import Timer

class BlacksmithMenu:
    def __init__(self, player):
        self.player = player
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font("font/LycheeSoda.ttf", 30)
        self.active = True
        
        # Simple upgrade system
        self.upgrades = [
            {"name": "Tool Repair", "price": 50, "description": "Repair all tools"},
            {"name": "Hoe Upgrade", "price": 100, "description": "Better farming tool"},
            {"name": "Axe Sharpening", "price": 80, "description": "Faster tree cutting"}
        ]
        
        self.index = 0
        self.timer = Timer(200)
    
    def input(self):
        keys = pygame.key.get_pressed()
        self.timer.update()
        
        if keys[pygame.K_ESCAPE]:
            self.active = False
            return
        
        if not self.timer.active:
            if keys[pygame.K_UP]:
                self.index = (self.index - 1) % len(self.upgrades)
                self.timer.activate()
            
            if keys[pygame.K_DOWN]:
                self.index = (self.index + 1) % len(self.upgrades)
                self.timer.activate()
            
            if keys[pygame.K_SPACE]:
                self.purchase_upgrade()
                self.timer.activate()
    
    def purchase_upgrade(self):
        upgrade = self.upgrades[self.index]
        if self.player.money >= upgrade["price"]:
            self.player.money -= upgrade["price"]
            print(f"🔨 {upgrade['description']} complete!")
        else:
            print("💰 Not enough money!")
    
    def display(self):
        # Simple menu display
        menu_rect = pygame.Rect(200, 150, 400, 300)
        pygame.draw.rect(self.display_surface, (50, 50, 50), menu_rect)
        pygame.draw.rect(self.display_surface, "white", menu_rect, 3)
        
        # Title
        title_surf = self.font.render("🔨 Blacksmith Services", True, "white")
        title_rect = title_surf.get_rect(centerx=menu_rect.centerx, y=menu_rect.y + 20)
        self.display_surface.blit(title_surf, title_rect)
        
        # Money
        money_surf = pygame.font.Font("font/LycheeSoda.ttf", 24).render(f"Money: ${self.player.money}", True, "yellow")
        money_rect = money_surf.get_rect(centerx=menu_rect.centerx, y=title_rect.bottom + 20)
        self.display_surface.blit(money_surf, money_rect)
        
        # Options
        for i, upgrade in enumerate(self.upgrades):
            y_pos = money_rect.bottom + 40 + i * 50
            color = "yellow" if i == self.index else "white"
            
            text = f"{upgrade['name']} - ${upgrade['price']}"
            text_surf = pygame.font.Font("font/LycheeSoda.ttf", 20).render(text, True, color)
            text_rect = text_surf.get_rect(centerx=menu_rect.centerx, y=y_pos)
            self.display_surface.blit(text_surf, text_rect)
            
            if i == self.index:
                pygame.draw.rect(self.display_surface, "yellow", text_rect.inflate(20, 5), 2)
        
        # Instructions
        inst_surf = pygame.font.Font("font/LycheeSoda.ttf", 16).render("SPACE: Select | ESC: Exit", True, "white")
        inst_rect = inst_surf.get_rect(centerx=menu_rect.centerx, y=menu_rect.bottom - 30)
        self.display_surface.blit(inst_surf, inst_rect)
    
    def update(self):
        self.input()
        if self.active:
            self.display()
        return self.active
```

### Step 2: Modify Existing Files

**In `level.py`**, add these imports at the top:
```python
from npc_characters import Blacksmith
from blacksmith_menu import BlacksmithMenu
```

**In `level.py`**, add to the `__init__` method:
```python
# Add after the trader menu setup
self.blacksmith_menu = BlacksmithMenu(self.player)
self.blacksmith_active = False
```

**In `level.py`**, add to the `setup()` method (after the ground tile):
```python
# TEMPORARY BLACKSMITH NPC (for testing)
blacksmith_pos = (300, 200)  # Choose a position on your map
Interaction(
    blacksmith_pos,
    (64, 64),
    self.interaction_sprites,
    "Blacksmith"
)

# Create visual blacksmith character
self.blacksmith_npc = Blacksmith(
    blacksmith_pos,
    self.all_sprites
)
```

**In `level.py`**, add these methods:
```python
def toggle_blacksmith(self):
    """Start Blacksmith Dialogue"""
    recent_emotions = list(self.emotions_deque) if self.emotions_deque else ["neutral"]
    current_emotion = recent_emotions[0] if recent_emotions else "neutral"
    
    player_context = {
        "npc_name": "Magnus the Blacksmith",
        "npc_role": "skilled tool craftsman",
        "situation": "player wants to upgrade their farming tools",
        "emotion": current_emotion,
        "player_money": self.player.money,
    }
    
    self.dialogue_system.start_dialogue(
        "blacksmith",
        player_context=player_context,
        on_finish=self.open_blacksmith_menu
    )

def open_blacksmith_menu(self):
    """Open the Blacksmith Menu"""
    self.blacksmith_active = True
    self.blacksmith_menu = BlacksmithMenu(self.player)  # Refresh menu
```

**In `level.py`**, update the `run()` method:
```python
def run(self, dt):
    # ... existing code ...
    
    # Handle blacksmith menu
    if self.blacksmith_active:
        self.blacksmith_active = self.blacksmith_menu.update()
    
    # ... rest of existing code ...
```

**In `level.py`**, update player creation:
```python
self.player = Player(
    pos=(obj.x, obj.y),
    group=self.all_sprites,
    collision_sprites=self.collision_sprites,
    tree_sprites=self.tree_sprites,
    interaction=self.interaction_sprites,
    soil_layer=self.soil_layer,
    toggle_shop=self.toggle_shop,
    toggle_blacksmith=self.toggle_blacksmith,  # Add this line
)
```

**In `player.py`**, update the `__init__` method signature:
```python
def __init__(self, pos, group, collision_sprites, tree_sprites, interaction, soil_layer, toggle_shop, toggle_blacksmith=None):
    # ... existing code ...
    self.toggle_blacksmith = toggle_blacksmith
```

**In `player.py`**, update the interaction handling:
```python
if collided_interaction_sprite:
    if collided_interaction_sprite[0].name == "Trader":
        self.toggle_shop()
    elif collided_interaction_sprite[0].name == "Blacksmith":
        if self.toggle_blacksmith:
            self.toggle_blacksmith()
    else:
        self.status = "left_idle"
        self.sleep = True
```

**In `dialogue_system.py`**, update the fallback method:
```python
def _get_static_fallback(self, character_id: str) -> str:
    fallbacks = {
        "trader": "Welcome, friend! I have many fine goods for a hardworking farmer like you. Let's see what you need.",
        "blacksmith": "Greetings, farmer! I can forge better tools for your farm work. Bring me some metal and I'll craft you something special!"
    }
    return fallbacks.get(character_id, "Hello there! Nice day for farming.")
```

### Step 3: Test Your New NPC

1. Run the game: `python main.py`
2. Walk to position (300, 200) on the map
3. You should see a brown rectangle (the blacksmith)
4. Press Enter near it to trigger dialogue
5. After dialogue, the blacksmith menu should appear
6. Use arrow keys to navigate, Space to select, Esc to exit

---

## 🎯 Quick NPC Addition Template

For future NPCs, use this template:

### 1. Create NPC Class
```python
# In npc_characters.py
class YourNPC(NPCCharacter):
    def __init__(self, pos, groups):
        super().__init__(pos, "your_npc_name", groups)
        self.name = "NPC Display Name"
        self.role = "npc role description"
        self.image.fill((R, G, B))  # Choose color
```

### 2. Add to Level
```python
# In level.py setup()
npc_pos = (x, y)  # Choose position
Interaction(npc_pos, (64, 64), self.interaction_sprites, "YourNPCName")
self.your_npc = YourNPC(npc_pos, self.all_sprites)
```

### 3. Add Interaction Method
```python
# In level.py
def toggle_your_npc(self):
    # Add dialogue logic here
    print("Interacting with your NPC!")
```

### 4. Update Player
```python
# In player.py interaction handling
elif collided_interaction_sprite[0].name == "YourNPCName":
    if self.toggle_your_npc:
        self.toggle_your_npc()
```

### 5. Add Dialogue Fallback
```python
# In dialogue_system.py
"your_npc_name": "Your NPC's default message here!"
```

---

## 🎨 Visual Customization Tips

### Creating NPC Sprites
1. **Size**: NPCs should be similar to player size (32x48 pixels recommended)
2. **Style**: Match the game's pixel art aesthetic
3. **Colors**: Use distinct colors to make NPCs recognizable
4. **Animation**: Start with idle animations, add more complex ones later

### Positioning NPCs
1. **Accessibility**: Place NPCs in easy-to-reach locations
2. **Visual Logic**: Put blacksmiths near forges, librarians near buildings
3. **Spacing**: Ensure NPCs don't overlap with important game elements
4. **Testing**: Walk around the NPC to ensure interaction area works

### Advanced Visual Features
1. **Animated NPCs**: Add walking animations for moving characters
2. **Dialogue Indicators**: Show speech bubbles or "!" when nearby
3. **Day/Night Behavior**: Different sprites for different times
4. **Seasonal Changes**: NPCs that change appearance with seasons

---

## 🏆 Extension Projects

### Beginner Projects
1. **Village Elder**: NPC who gives daily quests
2. **Seed Merchant**: Alternative trader with different items
3. **Weather Prophet**: NPC who predicts tomorrow's weather

### Intermediate Projects
1. **Moving NPCs**: Characters that walk around the map
2. **Quest System**: NPCs that give and track missions
3. **Relationship System**: NPCs with friendship levels

### Advanced Projects
1. **Dynamic Dialogue**: NPCs that remember past conversations
2. **Event System**: NPCs that react to game events
3. **Social Network**: NPCs that talk about each other

---

**🎉 Congratulations!** You now know how to add new characters and NPCs to PyDew Valley. Start with simple stationary NPCs and gradually add more complex features like custom menus, AI dialogues, and interactive systems. Each NPC you add makes the world feel more alive and engaging! 🌟
