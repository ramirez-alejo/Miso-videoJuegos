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
            elif hunter.state == HunterState.CHASING:
                self._handle_chase_state(hunter, current_position, velocity, animation)
            elif hunter.state == HunterState.RETURNING:
                self._handle_return_state(hunter, current_position, velocity, animation)
            
            hunter.is_chasing = (hunter.state == HunterState.CHASING)
            hunter.is_returning = (hunter.state == HunterState.RETURNING)
    
    def _update_state(self, hunter: CHunter, current_position: pygame.Vector2):
        distance_to_player = current_position.distance_to(self.player_position)
        distance_to_origin = current_position.distance_to(hunter.origin_position)
        
        if hunter.state != HunterState.RETURNING and distance_to_origin > hunter.distance_start_return:
            hunter.state = HunterState.RETURNING
        elif hunter.state == HunterState.IDLE and distance_to_player < hunter.distance_start_chase:
            ServiceLocator.sounds_service.play(hunter.sound)
            hunter.state = HunterState.CHASING
        elif hunter.state == HunterState.RETURNING and distance_to_origin < 5:
            hunter.state = HunterState.IDLE
    
    def _handle_idle_state(self, hunter: CHunter, velocity: CVelocity, animation: CAnimation):
        velocity.speed = pygame.Vector2(0, 0)
        self._set_animation(animation, 1)
    
    def _handle_chase_state(self, hunter: CHunter, current_position: pygame.Vector2, 
                           velocity: CVelocity, animation: CAnimation):
        direction = self.player_position - current_position
        if direction.magnitude() > 0:
            direction = direction.normalize()
        
        velocity.speed = direction * hunter.velocity_chase
        self._set_animation(animation, 0)
    
    def _handle_return_state(self, hunter: CHunter, current_position: pygame.Vector2, 
                            velocity: CVelocity, animation: CAnimation):
        direction = hunter.origin_position - current_position
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
