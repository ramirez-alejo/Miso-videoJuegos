import pygame

class CBullet:
    """Component for bullet entities"""
    def __init__(self, velocity: float) -> None:
        self.velocity = velocity
    
    @classmethod
    def from_dict(cls, bullet_config):
        return cls(
            velocity=bullet_config.get("velocity", 200)
        )
