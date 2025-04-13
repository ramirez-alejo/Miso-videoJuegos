import pygame

class Enemy:
    def __init__(self, type: str, velocity_min: int, velocity_max: int, sprite_image: str) -> None:
        self.type = type
        self.velocity_min = velocity_min
        self.velocity_max = velocity_max
        self.sprite_image = sprite_image