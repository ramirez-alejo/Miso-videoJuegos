import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "assets", "cfg")

def load_config(filename):
    filepath = os.path.join(CONFIG_PATH, filename)
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
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
