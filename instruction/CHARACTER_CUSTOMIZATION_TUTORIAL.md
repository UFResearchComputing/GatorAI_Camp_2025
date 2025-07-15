# 🎨 Character Customization Tutorial: Add Your Own Character to PyDew Valley

## 📋 Table of Contents
1. [Understanding the Character System](#understanding-the-character-system)
2. [Preparing Your Character Sprites](#preparing-your-character-sprites)
3. [Step-by-Step Implementation Guide](#step-by-step-implementation-guide)
4. [Advanced Customization Options](#advanced-customization-options)
5. [Troubleshooting Common Issues](#troubleshooting-common-issues)
6. [Tips for Creating Great Character Art](#tips-for-creating-great-character-art)

---

## 🔍 Understanding the Character System

Before we start adding your custom character, let's understand how the game's character system works:

### Character Animation Structure
The game uses a **sprite-based animation system** where each character action requires multiple PNG files:

```
graphics/character/
├── down/           # Walking downward (4 frames: 0.png, 1.png, 2.png, 3.png)
├── down_idle/      # Standing still facing down (4 frames)
├── down_hoe/       # Using hoe tool facing down (4 frames)
├── down_axe/       # Using axe tool facing down (4 frames)
├── down_water/     # Using watering can facing down (4 frames)
├── left/           # Walking left (4 frames)
├── left_idle/      # Standing still facing left (4 frames)
├── left_hoe/       # Using hoe tool facing left (4 frames)
├── left_axe/       # Using axe tool facing left (4 frames)
├── left_water/     # Using watering can facing left (4 frames)
├── right/          # Walking right (4 frames)
├── right_idle/     # Standing still facing right (4 frames)
├── right_hoe/      # Using hoe tool facing right (4 frames)
├── right_axe/      # Using axe tool facing right (4 frames)
├── right_water/    # Using watering can facing right (4 frames)
├── up/             # Walking upward (4 frames)
├── up_idle/        # Standing still facing up (4 frames)
├── up_hoe/         # Using hoe tool facing up (4 frames)
├── up_axe/         # Using axe tool facing up (4 frames)
└── up_water/       # Using watering can facing up (4 frames)
```

### Required Animation States
Your character needs **20 different animation states** × **4 frames each** = **80 total PNG files**

---

## 🎨 Preparing Your Character Sprites

### Option 1: Using Online Sprite Editors (Recommended for Beginners)

#### **Piskel** (Free, Browser-based)
1. Go to [Piskel.com](https://www.piskelapp.com/)
2. Create a **16x32 pixel** canvas (this matches the original character size)
3. Design your character facing down
4. Create 4 frames for walking animation
5. Export as PNG files

#### **Aseprite** (Paid, Professional)
1. Download Aseprite ($19.99)
2. Create new sprite: **16x32 pixels**
3. Use onion skinning for smooth animations
4. Export frame sequence as PNG

### Option 2: Converting Existing Art
If you have character art from other sources:

1. **Resize** to 16x32 pixels using image editing software
2. **Split into frames** if it's a sprite sheet
3. **Ensure transparency** (save as PNG with alpha channel)
4. **Name files correctly** (0.png, 1.png, 2.png, 3.png)

### Sprite Requirements Checklist
- ✅ **Size**: 16x32 pixels per frame
- ✅ **Format**: PNG with transparency
- ✅ **Frames**: Exactly 4 frames per animation
- ✅ **Colors**: Any color palette (but consider game's aesthetic)
- ✅ **Transparency**: Proper alpha channel for background

---

## 📁 Step-by-Step Implementation Guide

### Step 1: Create Backup
Always backup your original files first!

```powershell
# Navigate to your game directory
cd d:\GatorAI_Camp_2025

# Create backup of original character graphics
cp -r graphics\character graphics\character_original_backup
```

### Step 2: Organize Your New Character Files

Create your character sprites and organize them like this:

```
your_character_files/
├── down/
│   ├── 0.png
│   ├── 1.png
│   ├── 2.png
│   └── 3.png
├── down_idle/
│   ├── 0.png
│   ├── 1.png
│   ├── 2.png
│   └── 3.png
├── down_hoe/
│   ├── 0.png
│   ├── 1.png
│   ├── 2.png
│   └── 3.png
[... and so on for all 20 animation states]
```

### Step 3: Replace Character Files

#### Method A: Complete Character Replacement (Easiest)
```powershell
# Remove old character files
rm -r graphics\character\*

# Copy your new character files
cp -r your_character_files\* graphics\character\
```

#### Method B: Character Selection System (Advanced)
We'll create a character selection system that lets players choose between multiple characters.

### Step 4: Test Your Character

1. **Run the game**:
   ```powershell
   python main.py
   ```

2. **Check for errors** in the console
3. **Test all animations** by moving and using tools
4. **Verify transparency** - no white/black boxes around character

### Step 5: Quick Character Test Script

Create a test script to verify your character files:

```python
# test_character.py
import pygame
import os
from support import import_folder

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Character Test")

# Test loading all animations
animations = [
    "down", "down_idle", "down_hoe", "down_axe", "down_water",
    "left", "left_idle", "left_hoe", "left_axe", "left_water", 
    "right", "right_idle", "right_hoe", "right_axe", "right_water",
    "up", "up_idle", "up_hoe", "up_axe", "up_water"
]

print("Testing character animations...")
for animation in animations:
    try:
        frames = import_folder(f"graphics/character/{animation}")
        print(f"✅ {animation}: {len(frames)} frames loaded")
    except Exception as e:
        print(f"❌ {animation}: ERROR - {e}")

print("Character test complete!")
pygame.quit()
```

Run this test with:
```powershell
python test_character.py
```

---

## 🚀 Advanced Customization Options

### Option 1: Multiple Character Support

Let's create a system where players can choose between different characters!

#### Step 1: Modify the Character Structure
```
graphics/
├── characters/
│   ├── farmer/           # Original character
│   │   ├── down/
│   │   ├── down_idle/
│   │   └── ... (all animations)
│   ├── knight/           # Your new character
│   │   ├── down/
│   │   ├── down_idle/
│   │   └── ... (all animations)
│   └── wizard/           # Another character
│       ├── down/
│       ├── down_idle/
│       └── ... (all animations)
└── character/            # Current active character (symlink or copy)
```

#### Step 2: Create Character Selection Code

Create `character_selector.py`:
```python
import os
import shutil
from pathlib import Path

class CharacterSelector:
    def __init__(self):
        self.base_path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.characters_path = self.base_path / "graphics" / "characters"
        self.active_character_path = self.base_path / "graphics" / "character"
        
    def get_available_characters(self):
        """Get list of available character folders"""
        if not self.characters_path.exists():
            return []
        return [d.name for d in self.characters_path.iterdir() if d.is_dir()]
    
    def switch_character(self, character_name):
        """Switch to a different character"""
        character_path = self.characters_path / character_name
        
        if not character_path.exists():
            print(f"Character '{character_name}' not found!")
            return False
            
        # Remove current character
        if self.active_character_path.exists():
            shutil.rmtree(self.active_character_path)
            
        # Copy new character
        shutil.copytree(character_path, self.active_character_path)
        print(f"Switched to character: {character_name}")
        return True
    
    def create_character_menu(self):
        """Interactive character selection menu"""
        characters = self.get_available_characters()
        
        if not characters:
            print("No characters found in graphics/characters/")
            return
            
        print("\n=== Character Selection ===")
        for i, char in enumerate(characters, 1):
            print(f"{i}. {char.title()}")
            
        try:
            choice = int(input(f"\nSelect character (1-{len(characters)}): ")) - 1
            if 0 <= choice < len(characters):
                self.switch_character(characters[choice])
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter a number!")

# Usage
if __name__ == "__main__":
    selector = CharacterSelector()
    selector.create_character_menu()
```

#### Step 3: Add Character Selection to Main Menu

Modify `main_menu.py` to include character selection:

```python
# Add this to the MainMenu class in main_menu.py

def display_character_select(self):
    """Display character selection screen"""
    from character_selector import CharacterSelector
    
    selector = CharacterSelector()
    characters = selector.get_available_characters()
    
    # Title
    title_surf = self.title_font.render("Choose Character", True, "White")
    title_rect = title_surf.get_rect(center=(SCREEN_WIDTH / 2, 100))
    self.display_surface.blit(title_surf, title_rect)
    
    # Character options
    start_y = 200
    for i, character in enumerate(characters):
        color = "Yellow" if i == self.selected_character else "White"
        char_surf = self.font.render(f"{i+1}. {character.title()}", True, color)
        char_rect = char_surf.get_rect(center=(SCREEN_WIDTH / 2, start_y + i * 60))
        self.display_surface.blit(char_surf, char_rect)
    
    # Instructions
    instruction_surf = self.font.render("Press NUMBER to select, ESC to return", True, "White")
    instruction_rect = instruction_surf.get_rect(center=(SCREEN_WIDTH / 2, start_y + len(characters) * 60 + 60))
    self.display_surface.blit(instruction_surf, instruction_rect)
```

### Option 2: Character Customization System

Create a more advanced system where players can mix and match character parts:

```python
# character_customizer.py
import pygame
import os
from pathlib import Path

class CharacterCustomizer:
    def __init__(self):
        self.base_path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.parts_path = self.base_path / "graphics" / "character_parts"
        
    def combine_character_parts(self, head_style, body_style, outfit_style):
        """Combine different character parts into a complete character"""
        # Load base body
        body_frames = self.load_part_frames("body", body_style)
        
        # Load head overlay
        head_frames = self.load_part_frames("head", head_style)
        
        # Load outfit overlay
        outfit_frames = self.load_part_frames("outfit", outfit_style)
        
        # Combine all parts
        combined_character = self.layer_parts(body_frames, head_frames, outfit_frames)
        
        return combined_character
        
    def load_part_frames(self, part_type, style):
        """Load animation frames for a specific character part"""
        part_path = self.parts_path / part_type / style
        frames = {}
        
        animations = ["down", "down_idle", "down_hoe", "down_axe", "down_water",
                     "left", "left_idle", "left_hoe", "left_axe", "left_water",
                     "right", "right_idle", "right_hoe", "right_axe", "right_water",
                     "up", "up_idle", "up_hoe", "up_axe", "up_water"]
        
        for animation in animations:
            frames[animation] = []
            animation_path = part_path / animation
            
            if animation_path.exists():
                for i in range(4):  # 4 frames per animation
                    frame_path = animation_path / f"{i}.png"
                    if frame_path.exists():
                        frames[animation].append(pygame.image.load(frame_path))
                        
        return frames
        
    def layer_parts(self, body, head, outfit):
        """Layer character parts on top of each other"""
        combined = {}
        
        for animation in body.keys():
            combined[animation] = []
            
            for i in range(4):  # 4 frames
                # Create a new surface
                combined_frame = pygame.Surface((16, 32), pygame.SRCALPHA)
                
                # Layer the parts: body first, then head, then outfit
                if body[animation] and i < len(body[animation]):
                    combined_frame.blit(body[animation][i], (0, 0))
                    
                if head[animation] and i < len(head[animation]):
                    combined_frame.blit(head[animation][i], (0, 0))
                    
                if outfit[animation] and i < len(outfit[animation]):
                    combined_frame.blit(outfit[animation][i], (0, 0))
                    
                combined[animation].append(combined_frame)
                
        return combined
```

---

## 🛠️ Troubleshooting Common Issues

### Problem: Character appears as white/black rectangle
**Solution**: Your PNG files don't have proper transparency
- Use an image editor to add transparency
- Save as PNG-24 with alpha channel
- Test transparency in image viewer first

### Problem: Game crashes with "FileNotFoundError"
**Solution**: Missing animation files
- Check that all 20 animation folders exist
- Ensure each folder has exactly 4 PNG files (0.png, 1.png, 2.png, 3.png)
- Use the test script provided above to identify missing files

### Problem: Character animations look choppy
**Solution**: Frame timing or size issues
- Ensure all frames are exactly 16x32 pixels
- Check that frames flow smoothly together
- Consider adding more in-between frames

### Problem: Character appears too small/large
**Solution**: Scale issues
- Character should be 16x32 pixels
- If your art is larger, resize it proportionally
- Use pixel art scaling (nearest neighbor) to maintain crisp edges

### Problem: Character doesn't line up with tools
**Solution**: Tool positioning is based on character center
- Tools are positioned relative to character's center point
- If your character is very different, you may need to adjust `PLAYER_TOOL_OFFSET` in `settings.py`

---

## 🎨 Tips for Creating Great Character Art

### Pixel Art Best Practices
1. **Use a limited color palette** (8-16 colors max)
2. **Maintain consistent style** across all animations
3. **Keep details minimal** at 16x32 resolution
4. **Use contrast** to make features stand out
5. **Study the original character** for proportions and style

### Animation Tips
1. **Start with key poses** (extreme positions)
2. **Add in-between frames** for smoother motion
3. **Use reference** - record yourself walking!
4. **Keep it subtle** - small movements work better at this scale
5. **Test frequently** - see how it looks in-game

### Tool Animation Guidelines
1. **Show clear tool usage** - make it obvious what the character is doing
2. **Keep tools consistent** with game's existing tool sprites
3. **Add anticipation** - wind up before the action
4. **Include follow-through** - recovery after the action

### Color Scheme Ideas
- **Fantasy**: Bright blues, purples, golds
- **Modern**: Realistic skin tones, contemporary clothing colors
- **Retro**: Limited NES/Game Boy color palettes
- **Seasonal**: Colors that match different seasons in the game

---

## 🎮 Example: Quick Character Replacement

Here's a step-by-step example of replacing the character with a simple recolor:

### Step 1: Extract Original Character
```powershell
# Create a working directory
mkdir my_character
cd my_character

# Copy original character for editing
cp -r ..\graphics\character\* .
```

### Step 2: Edit with Simple Tools
You can use free tools like:
- **GIMP** (Free, powerful)
- **Paint.NET** (Windows, user-friendly)
- **Krita** (Free, excellent for digital art)

### Step 3: Batch Edit for Consistency
If you just want to change colors:

```python
# color_changer.py - Simple script to change character colors
import pygame
import os
from pathlib import Path

def change_color(image, old_color, new_color):
    """Change one color to another in an image"""
    result = image.copy()
    pygame.PixelArray(result)[:] = result.map_rgb(lambda r, g, b: 
        new_color if (r, g, b) == old_color else (r, g, b))
    return result

def process_character_folder(folder_path, color_changes):
    """Process all PNG files in a folder to change colors"""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.png'):
                file_path = os.path.join(root, file)
                
                # Load image
                image = pygame.image.load(file_path)
                
                # Apply color changes
                for old_color, new_color in color_changes.items():
                    image = change_color(image, old_color, new_color)
                
                # Save modified image
                pygame.image.save(image, file_path)
                print(f"Processed: {file_path}")

# Example usage
pygame.init()
color_changes = {
    (139, 69, 19): (255, 0, 0),    # Change brown hair to red
    (255, 220, 177): (255, 200, 150),  # Change skin tone
    (0, 100, 0): (0, 0, 200),      # Change green shirt to blue
}

process_character_folder("graphics/character", color_changes)
print("Character recoloring complete!")
```

### Step 4: Test and Iterate
```powershell
# Test your changes
python main.py

# If there are issues, restore backup and try again
cp -r graphics\character_original_backup\* graphics\character\
```

---

## 🎯 Challenge Projects

Once you've mastered basic character replacement, try these advanced projects:

### Beginner Challenge: Seasonal Characters
Create 4 versions of your character for different seasons:
- **Spring**: Green clothing, flower accessories
- **Summer**: Light colors, sun hat
- **Fall**: Orange/brown colors, warm clothes
- **Winter**: Heavy coat, winter accessories

### Intermediate Challenge: Professional Characters
Create characters for different professions:
- **Chef**: Chef's hat, apron
- **Adventurer**: Armor, cape
- **Scientist**: Lab coat, goggles
- **Artist**: Paint-splattered clothes, beret

### Advanced Challenge: Animated Accessories
Add accessories that animate independently:
- **Flowing cape** that waves in the wind
- **Glowing magical aura** around the character
- **Pet companion** that follows the character
- **Dynamic hair** that bounces with movement

---

## 📚 Resources and Tools

### Free Sprite Creation Tools
- **Piskel**: https://www.piskelapp.com/ (Browser-based)
- **GIMP**: https://www.gimp.org/ (Full image editor)
- **Krita**: https://krita.org/ (Digital painting)
- **LibreSprite**: https://libresprite.github.io/ (Aseprite alternative)

### Paid Tools (Professional)
- **Aseprite**: https://www.aseprite.org/ ($19.99)
- **PyxelEdit**: https://pyxeledit.com/ ($9)
- **Pro Motion NG**: https://www.cosmigo.com/ ($39)

### Learning Resources
- **Pixel Art Tutorials**: https://lospec.com/articles/
- **Game Art**: https://opengameart.org/
- **Sprite References**: https://www.spriters-resource.com/
- **Color Palettes**: https://lospec.com/palette-list

### Inspiration Sources
- **Classic RPGs**: Final Fantasy, Secret of Mana
- **Indie Games**: Stardew Valley, Hyper Light Drifter
- **Pixel Art Communities**: r/PixelArt, DeviantArt

---

## 🏆 Sharing Your Creation

Once you've created an awesome character, consider sharing it!

### Create a Character Pack
```
MyCharacterPack/
├── README.md                 # Description and credits
├── preview.gif              # Animated preview
├── installation.md          # Installation instructions
└── character/               # Character files
    ├── down/
    ├── down_idle/
    └── ... (all animations)
```

### Share on Platforms
- **GitHub**: Create a repository for your character pack
- **Itch.io**: Upload as a free asset pack
- **Reddit**: Share in r/PixelArt or r/gamedev
- **Discord**: Join game development communities

---

**🎉 Congratulations!** You now have everything you need to create and implement your own custom character in PyDew Valley. Remember, creating good pixel art takes practice, so don't get discouraged if your first attempts aren't perfect. The most important thing is to have fun and keep experimenting!

Happy character creating! 🌟
