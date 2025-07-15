# 🧙‍♂️ Quick NPC Addition Guide

## ⚡ 5-Minute NPC Setup

### What You Need
- NPC name and role
- Position on the map
- Interaction type (dialogue, menu, quest)

### Quick Commands
```bash
# 1. Run the NPC creator
python npc_creator.py

# 2. Follow the interactive prompts
# 3. Copy generated files to main directory
# 4. Apply code patches to existing files
```

## 🎯 NPC Types

### 1. Simple Dialogue NPC
- **Best for**: Information providers, friendly villagers
- **Features**: Basic conversation with AI-generated responses
- **Example**: Village elder, librarian, helpful farmer

### 2. Menu/Shop NPC  
- **Best for**: Service providers, traders, crafters
- **Features**: Custom interface with options and pricing
- **Example**: Blacksmith, alternative trader, healer

### 3. Quest Giver NPC
- **Best for**: Mission providers, story characters
- **Features**: Task assignment and progress tracking
- **Example**: Mayor, adventure guide, researcher

### 4. Information NPC
- **Best for**: Tutorial helpers, game guides
- **Features**: Context-sensitive help and tips
- **Example**: Farming mentor, tool expert, weather predictor

## 🛠️ Manual NPC Creation (Advanced)

### Step 1: Create NPC Character Class
```python
# npc_name_character.py
import pygame
from sprites import Generic
from settings import LAYERS

class YourNPCName(Generic):
    def __init__(self, pos, groups):
        placeholder = pygame.Surface((32, 48))
        placeholder.fill((R, G, B))  # Choose your color
        super().__init__(pos, placeholder, groups, LAYERS['main'])
        
        self.name = "NPC Display Name"
        self.role = "npc role"
        self.hitbox = self.rect.copy().inflate(-20, -10)
    
    def update(self, dt):
        pass
```

### Step 2: Add to Level System
```python
# In level.py setup() method:
npc_pos = (x, y)  # Your chosen position
Interaction(npc_pos, (64, 64), self.interaction_sprites, "NPCName")
self.your_npc = YourNPCName(npc_pos, self.all_sprites)

# Add interaction method:
def toggle_your_npc(self):
    self.dialogue_system.start_dialogue("npc_id", 
                                       player_context={...}, 
                                       on_finish=self.open_npc_menu)
```

### Step 3: Update Player Interaction
```python
# In player.py __init__:
def __init__(self, ..., toggle_your_npc=None):
    self.toggle_your_npc = toggle_your_npc

# In player.py interaction handling:
elif collided_interaction_sprite[0].name == "NPCName":
    if self.toggle_your_npc:
        self.toggle_your_npc()
```

### Step 4: Add Dialogue Support
```python
# In dialogue_system.py:
def _get_static_fallback(self, character_id: str) -> str:
    fallbacks = {
        # ... existing entries ...
        "npc_id": "Your NPC's default message here!"
    }
```

## 🎨 Customization Quick Tips

### Visual Appearance
```python
# Solid color NPC
self.image.fill((255, 0, 0))  # Red

# Custom sprite (create graphics/npcs/npc_name/idle/ with 4 PNGs)
# The system will auto-load if sprites exist
```

### Positioning Guide
- **Near trader**: (400, 250) 
- **Near house**: (200, 200)
- **Center area**: (500, 400)
- **Safe positions**: Away from trees, water, paths

### Color Coding Ideas
- **🔨 Crafters**: Brown/orange (150, 75, 0)
- **📚 Scholars**: Blue/purple (100, 100, 200)
- **💰 Merchants**: Gold/yellow (200, 200, 0)
- **🌱 Farmers**: Green (0, 150, 50)
- **⚔️ Guards**: Gray/black (100, 100, 100)

## 🎮 Testing Your NPC

### Quick Test Checklist
1. ✅ NPC appears at chosen position
2. ✅ Can walk near NPC without issues
3. ✅ Press Enter near NPC triggers interaction
4. ✅ Dialogue system responds
5. ✅ Menu opens (if applicable)
6. ✅ ESC exits menu properly

### Debug Commands
```python
# Add temporary debug prints:
print(f"🔍 NPC created at {position}")
print(f"🎯 Interaction triggered for {npc.name}")
print(f"💬 Dialogue started with {character_id}")
```

## 🏆 NPC Ideas for Students

### Beginner NPCs
1. **Friendly Cat**: Simple pet that gives encouragement
2. **Weather Watcher**: Tells you tomorrow's weather
3. **Seed Inspector**: Evaluates your crops
4. **Tool Repair**: Fixes broken equipment

### Intermediate NPCs  
1. **Quest Master**: Daily challenges and rewards
2. **Knowledge Bank**: Farming tips and tutorials
3. **Trade Evaluator**: Market price information
4. **Skill Trainer**: Unlocks new abilities

### Advanced NPCs
1. **Moving Merchant**: Travels around the map
2. **Seasonal Character**: Changes with weather/time
3. **Memory Keeper**: Remembers past conversations
4. **Community Board**: Player-to-player messages

## 🚀 Extension Ideas

### Make NPCs Come Alive
1. **Walking Patterns**: NPCs that move around
2. **Schedule System**: Different locations at different times
3. **Relationship Tracking**: Friendship levels that unlock content
4. **Event Reactions**: NPCs respond to player achievements
5. **Seasonal Behavior**: Different dialogue/appearance per season

### Interactive Features
1. **Gift System**: NPCs accept and give presents
2. **Mini-Games**: Small challenges within NPC interactions
3. **Story Arcs**: Multi-stage quests with character development
4. **Social Network**: NPCs that talk about each other

## 🔧 Common Fixes

### NPC Won't Appear
```python
# Check position is valid
print(f"NPC position: {npc_pos}")
# Ensure added to correct sprite group
# Verify import statements
```

### Interaction Not Working
```python
# Check interaction area size
Interaction(pos, (64, 64), ...)  # Larger area
# Verify naming consistency
# Test collision detection
```

### Menu Issues
```python
# Ensure menu class is imported
# Check menu initialization in Level.__init__
# Verify update() call in Level.run()
```

For complete tutorial: See `NPC_TUTORIAL.md`
For automated creation: Run `python npc_creator.py`
