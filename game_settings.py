import json
import pygame

# File path for settings
SETTINGS_FILE = "settings.json"

# Default settings
DEFAULT_SETTINGS = {"master_volume": 0.8, "music_volume": 0.7, "sfx_volume": 0.8}

# Global references for audio management
current_level = None
current_player = None


def load_settings():
    """Load settings from JSON file, create default if not exists"""
    try:
        with open(SETTINGS_FILE, "r") as f:
            settings = json.load(f)
            # Ensure all required keys exist
            for key, default_value in DEFAULT_SETTINGS.items():
                if key not in settings:
                    settings[key] = default_value
            return settings
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_SETTINGS.copy()


def save_settings(settings):
    """Save settings to JSON file"""
    try:
        with open(SETTINGS_FILE, "w") as f:
            json.dump(settings, f, indent=2)
    except Exception as e:
        print(f"Error saving settings: {e}")


def get(key, default=None):
    """Get a setting value"""
    settings = load_settings()
    return settings.get(key, default)


def set_volume_percentage(volume_type, percentage):
    """Set volume as percentage (0-100) and save to file"""
    settings = load_settings()
    volume_value = percentage / 100.0
    settings[volume_type] = volume_value
    save_settings(settings)

    # Update audio volumes immediately
    refresh_all_audio()


def set_current_level(level_instance):
    """Set the current level instance for audio management"""
    global current_level
    current_level = level_instance


def set_current_player(player_instance):
    """Set the current player instance for audio management"""
    global current_player
    current_player = player_instance


def refresh_all_audio():
    """Update audio volumes for all game components"""
    if current_level and hasattr(current_level, "update_audio_volumes"):
        current_level.update_audio_volumes()
    if current_player and hasattr(current_player, "update_audio_volumes"):
        current_player.update_audio_volumes()


def update_all_game_audio():
    """Public function to update all game audio volumes"""
    refresh_all_audio()


def get_volume_percentage(volume_type):
    """Get volume as percentage (0-100)"""
    volume_value = get(volume_type, 0.0)
    return int(volume_value * 100)
