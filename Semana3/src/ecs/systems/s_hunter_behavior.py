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
    # Get player position
    player_components = list(world.get_components(CTransform, CTagPlayer))
    if not player_components:
        return  # No player found
    
    _, (player_transform, _) = player_components[0]
    player_position = pygame.Vector2(
        player_transform.position.x,
        player_transform.position.y
    )
    
    # Process all hunters
    hunter_components = world.get_components(CHunter, CTransform, CVelocity, CAnimation)
    for _, (hunter, transform, velocity, animation) in hunter_components:
        current_position = pygame.Vector2(transform.position.x, transform.position.y)
        
        # Calculate distances
        distance_to_player = current_position.distance_to(player_position)
        distance_to_origin = current_position.distance_to(hunter.origin_position)
        
        # Determine behavior based on distances
        if distance_to_origin > hunter.distance_start_return:
            # Return to origin behavior
            hunter.is_chasing = False
            hunter.is_returning = True
            
            # Calculate direction to origin
            direction = hunter.origin_position - current_position
            if direction.magnitude() > 0:
                direction = direction.normalize()
            
            # Set velocity towards origin
            velocity.speed = direction * hunter.velocity_return
            
            # Set animation to MOVE
            _set_animation(animation, 0)  # MOVE animation
            
        elif distance_to_player < hunter.distance_start_chase and not hunter.is_returning:
            # Chase player behavior
            hunter.is_chasing = True
            
            # Calculate direction to player
            direction = player_position - current_position
            if direction.magnitude() > 0:
                direction = direction.normalize()
            
            # Set velocity towards player
            velocity.speed = direction * hunter.velocity_chase
            
            # Set animation to MOVE
            _set_animation(animation, 0)  # MOVE animation
            
        elif hunter.is_returning and distance_to_origin < 5:
            # Reached origin, stop returning
            hunter.is_returning = False
            velocity.speed = pygame.Vector2(0, 0)
            
            # Set animation to IDLE
            _set_animation(animation, 1)  # IDLE animation
            
        elif not hunter.is_chasing and not hunter.is_returning:
            # Idle behavior
            velocity.speed = pygame.Vector2(0, 0)
            
            # Set animation to IDLE
            _set_animation(animation, 1)  # IDLE animation

def _set_animation(c_a: CAnimation, num_anim: int):
    if c_a.current_animation == num_anim:
        return
    c_a.current_animation = num_anim
    c_a.curren_animation_time = 0
    c_a.current_frame = c_a.animation_list[num_anim].start
