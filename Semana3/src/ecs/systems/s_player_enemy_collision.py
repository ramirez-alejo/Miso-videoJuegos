import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_tag_player import CTagPlayer
from src.ecs.components.c_tag_enemy import CTagEnemy

def system_player_enemy_collision(world: esper.World, player_spawn_position: pygame.Vector2):
    player_components = list(world.get_components(CTransform, CSurface, CTagPlayer))
    
    enemy_components = list(world.get_components(CTransform, CSurface, CTagEnemy))
    
    enemies_to_remove = set()
    
    for _, (player_transform, player_surface, _) in player_components:

        player_rect = player_surface.area.copy()
        player_rect.topleft = (player_transform.position.x, player_transform.position.y)
        
        for enemy_entity, (enemy_transform, enemy_surface, _) in enemy_components:

            enemy_rect = enemy_surface.area.copy()
            enemy_rect.topleft = (enemy_transform.position.x, enemy_transform.position.y)
            
            if player_rect.colliderect(enemy_rect):
                enemies_to_remove.add(enemy_entity)
                
                player_transform.position.x = player_spawn_position.x
                player_transform.position.y = player_spawn_position.y
                
                print(f"Player collision! Removing enemy {enemy_entity} and resetting player position")
                break
    
    for entity in enemies_to_remove:
        world.delete_entity(entity, True)
