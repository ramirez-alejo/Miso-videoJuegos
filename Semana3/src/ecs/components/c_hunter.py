import pygame

class CHunter:
    def __init__(self, origin_position: pygame.Vector2, 
                 distance_start_chase: float, 
                 distance_start_return: float,
                 velocity_chase: float,
                 velocity_return: float) -> None:
        self.origin_position = origin_position.copy()
        self.distance_start_chase = distance_start_chase
        self.distance_start_return = distance_start_return
        self.velocity_chase = velocity_chase
        self.velocity_return = velocity_return
        self.is_chasing = False
        self.is_returning = False
