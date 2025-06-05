import pygame
import json
import os


class GameSettings:
    def __init__(self):
        self.settings_file = "settings.json"

        # Default settings
        self.default_settings = {
            "master_volume": 0.7,
            "music_volume": 0.5,
            "sfx_volume": 0.8,
            "fullscreen": False,
        }

        # Current settings (will be loaded from file or defaults)
        self.settings = {}

        # Load settings from file
        self.load_settings()

        # Apply audio settings immediately
        self.apply_audio_settings()

    def load_settings(self):
        """Load settings from JSON file, or use defaults if file doesn't exist"""
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, "r") as f:
                    loaded_settings = json.load(f)
                # Merge with defaults to ensure all keys exist
                self.settings = self.default_settings.copy()
                self.settings.update(loaded_settings)
            else:
                self.settings = self.default_settings.copy()
        except (json.JSONDecodeError, IOError):
            # If file is corrupted or can't be read, use defaults
            self.settings = self.default_settings.copy()

    def save_settings(self):
        """Save current settings to JSON file"""
        try:
            with open(self.settings_file, "w") as f:
                json.dump(self.settings, f, indent=4)
        except IOError:
            print("Warning: Could not save settings to file")

    def get(self, key):
        """Get a setting value"""
        return self.settings.get(key, self.default_settings.get(key))

    def set(self, key, value):
        """Set a setting value and save immediately"""
        if key in self.default_settings:
            self.settings[key] = value

            # Apply audio settings immediately when changed
            if key in ["master_volume", "music_volume", "sfx_volume"]:
                self.apply_audio_settings()

            self.save_settings()

    def apply_audio_settings(self):
        """Apply volume settings to pygame mixer"""
        try:
            # Initialize mixer if it's not already
            if not pygame.mixer.get_init():
                pygame.mixer.init()

            # Set master volume for pygame mixer
            master_vol = self.get("master_volume")
            pygame.mixer.set_num_channels(32)  # Ensure we have enough channels

            # Apply master volume to music globally
            music_vol = self.get("music_volume")
            pygame.mixer.music.set_volume(master_vol * music_vol)

        except pygame.error:
            # Pygame mixer might not be initialized yet
            pass

    def get_volume_percentage(self, volume_type):
        """Get volume as percentage (0-100) for display"""
        return int(self.get(volume_type) * 100)

    def set_volume_percentage(self, volume_type, percentage):
        """Set volume from percentage (0-100)"""
        volume = max(0.0, min(1.0, percentage / 100.0))
        self.set(volume_type, volume)

        # Force immediate audio updates throughout the game
        self.refresh_all_audio()

    def refresh_all_audio(self):
        """Force refresh of all audio volumes in the game"""
        # Apply settings immediately
        self.apply_audio_settings()

        # Update all game audio using global system
        update_all_game_audio()


# Global reference to current level and player instances
_current_level = None
_current_player = None


def set_current_level(level):
    """Set the current level instance for global audio updates"""
    global _current_level
    _current_level = level


def set_current_player(player):
    """Set the current player instance for global audio updates"""
    global _current_player
    _current_player = player


def update_all_game_audio():
    """Update audio volumes for all game components"""
    # Update level audio
    if _current_level and hasattr(_current_level, "update_audio_volumes"):
        _current_level.update_audio_volumes()

    # Update player audio
    if _current_player and hasattr(_current_player, "update_audio_volumes"):
        _current_player.update_audio_volumes()

    # Update global pygame mixer music
    game_settings.apply_audio_settings()


# Global settings instance
game_settings = GameSettings()
