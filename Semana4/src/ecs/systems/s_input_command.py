import esper
import pygame
from src.ecs.components.c_input_command import CInputCommand, PlayerAction
from src.ecs.components.c_tag_player import CTagPlayer

def system_input_command(world: esper.World):
    components = world.get_components(CInputCommand, CTagPlayer)
    
    keys = pygame.key.get_pressed()
    
    mouse_buttons = pygame.mouse.get_pressed()
    
    static_vars = getattr(system_input_command, "static_vars", {"last_mouse_state": False})
    current_mouse_state = mouse_buttons[0]  # Left mouse button
    mouse_just_pressed = current_mouse_state and not static_vars["last_mouse_state"]
    static_vars["last_mouse_state"] = current_mouse_state
    system_input_command.static_vars = static_vars
    
    for _, (input_command, _) in components:
        input_command.clear_actions()
        
        if keys[pygame.K_LEFT]:
            input_command.add_action(PlayerAction.PLAYER_LEFT)
        if keys[pygame.K_RIGHT]:
            input_command.add_action(PlayerAction.PLAYER_RIGHT)
        if keys[pygame.K_UP]:
            input_command.add_action(PlayerAction.PLAYER_UP)
        if keys[pygame.K_DOWN]:
            input_command.add_action(PlayerAction.PLAYER_DOWN)
        
        if mouse_just_pressed:
            input_command.add_action(PlayerAction.PLAYER_FIRE)
