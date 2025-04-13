import pygame
from typing import Dict, Any, Optional

class Enemy:
    def __init__(self, type: str, sprite_image: str, 
                 velocity_min: int = 0, velocity_max: int = 0,
                 animations: Optional[Dict[str, Any]] = None,
                 velocity_chase: float = 0, velocity_return: float = 0,
                 distance_start_chase: float = 0, distance_start_return: float = 0) -> None:
        self.type = type
        self.velocity_min = velocity_min
        self.velocity_max = velocity_max
        self.sprite_image = sprite_image
        self.animations = animations
        self.velocity_chase = velocity_chase
        self.velocity_return = velocity_return
        self.distance_start_chase = distance_start_chase
        self.distance_start_return = distance_start_return
