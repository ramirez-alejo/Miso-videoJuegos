import esper
import pygame
from src.create.i_sprite import create_sprite
from src.ecs.components.c_bullet import CBullet
from src.ecs.components.c_tag_bullet import CTagBullet
from src.engine.service_locator import ServiceLocator

def create_bullet(world: esper.World, 
                  bullet_config, 
                  position: pygame.Vector2, 
                  target_position: pygame.Vector2,
                  image: str = None,
                  sound: str = None,
                  ) -> int:
    
    if image is None:
        image = bullet_config.get("image")
    if sound is None:
        sound = bullet_config.get("sound")


    direction = pygame.Vector2(target_position.x - position.x, target_position.y - position.y)
    
    if direction.length() > 0:
        direction = direction.normalize()
    
    bullet_velocity = bullet_config.get("velocity", 200)
    
    velocity = pygame.Vector2(
        direction.x * bullet_velocity,
        direction.y * bullet_velocity
    )
    
    ServiceLocator.sounds_service.play(sound)

    bullet_entity = create_sprite(
        entity=world.create_entity(),
        ecs_world=world,
        sprite_image=image,
        position=position,
        velocity=velocity
    )
    
    world.add_component(bullet_entity, CBullet(bullet_velocity))
    world.add_component(bullet_entity, CTagBullet())
    
    return bullet_entity
