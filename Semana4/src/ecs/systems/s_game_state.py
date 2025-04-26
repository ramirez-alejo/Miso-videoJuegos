import esper
import pygame
from src.ecs.components.c_game_state import CGameState, GameState
from src.ecs.components.c_input_command import CInputCommand, PlayerAction
from src.ecs.components.c_text import CText
from src.ecs.components.c_tag_player import CTagPlayer
from src.engine.service_locator import ServiceLocator
from src.create.i_text import create_pause_text

def system_game_state(world: esper.World, screen_width: int, screen_height: int):
    game_state_components = world.get_component(CGameState)
    
    if len(list(game_state_components)) == 0:
        world.create_entity(CGameState())
        return
    
    input_components = world.get_components(CInputCommand, CTagPlayer)
    
    for game_state_entity, game_state in game_state_components:
        for _, (input_command, _) in input_components:
            if input_command.has_action(PlayerAction.PLAYER_PAUSE):
                if game_state.state == GameState.RUNNING:
                    _enter_paused_state(world, game_state, screen_width, screen_height)
                else:
                    _enter_running_state(world, game_state)

    


def _enter_paused_state(world: esper.World, game_state: CGameState, screen_width: int, screen_height: int):
    game_state.state = GameState.PAUSED
    
    if game_state.pause_text_entity is None:
        game_state.pause_text_entity = create_pause_text(world, screen_width, screen_height)
    
    pause_text_comp = world.component_for_entity(game_state.pause_text_entity, CText)
    if pause_text_comp is not None:
        pause_text_comp.dirty = True
        pause_text_comp.hidden = False
        pause_text_comp.text = "GAME PAUSED"
    


def _enter_running_state(world: esper.World, game_state: CGameState):
    game_state.state = GameState.RUNNING
    
    if game_state.pause_text_entity is not None:
        pause_text_comp = world.component_for_entity(game_state.pause_text_entity, CText)
        if pause_text_comp is not None:
            pause_text_comp.dirty = True
            pause_text_comp.hidden = True


