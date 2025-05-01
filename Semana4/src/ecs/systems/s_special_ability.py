import esper
import pygame
import math
from src.ecs.components.c_player import CPlayer
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_input_command import CInputCommand, PlayerAction
from src.ecs.components.c_special_ability import CSpecialAbility
from src.ecs.components.c_text import CText
from src.create.i_bullet import create_bullet
from src.engine.service_locator import ServiceLocator

def system_special_ability(world: esper.World, delta_time: float, bullet_config):
    components = world.get_components(CPlayer, CTransform, CSurface, CInputCommand, CSpecialAbility)
    
    percentage_text_entities = []
    for entity, text_comp in world.get_component(CText):
        if text_comp.text.endswith("%"):
            percentage_text_entities.append((entity, text_comp))
    
    for _, (player, transform, surface, input_command, special_ability) in components:
        if not special_ability.ready:
            special_ability.current_cooldown -= delta_time
            
            percentage = int((1 - (special_ability.current_cooldown / special_ability.cooldown_time)) * 100)
            
            for entity, text_comp in percentage_text_entities:
                text_comp.text = f"{percentage}%"
                text_comp.dirty = True
            
            if special_ability.current_cooldown <= 0:
                special_ability.ready = True
                special_ability.current_cooldown = 0
                
                for entity, text_comp in percentage_text_entities:
                    text_comp.text = "100%"
                    text_comp.dirty = True
        
        if special_ability.ready and input_command.has_action(PlayerAction.PLAYER_SPECIAL):
            player_center = pygame.Vector2(
                transform.position.x + (surface.area.width / 2),
                transform.position.y + (surface.area.height / 2)
            )
            
            for angle in range(15, 375, 30):
                radians = math.radians(angle)
                target_x = player_center.x + 100 * math.cos(radians)
                target_y = player_center.y + 100 * math.sin(radians)
                target_pos = pygame.Vector2(target_x, target_y)
                
                create_bullet(world, bullet_config, player_center, target_pos,
                              'assets/img/bullet_especial.png',
                              'assets/snd/laser_special.ogg')
            
            ServiceLocator.sounds_service.play("assets/snd/laser_special.ogg")
            
            special_ability.ready = False
            special_ability.current_cooldown = special_ability.cooldown_time
            
            for entity, text_comp in percentage_text_entities:
                text_comp.text = "0%"
                text_comp.dirty = True
