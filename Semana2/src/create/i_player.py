import esper
import pygame
from src.create.i_square import create_square
from src.ecs.components.c_player import CPlayer
from src.ecs.components.c_tag_player import CTagPlayer
from src.ecs.components.c_input_command import CInputCommand

def create_player(world: esper.World, player_config, position: pygame.Vector2) -> int:
    # Create a square entity for the player
    player_entity = create_square(
        entity=world.create_entity(),
        ecs_world=world,
        size=pygame.Vector2(player_config["size"]["x"], player_config["size"]["y"]),
        color=pygame.Color(player_config["color"]["r"], player_config["color"]["g"], player_config["color"]["b"]),
        position=position,
        velocity=pygame.Vector2(0, 0)  # Initial velocity is zero
    )
    
    # Add player-specific components
    world.add_component(player_entity, CPlayer(player_config["input_velocity"]))
    world.add_component(player_entity, CTagPlayer())
    world.add_component(player_entity, CInputCommand())
    
    return player_entity
