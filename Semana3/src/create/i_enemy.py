import random
import esper
import math
import pygame
from src.create.i_sprite import create_sprite
from src.ecs.components.c_enemy import Enemy
from src.ecs.components.c_tag_enemy import CTagEnemy
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_hunter import CHunter

def create_enemy(world: esper.World, enemy: Enemy, position: pygame.Vector2) -> int:
    enemy_entity = None
    
    if enemy.type == "Hunter":
        enemy_entity = create_sprite(
            entity=world.create_entity(),
            ecs_world=world,
            sprite_image=enemy.sprite_image,
            position=position,
            velocity=pygame.Vector2(0, 0),
            frames_number=enemy.animations["number_frames"] if hasattr(enemy, "animations") else 1
        )
        
        world.add_component(enemy_entity, CHunter(
            origin_position=position,
            distance_start_chase=enemy.distance_start_chase,
            distance_start_return=enemy.distance_start_return,
            velocity_chase=enemy.velocity_chase,
            velocity_return=enemy.velocity_return
        ))
        
        if hasattr(enemy, "animations"):
            world.add_component(enemy_entity, CAnimation.from_dict(enemy.animations))
    else:
        angle = random.uniform(0, 360)
        speed = random.uniform(enemy.velocity_min, enemy.velocity_max)
        
        vel_x = speed * math.cos(math.radians(angle))
        vel_y = speed * math.sin(math.radians(angle))
        
        enemy_entity = create_sprite(
            entity=world.create_entity(),
            ecs_world=world,
            sprite_image=enemy.sprite_image,
            position=position,
            velocity=pygame.Vector2(vel_x, vel_y)
        )
    
    world.add_component(enemy_entity, CTagEnemy())
    
    return enemy_entity
