# 🎮 PyDew Valley: Educational Game Development Roadmap

## 🎯 Project Overview

**PyDew Valley** is an educational farming simulation game designed to teach Python programming concepts through game development. Students learn programming fundamentals while building a complete 2D game using Pygame.

---

## 📋 File Architecture Overview

### 🏗️ Core Architecture Diagram

```
🎮 PYDEW VALLEY GAME ARCHITECTURE
═══════════════════════════════════════════════════════════════════════

                           [main.py] 🚀
                         ENTRY POINT & GAME LOOP
                        ┌─────────────────────────┐
                        │ • Game initialization  │
                        │ • Main game loop       │
                        │ • Event handling       │
                        │ • Screen management    │
                        └─────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
               [main_menu.py]   [level.py]    [character_screen.py]
              MENU SYSTEM      GAME WORLD      PLAYER STATS UI
             ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
             │ • Start     │  │ • Map mgmt  │  │ • Inventory │
             │ • Settings  │  │ • Sprites   │  │ • Stats     │
             │ • Credits   │  │ • Camera    │  │ • Money     │
             └─────────────┘  └─────────────┘  └─────────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
         [player.py]           [sprites.py]         [soil.py]
        PLAYER CHARACTER       GAME OBJECTS      FARMING SYSTEM
       ┌─────────────────┐   ┌─────────────┐   ┌─────────────┐
       │ • Movement      │   │ • Trees     │   │ • Planting  │
       │ • Animation     │   │ • Water     │   │ • Growth    │
       │ • Tools/Seeds   │   │ • Objects   │   │ • Watering  │
       │ • Inventory     │   │ • Particles │   │ • Harvest   │
       └─────────────────┘   └─────────────┘   └─────────────┘

                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
         [overlay.py]          [sky.py]           [transition.py]
           UI SYSTEM         WEATHER SYSTEM        DAY/NIGHT
       ┌─────────────┐      ┌─────────────┐     ┌─────────────┐
       │ • Tool UI   │      │ • Rain      │     │ • Sleep     │
       │ • Seed UI   │      │ • Sky color │     │ • Reset     │
       │ • Controls  │      │ • Particles │     │ • Effects   │
       └─────────────┘      └─────────────┘     └─────────────┘

═══════════════════════════════════════════════════════════════════════
                         SUPPORTING SYSTEMS
═══════════════════════════════════════════════════════════════════════

    [settings.py]     [support.py]     [timer.py]     [installer.py]
   GAME CONFIG      UTILITY FUNCS     TIMING SYSTEM   DEPENDENCY MGT
  ┌─────────────┐  ┌─────────────┐   ┌─────────────┐  ┌─────────────┐
  │ • Constants │  │ • File load │   │ • Cooldowns │  │ • Auto pip  │
  │ • Positions │  │ • Image mgmt│   │ • Delays    │  │ • Imports   │
  │ • Layers    │  │ • Utilities │   │ • Callbacks │  │ • Packages  │
  └─────────────┘  └─────────────┘   └─────────────┘  └─────────────┘

═══════════════════════════════════════════════════════════════════════
                              AI FEATURES
═══════════════════════════════════════════════════════════════════════

    [emotion_detector.py]    [dialogue_system.py]    [ai_dialogue_manager.py]
       AI EMOTION RECOG         CONVERSATION UI            AI CHATBOT
      ┌─────────────────┐     ┌─────────────────┐      ┌─────────────────┐
      │ • Camera feed   │     │ • NPC dialogue  │      │ • OpenAI API    │
      │ • CNN model     │     │ • Text display  │      │ • Context aware │
      │ • Real-time     │     │ • Input handling│      │ • Emotion-based │
      │ • Threading     │     │ • State machine │      │ • Dynamic text  │
      └─────────────────┘     └─────────────────┘      └─────────────────┘

═══════════════════════════════════════════════════════════════════════
                             TRADING SYSTEM
═══════════════════════════════════════════════════════════════════════

         [trader_menu.py]           [game_settings.py]
           SHOP INTERFACE             PERSISTENT CONFIG
          ┌─────────────────┐       ┌─────────────────┐
          │ • Buy/Sell UI   │       │ • Audio levels  │
          │ • Inventory mgmt│       │ • Game options  │
          │ • Price system │       │ • Save/Load     │
          │ • Navigation    │       │ • Camera setup │
          └─────────────────┘       └─────────────────┘
```

---

## 📚 Educational Learning Path

### 🔰 Beginner Level (Week 1)

**Files to Study First:**
1. `main.py` - Game structure and main loop
2. `settings.py` - Constants and configuration
3. `player.py` - Character movement and input
4. `support.py` - Helper functions

**Key Concepts:**
- Basic Python syntax and imports
- Classes and objects
- Game loops and event handling
- Coordinate systems

### 🔸 Intermediate Level (Week 1-2)

