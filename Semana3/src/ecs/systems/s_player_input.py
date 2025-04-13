import pygame
import esper
from src.ecs.components.c_player import CPlayer
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_input_command import CInputCommand, PlayerAction
from src.ecs.components.c_tag_player import CTagPlayer
from src.create.i_bullet import create_bullet

def system_player_input(world: esper.World, bullet_config, max_bullets: int):
    components = world.get_components(CPlayer, CVelocity, CTransform, CSurface, CInputCommand, CTagPlayer)
    
    bullet_count = len(list(world.get_component(CTagBullet)))
    
    for _, (player, velocity, transform, surface, input_command, _) in components:
        velocity.speed.x = 0
        velocity.speed.y = 0
        
        if input_command.has_action(PlayerAction.PLAYER_LEFT):
            velocity.speed.x = -player.input_velocity
        if input_command.has_action(PlayerAction.PLAYER_RIGHT):
            velocity.speed.x = player.input_velocity
        if input_command.has_action(PlayerAction.PLAYER_UP):
            velocity.speed.y = -player.input_velocity
        if input_command.has_action(PlayerAction.PLAYER_DOWN):
            velocity.speed.y = player.input_velocity
        
        if input_command.has_action(PlayerAction.PLAYER_FIRE) and bullet_count < max_bullets:
            mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            
            player_current_rect = surface.area.copy()
            #bullet_size = surface.area.size
            player_center = pygame.Vector2(
                transform.position.x + (player_current_rect.width / 2),# - (bullet_size[0] / 2), 
                transform.position.y + (player_current_rect.height / 2) #- (bullet_size[1] / 2)
            )
            
            create_bullet(world, bullet_config, player_center, mouse_pos)

from src.ecs.components.c_tag_bullet import CTagBullet
