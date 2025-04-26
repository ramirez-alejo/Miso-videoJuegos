import pygame
from enum import Enum, auto

class HunterState(Enum):
    IDLE = auto()
    PATROLLING = auto()  # New state for patrolling
    CHASING = auto()
    RETURNING = auto()

class CHunter:
    def __init__(self, distance_start_chase: float, 
                 distance_start_return: float,
                 velocity_chase: float,
                 velocity_return: float,
                 origin_position: pygame.Vector2,
                 sound: str = "",
                 velocity_patrol: float = 1,
                 patrol_type: str = '',
                 patrol_distance: float = 0,
                 ):
        self.distance_start_chase = distance_start_chase
        self.distance_start_return = distance_start_return
        self.velocity_chase = velocity_chase
        self.velocity_return = velocity_return
        self.velocity_patrol = velocity_patrol
        self.patrol_type = patrol_type
        self.patrol_distance = patrol_distance
        self.origin_position = origin_position
        self.chase_start_position = None
        self.patrol_direction = 1
        self.state = HunterState.PATROLLING
        self.is_chasing = False
        self.is_returning = False
        self.sound = sound