import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface

def system_screen_bounce(world: esper.World, screen: pygame.Surface):
    components = world.get_components(CTransform, CVelocity, CSurface)
    for _, (transform, velocity, surface) in components:
        cuad_rect = surface.get_rect(topLeft=transform.position)
        screen_rect = screen.get_rect()

        if transform.position.x < 0 or transform.position.x > screen.get_width() - surface.surf.get_width():
            velocity.speed.x *= -1
            cuad_rect.clamp_ip(screen_rect)
            transform.position.x = cuad_rect.x

            
        if transform.position.y < 0 or transform.position.y > screen.get_height() - surface.surf.get_height():
            velocity.speed.y *= -1
            cuad_rect.clamp_ip(screen_rect)
            transform.position.y = cuad_rect.y
            