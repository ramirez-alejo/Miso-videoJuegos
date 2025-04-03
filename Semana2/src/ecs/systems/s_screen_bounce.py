import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_tag_enemy import CTagEnemy

def system_screen_bounce(world: esper.World, screen: pygame.Surface):
    components = world.get_components(CTransform, CVelocity, CSurface, CTagEnemy)
    
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    
    for _, (transform, velocity, surface, _) in components:
        enemy_rect = pygame.Rect(
            transform.position.x,
            transform.position.y,
            surface.surf.get_width(),
            surface.surf.get_height()
        )

        if enemy_rect.left < 0:
            velocity.speed.x *= -1  # Reverse horizontal velocity
            transform.position.x = 0  # Place at boundary
        elif enemy_rect.right > screen_width:
            velocity.speed.x *= -1  # Reverse horizontal velocity
            transform.position.x = screen_width - surface.surf.get_width()  # Place at boundary
            
        if enemy_rect.top < 0:
            velocity.speed.y *= -1  # Reverse vertical velocity
            transform.position.y = 0  # Place at boundary
        elif enemy_rect.bottom > screen_height:
            velocity.speed.y *= -1  # Reverse vertical velocity
            transform.position.y = screen_height - surface.surf.get_height()  # Place at boundary
