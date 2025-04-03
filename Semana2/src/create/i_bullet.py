import esper
import pygame
import math
from src.create.i_square import create_square
from src.ecs.components.c_bullet import CBullet
from src.ecs.components.c_tag_bullet import CTagBullet

def create_bullet(world: esper.World, bullet_config, position: pygame.Vector2, target_position: pygame.Vector2) -> int:
    # Calculate direction vector from player to target
    direction = pygame.Vector2(target_position.x - position.x, target_position.y - position.y)
    
    # Normalize the direction vector
    if direction.length() > 0:
        direction = direction.normalize()
    
    # Get bullet velocity from config
    bullet_velocity = bullet_config.get("velocity", 200)
    
    # Calculate velocity components
    velocity = pygame.Vector2(
        direction.x * bullet_velocity,
        direction.y * bullet_velocity
    )
    
    # Create bullet entity
    bullet_entity = create_square(
        entity=world.create_entity(),
        ecs_world=world,
        size=pygame.Vector2(bullet_config["size"]["x"], bullet_config["size"]["y"]),
        color=pygame.Color(bullet_config["color"]["r"], bullet_config["color"]["g"], bullet_config["color"]["b"]),
        position=position,
        velocity=velocity
    )
    
    # Add bullet-specific components
    world.add_component(bullet_entity, CBullet(bullet_velocity))
    world.add_component(bullet_entity, CTagBullet())
    
    return bullet_entity
