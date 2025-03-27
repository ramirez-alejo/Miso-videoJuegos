from typing import List
import esper
import pygame

from src.create.i_enemy import create_enemy
from src.ecs.components.c_enemy import Enemy
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.c_enemy_spawner_event import EnemySpawnerEvent


    
def system_spawner(world: esper.World, 
           spawner: CEnemySpawner,
           elapsed_time: float
           ) -> None:
    if not spawner.spawn_events:
        return
    events_to_process = [event for event in spawner.spawn_events if event.time <= elapsed_time]
    for event in events_to_process:
        _spawn_enemy(world, event, spawner.enemies)
        spawner.spawn_events.remove(event)

def _spawn_enemy(world: esper.World, event: EnemySpawnerEvent, enemies: List[Enemy]) -> None:
    enemy_type = event.enemy_type
    # from the enemy list the one with the type of the enemy
    matching_enemies = [enemy for enemy in enemies if enemy.type == enemy_type]
    
    if matching_enemies:
        enemy = matching_enemies[0]
        create_enemy(world, enemy, event.position)