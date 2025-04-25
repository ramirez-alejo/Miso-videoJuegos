import esper
import pygame
from src.create.i_sprite import create_sprite
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_player import CPlayer
from src.ecs.components.c_player_state import CPlayerState
from src.ecs.components.c_tag_player import CTagPlayer
from src.ecs.components.c_input_command import CInputCommand

def create_player(world: esper.World, player_config, position: pygame.Vector2, level_config=None) -> int:
    frames_number = player_config["animations"]["number_frames"]
    # Create a square entity for the player
    player_entity = create_sprite(
        entity=world.create_entity(),
        ecs_world=world,
        sprite_image=player_config["image"],
        position=position,
        velocity=pygame.Vector2(0, 0),  # Initial velocity is zero
        frames_number=frames_number
    )
    
    # Add player-specific components
    world.add_component(player_entity, CPlayer.from_dict(player_config, level_config))
    world.add_component(player_entity, CTagPlayer())
    world.add_component(player_entity, CAnimation.from_dict(player_config["animations"]))
    world.add_component(player_entity, CPlayerState())
    world.add_component(player_entity, CInputCommand())
    
    return player_entity
