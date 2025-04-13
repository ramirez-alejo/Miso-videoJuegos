import pygame

class CPlayer:
    def __init__(self, input_velocity: float, spawn_position: pygame.Vector2 = None, frames: int = 1) -> None:
        self.input_velocity = input_velocity
        self.spawn_position = spawn_position
        self.frames = frames
        
    @classmethod
    def from_dict(cls, player_config, level_config):
        player_spawn = level_config.get("player_spawn", {}).get("position", {"x": 100, "y": 100})
        spawn_position = pygame.Vector2(player_spawn["x"], player_spawn["y"])
        
        frames = player_config.get("animations", {}).get("number_frames", 1)
        
        return cls(
            input_velocity=player_config.get("input_velocity", 100),
            spawn_position=spawn_position,
            frames=frames
        )
