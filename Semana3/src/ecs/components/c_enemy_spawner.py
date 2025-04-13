import pygame
from typing import List, Dict, Any
import pygame

from src.ecs.components.c_enemy import Enemy
from src.ecs.components.c_enemy_spawner_event import EnemySpawnerEvent

class CEnemySpawner:
    def __init__(self, spawn_events: List[EnemySpawnerEvent], enemies: List[Enemy]):
        self.spawn_events = sorted(spawn_events, key=lambda event: event.time)
        self.enemies = enemies
    
    @classmethod
    def from_dict(cls, level_config: Dict[str, Any], enemies_config: Dict[str, Any]) -> 'CEnemySpawner':
        spawn_events = []
        for event_dict in level_config.get("enemy_spawn_events", []):
            spawn_events.append(EnemySpawnerEvent(
                time=event_dict["time"],
                enemy_type=event_dict["enemy_type"],
                position = pygame.Vector2(event_dict["position"]["x"], event_dict["position"]["y"]),
            ))
        
        enemies = []
        for enemy_type, config in enemies_config.items():
            
            enemies.append(Enemy(
                type=enemy_type,
                sprite_image=config["image"],
                velocity_min=config["velocity_min"],
                velocity_max=config["velocity_max"],
            ))
        
        return cls(spawn_events, enemies)