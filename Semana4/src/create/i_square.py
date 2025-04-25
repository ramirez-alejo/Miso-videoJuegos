import pygame
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

def create_square(entity: int,
                    ecs_world: esper.World,
                    size: pygame.Vector2 = pygame.Vector2(50, 50),
                    color: pygame.Color = pygame.Color(100, 100, 200),
                    position: pygame.Vector2 = pygame.Vector2(100, 100),
                    velocity: pygame.Vector2 = pygame.Vector2(100, 100)) -> None:
    ecs_world.add_component(entity, CSurface(size, color))
    ecs_world.add_component(entity, CTransform(position))
    ecs_world.add_component(entity, CVelocity(velocity))
    return entity