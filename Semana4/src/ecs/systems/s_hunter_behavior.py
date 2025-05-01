import esper
import pygame
from enum import Enum
from src.ecs.components.c_hunter import CHunter, HunterState
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_tag_player import CTagPlayer
from src.ecs.components.c_animation import CAnimation
from src.engine.service_locator import ServiceLocator

class HunterBehaviorSystem:
    def __init__(self):
        self.player_position = None
    
    def process(self, world: esper.World):
        player_components = list(world.get_components(CTransform, CTagPlayer))
        if not player_components:
            return
        
        _, (player_transform, _) = player_components[0]
        self.player_position = pygame.Vector2(
            player_transform.position.x,
            player_transform.position.y
        )
        
        hunter_components = world.get_components(CHunter, CTransform, CVelocity, CAnimation)
        for _, (hunter, transform, velocity, animation) in hunter_components:
            current_position = pygame.Vector2(transform.position.x, transform.position.y)
            
            self._update_state(hunter, current_position)
            
            if hunter.state == HunterState.IDLE:
                self._handle_idle_state(hunter, velocity, animation)
            elif hunter.state == HunterState.PATROLLING:
                self._handle_patrol_state(hunter, current_position, velocity, animation)
            elif hunter.state == HunterState.CHASING:
                self._handle_chase_state(hunter, current_position, velocity, animation)
            elif hunter.state == HunterState.RETURNING:
                self._handle_return_state(hunter, current_position, velocity, animation)
            
            hunter.is_chasing = (hunter.state == HunterState.CHASING)
            hunter.is_returning = (hunter.state == HunterState.RETURNING)
    
    def _update_state(self, hunter: CHunter, current_position: pygame.Vector2):
        distance_to_player = current_position.distance_to(self.player_position)
        
        if hunter.state == HunterState.PATROLLING or hunter.state == HunterState.IDLE:
            if distance_to_player < hunter.distance_start_chase:
                ServiceLocator.sounds_service.play(hunter.sound)
                hunter.state = HunterState.CHASING
                hunter.chase_start_position = pygame.Vector2(current_position)
        
        elif hunter.state == HunterState.CHASING:
            if distance_to_player > hunter.distance_start_return:
                hunter.state = HunterState.RETURNING
        
        elif hunter.state == HunterState.RETURNING:
            distance_to_chase_start = current_position.distance_to(hunter.chase_start_position)
            if distance_to_chase_start < 5:
                hunter.state = HunterState.PATROLLING
    
    def _handle_idle_state(self, hunter: CHunter, velocity: CVelocity, animation: CAnimation):
        velocity.speed = pygame.Vector2(0, 0)
        self._set_animation(animation, 1)
    
    def _handle_patrol_state(self, hunter: CHunter, current_position: pygame.Vector2, 
                            velocity: CVelocity, animation: CAnimation):
        patrol_direction = pygame.Vector2(0, 0)
        
        if hunter.patrol_type == "horizontal":
            if current_position.x >= hunter.origin_position.x + hunter.patrol_distance:
                hunter.patrol_direction = -1
            elif current_position.x <= hunter.origin_position.x - hunter.patrol_distance:
                hunter.patrol_direction = 1
                
            patrol_direction.x = hunter.patrol_direction
            
        elif hunter.patrol_type == "vertical":
            if current_position.y >= hunter.origin_position.y + hunter.patrol_distance:
                hunter.patrol_direction = -1
            elif current_position.y <= hunter.origin_position.y - hunter.patrol_distance:
                hunter.patrol_direction = 1
                
            patrol_direction.y = hunter.patrol_direction
        
        velocity.speed = patrol_direction * hunter.velocity_patrol
        self._set_animation(animation, 0)
    
    def _handle_chase_state(self, hunter: CHunter, current_position: pygame.Vector2, 
                           velocity: CVelocity, animation: CAnimation):
        
        if current_position.distance_to(hunter.chase_start_position) > hunter.distance_start_return:
            hunter.state = HunterState.RETURNING
            return

        direction = self.player_position - current_position
        if direction.magnitude() > 0:
            direction = direction.normalize()
        
        velocity.speed = direction * hunter.velocity_chase
        self._set_animation(animation, 0)
    
    def _handle_return_state(self, hunter: CHunter, current_position: pygame.Vector2, 
                            velocity: CVelocity, animation: CAnimation):
        direction = hunter.chase_start_position - current_position
        if direction.magnitude() > 0:
            direction = direction.normalize()
        
        velocity.speed = direction * hunter.velocity_return
        self._set_animation(animation, 0)
    
    def _set_animation(self, c_a: CAnimation, num_anim: int):
        if c_a.current_animation == num_anim:
            return
        c_a.current_animation = num_anim
        c_a.curren_animation_time = 0
        c_a.current_frame = c_a.animation_list[num_anim].start

def system_hunter_behavior(world: esper.World):
    hunter_system = HunterBehaviorSystem()
    hunter_system.process(world)