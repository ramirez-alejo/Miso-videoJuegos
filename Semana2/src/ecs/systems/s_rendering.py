import esper
import pygame
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform

def system_rendering(world: esper.World, screen: pygame.Surface):
    components = world.get_components(CTransform, CSurface)
    for _, (transform, surface) in components:
        screen.blit(surface.surf, transform.position)