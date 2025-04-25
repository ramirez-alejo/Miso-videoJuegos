import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_tag_enemy import CTagEnemy
from src.ecs.components.c_hunter import CHunter

def system_screen_bounce(world: esper.World, screen: pygame.Surface):
    components = world.get_components(CTransform, CVelocity, CSurface, CTagEnemy)
    
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    
    for entity, (transform, velocity, surface, _) in components:
        # Skip stationary hunters at their origin positions
        if world.has_component(entity, CHunter):
            hunter = world.component_for_entity(entity, CHunter)
            if not hunter.is_chasing and not hunter.is_returning:
                continue
        
        # Use the existing area property instead of creating a new rectangle
        # Just create a copy and update its position to match the current transform
        enemy_rect = surface.area.copy()
        enemy_rect.topleft = (transform.position.x, transform.position.y)

        if enemy_rect.left < 0:
            velocity.speed.x *= -1
            transform.position.x = 0
        elif enemy_rect.right > screen_width:
            velocity.speed.x *= -1
            transform.position.x = screen_width - enemy_rect.width 
            
        if enemy_rect.top < 0:
            velocity.speed.y *= -1 
            transform.position.y = 0 
        elif enemy_rect.bottom > screen_height:
            velocity.speed.y *= -1 
            transform.position.y = screen_height - enemy_rect.height
