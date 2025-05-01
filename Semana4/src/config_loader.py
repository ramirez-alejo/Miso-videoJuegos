import json
import os
import sys

# Handle PyInstaller's special _MEIPASS directory for bundled resources
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    # Running as compiled executable
    BASE_PATH = sys._MEIPASS
else:
    # Running in normal Python environment
    BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

CONFIG_PATH = os.path.join(BASE_PATH, "assets", "cfg")

def load_config(filename):
    filepath = os.path.join(CONFIG_PATH, filename)
    try:
        with open(filepath, 'r') as file:
            config = json.load(file)
            print(f"Successfully loaded config: {filepath}")
            return config
    except FileNotFoundError:
        print(f"Configuration file not found: {filepath}")
        return {}
    except json.JSONDecodeError:
        print(f"Error parsing configuration file: {filepath}")
        return {}

def get_window_config():
    return load_config("window.json")

def get_enemies_config():
    return load_config("enemies.json")

def get_level_config(level_name):
    return load_config(f"{level_name}.json")

def get_player_config():
    return load_config("player.json")

def get_bullet_config():
    return load_config("bullet.json")

def get_explosion_config():
    return load_config("explosion.json")