**Files to Study Next:**
1. `level.py` - Complex system management
2. `sprites.py` - Object-oriented design
3. `soil.py` - Game mechanics implementation
4. `overlay.py` - User interface design

**Key Concepts:**
- Advanced OOP (inheritance, polymorphism)
- Sprite groups and collision detection
- File I/O and data management
- UI/UX design principles

### 🔶 Advanced Level (Week 2)

**Files to Study Finally:**
1. `emotion_detector.py` - AI/ML integration
2. `dialogue_system.py` - Complex state machines
3. `ai_dialogue_manager.py` - API integration
4. `game_settings.py` - Persistent data storage

**Key Concepts:**
- Machine learning integration
- Threading and asynchronous programming
- API integration and web requests
- Advanced state management

---

## 🗂️ File Categories & Dependencies

### 🏗️ Core Framework
- **`main.py`** - Entry point, orchestrates everything
- **`level.py`** - Game world manager
- **`player.py`** - Main character controller

### 🎨 Visual Systems
- **`sprites.py`** - Game objects and entities
- **`overlay.py`** - User interface elements
- **`sky.py`** - Weather and atmosphere
- **`transition.py`** - Screen transitions

### 🎮 Game Mechanics
- **`soil.py`** - Farming simulation
- **`trader_menu.py`** - Commerce system
- **`character_screen.py`** - Player statistics

### 🔧 Utilities & Support
- **`settings.py`** - Game configuration
- **`support.py`** - Helper functions
- **`timer.py`** - Timing and cooldowns
- **`installer.py`** - Dependency management

### 🤖 AI Integration
- **`emotion_detector.py`** - Computer vision
- **`dialogue_system.py`** - Conversation management
- **`ai_dialogue_manager.py`** - AI-powered responses

### 🎵 Audio & Settings
- **`game_settings.py`** - Persistent configuration
- **`settings_menu.py`** - Settings interface

---

## 🔄 Data Flow Architecture

```
GAME DATA FLOW OVERVIEW
════════════════════════════════════════════════════════════════

┌─────────────┐    Events     ┌─────────────┐    Updates
│   USER      │ ───────────── │   MAIN.PY   │ ─────────────┐
│   INPUT     │               │  GAME LOOP  │              │
└─────────────┘               └─────────────┘              │
                                     │                     │
                              Screen Management             │
                                     │                     │
                    ┌────────────────┼────────────────┐    │
                    │                │                │    │
            ┌───────▼───────┐ ┌──────▼──────┐ ┌──────▼──────┐
            │   MAIN MENU   │ │    LEVEL    │ │ CHARACTER   │
            │               │ │   (WORLD)   │ │   SCREEN    │
            └───────────────┘ └─────────────┘ └─────────────┘
                                     │
                          World State Management
                                     │
        ┌─────────────┬──────────────┼──────────────┬─────────────┐
        │             │              │              │             │
   ┌────▼────┐  ┌────▼────┐   ┌─────▼─────┐  ┌────▼────┐  ┌────▼────┐
   │ PLAYER  │  │ SPRITES │   │   SOIL    │  │ OVERLAY │  │   SKY   │
   │         │  │         │   │ (FARMING) │  │  (UI)   │  │(WEATHER)│
   └─────────┘  └─────────┘   └───────────┘  └─────────┘  └─────────┘
        │             │              │              │             │
        └─────────────┴──────────────┼──────────────┴─────────────┘
                                     │
                          ┌──────────▼──────────┐
                          │     GAME STATE      │
                          │   • Inventory       │
                          │   • Money           │
                          │   • Tools/Seeds     │
                          │   • World Changes   │
                          └─────────────────────┘
```

---

## 🎯 Learning Objectives by File

### 📊 Difficulty Matrix

| File | Complexity | Concepts | Prerequisites |
|------|------------|----------|---------------|
| `installer.py` | ⭐ | Imports, subprocess | None |
| `settings.py` | ⭐ | Constants, dictionaries | Basic Python |
| `timer.py` | ⭐⭐ | Classes, callbacks | OOP basics |
| `support.py` | ⭐⭐ | File I/O, functions | Functions |
| `main.py` | ⭐⭐⭐ | Game loops, architecture | Classes, events |
| `player.py` | ⭐⭐⭐ | Complex OOP, state mgmt | Sprites, vectors |
| `level.py` | ⭐⭐⭐⭐ | System integration | All above |
| `emotion_detector.py` | ⭐⭐⭐⭐⭐ | AI/ML, threading | Advanced Python |

---

## 🚀 Getting Started Guide

### Environment Setup
```bash
# Clone the repository
git clone https://github.com/UFResearchComputing/GatorAI_Camp_2025
cd GatorAI_Camp_2025

# Run the game (dependencies auto-install)
python main.py
```

---

*This roadmap serves as both a technical reference and educational guide for the GatorAI Camp 2025 program.*
