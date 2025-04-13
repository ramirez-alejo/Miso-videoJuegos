import esper
import pygame
from src.create.i_sprite import create_sprite
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_explosion import CExplosion
from src.ecs.components.c_surface import CSurface
from config_loader import get_explosion_config

def create_explosion(world: esper.World, position: pygame.Vector2) -> int:
    # Load explosion configuration
    explosion_config = get_explosion_config()
    
    # Calculate animation duration based on framerate and number of frames
    animation_data = explosion_config["animations"]["list"][0]
    frames = animation_data["end"] - animation_data["start"] + 1
    frame_duration = 1.0 / animation_data["framerate"]
    total_duration = frames * frame_duration
    
    # Create entity
    explosion_entity = world.create_entity()
    
    # Load the explosion image
    frames_number = explosion_config["animations"]["number_frames"]
    sprite = pygame.image.load(explosion_config["image"]).convert_alpha()
    
    # Calculate frame dimensions
    sprite_width = sprite.get_width()
    sprite_height = sprite.get_height()
    frame_width = sprite_width / frames_number
    
    # Center the explosion at the given position
    centered_position = pygame.Vector2(
        position.x - frame_width / 2,
        position.y - sprite_height / 2
    )
    
    # Add components
    world.add_component(explosion_entity, CSurface.from_surface(sprite))
    world.add_component(explosion_entity, CExplosion(total_duration))
    world.add_component(explosion_entity, CAnimation.from_dict(explosion_config["animations"]))
    
    # Set up the transform and velocity components
    from src.ecs.components.c_transform import CTransform
    from src.ecs.components.c_velocity import CVelocity
    world.add_component(explosion_entity, CTransform(centered_position))
    world.add_component(explosion_entity, CVelocity(pygame.Vector2(0, 0)))
    
    # Initialize the animation area
    surface = world.component_for_entity(explosion_entity, CSurface)
    animation = world.component_for_entity(explosion_entity, CAnimation)
    
    # Set the initial frame area
    surface.area.width = frame_width
    surface.area.height = sprite_height
    surface.area.x = animation.current_frame * frame_width
    surface.area.y = 0
    
    return explosion_entity
