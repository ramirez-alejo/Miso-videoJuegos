import esper
import pygame
import math
from src.ecs.components.c_hunter import CHunter
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_tag_player import CTagPlayer
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_player_state import PlayerState

def system_hunter_behavior(world: esper.World):
    player_components = list(world.get_components(CTransform, CTagPlayer))
    if not player_components:
        return
    
    _, (player_transform, _) = player_components[0]
    player_position = pygame.Vector2(
        player_transform.position.x,
        player_transform.position.y
    )
    
    hunter_components = world.get_components(CHunter, CTransform, CVelocity, CAnimation)
    for _, (hunter, transform, velocity, animation) in hunter_components:
        current_position = pygame.Vector2(transform.position.x, transform.position.y)
        
        distance_to_player = current_position.distance_to(player_position)
        distance_to_origin = current_position.distance_to(hunter.origin_position)
        
        if distance_to_origin > hunter.distance_start_return:
            hunter.is_chasing = False
            hunter.is_returning = True
            
            direction = hunter.origin_position - current_position
            if direction.magnitude() > 0:
                direction = direction.normalize()
            
            velocity.speed = direction * hunter.velocity_return
            
            _set_animation(animation, 0)
            
        elif distance_to_player < hunter.distance_start_chase and not hunter.is_returning:
            hunter.is_chasing = True
            
            direction = player_position - current_position
            if direction.magnitude() > 0:
                direction = direction.normalize()
            
            velocity.speed = direction * hunter.velocity_chase
            
            _set_animation(animation, 0)
            
        elif hunter.is_returning and distance_to_origin < 5:
            hunter.is_returning = False
            velocity.speed = pygame.Vector2(0, 0)
            
            _set_animation(animation, 1)
            
        elif not hunter.is_chasing and not hunter.is_returning:
            velocity.speed = pygame.Vector2(0, 0)
            
            _set_animation(animation, 1)

def _set_animation(c_a: CAnimation, num_anim: int):
    if c_a.current_animation == num_anim:
        return
    c_a.current_animation = num_anim
    c_a.curren_animation_time = 0
    c_a.current_frame = c_a.animation_list[num_anim].start
