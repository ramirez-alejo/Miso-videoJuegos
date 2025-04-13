import esper
import pygame
from config_loader import get_player_config, get_level_config
from src.create.i_player import create_player
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_player import CPlayer

def system_create_player(world: esper.World, level_name="level_01"):
    player_config = get_player_config()
    level_config = get_level_config(level_name)
    
    player_spawn = level_config.get("player_spawn", {}).get("position", {"x": 100, "y": 100})
    spawn_position = pygame.Vector2(player_spawn["x"], player_spawn["y"])
    
    player_entity = create_player(
        world,
        player_config,
        spawn_position,
        level_config
    )
    
    components = world.get_components(CTransform, CSurface, CPlayer)[0]
    player_transform, player_surface, player = components[1]
    
    size = player_surface.area.size
    size = (size[0] / player.frames, size[1])
    relative_position = pygame.Vector2(player.spawn_position.x - size[0], player.spawn_position.y - size[1] / 2)
    
    player_transform.position.x = relative_position.x
    player_transform.position.y = relative_position.y
    
    return player_entity, level_config.get("player_spawn", {}).get("max_bullets", 4)