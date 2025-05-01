import pygame
import esper
from src.ecs.components.c_text import CText
from src.engine.service_locator import ServiceLocator

def create_game_title(world: esper.World, screen_width: int, screen_height: int) -> int:

    ServiceLocator.fonts_service.get
    
    return world.create_entity(
        CText("EJERCICIO 04", pygame.Vector2(20, 30), 
              12, pygame.Color(255, 255, 255))
    )

def create_controls_text(world: esper.World, screen_width: int, screen_height: int) -> int:
    return world.create_entity(
        CText("Controles: Flechas, Disparo click normal, Disparo especial click derecho", 
              pygame.Vector2(20, 50), 
              8, 
              pygame.Color(255, 255, 0))
    )

def create_special_text(world: esper.World, screen_width: int, screen_height: int) -> int:
    
    return world.create_entity(
        CText("ESPECIAL", pygame.Vector2(20, screen_height - 40), 
              8, pygame.Color(255, 255, 255))
    )

def create_percentage_text(world: esper.World, screen_width: int, screen_height: int) -> int:
    
    return world.create_entity(
        CText("0%", pygame.Vector2(25, screen_height - 20), 
              8, pygame.Color(0, 255, 0))
    )

def create_pause_text(world: esper.World, screen_width: int, screen_height: int) -> int:
    
    return world.create_entity(
        CText("GAME PAUSED", pygame.Vector2(screen_width // 2, screen_height // 2), 
              16, pygame.Color(255, 0, 0), centered=True)
    )

def create_game_text(world: esper.World, screen_width: int, screen_height: int) -> None:
    create_game_title(world, screen_width, screen_height)
    create_controls_text(world, screen_width, screen_height)
    create_special_text(world, screen_width, screen_height)
    create_percentage_text(world, screen_width, screen_height)
