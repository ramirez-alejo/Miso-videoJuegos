import pygame
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

def create_sprite(entity: int,
                    ecs_world: esper.World,
                    sprite_image: str,
                    position: pygame.Vector2 = pygame.Vector2(100, 100),
                    velocity: pygame.Vector2 = pygame.Vector2(100, 100),
                    frames_number: int = 1) -> None:
    
    sprite = pygame.image.load(sprite_image).convert_alpha()
    size = sprite.get_size()
    size = (size[0] / frames_number, size[1])
    relative_position = pygame.Vector2(position.x - size[0] / 2, position.y - size[1] / 2)
    ecs_world.add_component(entity, CSurface.from_surface(sprite))
    ecs_world.add_component(entity, CTransform(relative_position))
    ecs_world.add_component(entity, CVelocity(velocity))
    return entity