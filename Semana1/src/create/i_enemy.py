import random
import esper
import math
import pygame
from src.create.i_square import create_square
from src.ecs.components.c_enemy import Enemy

def create_enemy(world: esper.World, enemy: Enemy, position: pygame.Vector2) -> int:
    
    # Random angle for movement
    angle = random.uniform(0, 360)
    speed = random.uniform(enemy.velocity_min, enemy.velocity_max)
    
    # Calculate velocity components
    vel_x = speed * math.cos(math.radians(angle))
    vel_y = speed * math.sin(math.radians(angle))
    
    # Use create_square to create the enemy entity
    enemy_entity = create_square(
        entity=world.create_entity(),
        ecs_world=world,
        size=enemy.size,
        color=enemy.color,
        position=position,
        velocity=pygame.Vector2(vel_x, vel_y)
    )
    
    return enemy_entity
