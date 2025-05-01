import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_tag_bullet import CTagBullet
from src.ecs.components.c_tag_enemy import CTagEnemy
from src.create.i_explosion import create_explosion

def system_bullet_enemy_collision(world: esper.World):
    bullet_components = list(world.get_components(CTransform, CSurface, CTagBullet))
    
    enemy_components = list(world.get_components(CTransform, CSurface, CTagEnemy))
    
    entities_to_remove = set()
    
    for bullet_entity, (bullet_transform, bullet_surface, _) in bullet_components:
        bullet_rect = bullet_surface.area.copy()
        bullet_rect.topleft = (bullet_transform.position.x, bullet_transform.position.y)
        
        for enemy_entity, (enemy_transform, enemy_surface, _) in enemy_components:
            enemy_rect = enemy_surface.area.copy()
            enemy_rect.topleft = (enemy_transform.position.x, enemy_transform.position.y)
            
            if bullet_rect.colliderect(enemy_rect):
                entities_to_remove.add(bullet_entity)
                entities_to_remove.add(enemy_entity)
                
                # Create explosion at collision point
                collision_pos = pygame.Vector2(
                    enemy_transform.position.x + enemy_rect.width / 2,
                    enemy_transform.position.y + enemy_rect.height / 2
                )
                create_explosion(world, collision_pos)
                
                print(f"Collision detected! Removing bullet {bullet_entity} and enemy {enemy_entity}")
                break
    
    for entity in entities_to_remove:
        world.delete_entity(entity, True)
