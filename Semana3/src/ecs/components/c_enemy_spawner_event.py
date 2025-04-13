import pygame

class EnemySpawnerEvent:
    def __init__(self, time: float, enemy_type: str, position: pygame.Vector2) -> None:
        self.time = time
        self.enemy_type = enemy_type
        self.position = position