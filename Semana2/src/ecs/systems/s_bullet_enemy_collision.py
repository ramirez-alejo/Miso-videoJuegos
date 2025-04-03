import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_tag_bullet import CTagBullet
from src.ecs.components.c_tag_enemy import CTagEnemy

def system_bullet_enemy_collision(world: esper.World):
    bullet_components = list(world.get_components(CTransform, CSurface, CTagBullet))
    
    enemy_components = list(world.get_components(CTransform, CSurface, CTagEnemy))
    
    entities_to_remove = set()
    
    for bullet_entity, (bullet_transform, bullet_surface, _) in bullet_components:
        bullet_rect = pygame.Rect(
            bullet_transform.position.x,
            bullet_transform.position.y,
            bullet_surface.surf.get_width(),
            bullet_surface.surf.get_height()
        )
        
        for enemy_entity, (enemy_transform, enemy_surface, _) in enemy_components:
            enemy_rect = pygame.Rect(
                enemy_transform.position.x,
                enemy_transform.position.y,
                enemy_surface.surf.get_width(),
                enemy_surface.surf.get_height()
            )
            
            if bullet_rect.colliderect(enemy_rect):
                entities_to_remove.add(bullet_entity)
                entities_to_remove.add(enemy_entity)
                print(f"Collision detected! Removing bullet {bullet_entity} and enemy {enemy_entity}")
                break
    
    for entity in entities_to_remove:
        world.delete_entity(entity, True)
