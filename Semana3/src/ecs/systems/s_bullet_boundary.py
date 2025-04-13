import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_tag_bullet import CTagBullet

def system_bullet_boundary(world: esper.World, screen: pygame.Surface):
    """Remove bullets that hit the screen boundaries"""
    components = world.get_components(CTransform, CSurface, CTagBullet)
    
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    
    entities_to_remove = []
    
    for entity, (transform, surface, _) in components:
        bullet_rect = pygame.Rect(
            transform.position.x,
            transform.position.y,
            surface.area.width,
            surface.area.height
        )
        
        if (bullet_rect.left < 0 or 
            bullet_rect.right > screen_width or
            bullet_rect.top < 0 or 
            bullet_rect.bottom > screen_height):
            entities_to_remove.append(entity)
            print(f"Bullet {entity} hit boundary and was removed")
            break
    
    for entity in entities_to_remove:
        world.delete_entity(entity, True)
