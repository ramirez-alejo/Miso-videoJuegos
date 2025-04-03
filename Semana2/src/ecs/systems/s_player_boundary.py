import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_tag_player import CTagPlayer

def system_player_boundary(world: esper.World, screen: pygame.Surface):
    components = world.get_components(CTransform, CSurface, CTagPlayer)
    
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    
    for _, (transform, surface, _) in components:
        player_rect = pygame.Rect(
            transform.position.x,
            transform.position.y,
            surface.surf.get_width(),
            surface.surf.get_height()
        )
        
        if player_rect.left < 0:
            transform.position.x = 0
        elif player_rect.right > screen_width:
            transform.position.x = screen_width - surface.surf.get_width()
            
        if player_rect.top < 0:
            transform.position.y = 0
        elif player_rect.bottom > screen_height:
            transform.position.y = screen_height - surface.surf.get_height()
