import pygame

class CPlayer:
    def __init__(self, input_velocity: float) -> None:
        self.input_velocity = input_velocity
        
    @classmethod
    def from_dict(cls, player_config):
        return cls(
            input_velocity=player_config.get("input_velocity", 100)
        )
