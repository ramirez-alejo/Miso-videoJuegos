import pygame

class Enemy:
    def __init__(self, type: str, size: pygame.Vector2, velocity_min: int, velocity_max: int, color: pygame.Color) -> None:
        self.type = type
        self.size = size
        self.velocity_min = velocity_min
        self.velocity_max = velocity_max
        self.color = color