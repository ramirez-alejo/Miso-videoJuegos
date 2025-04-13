import esper
from src.ecs.components.c_player_state import CPlayerState, PlayerState
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_velocity import CVelocity


def system_player_state(world: esper.World):
    player_components = world.get_components(CVelocity, CAnimation, CPlayerState)

    for _, (velocity, animation, player_state) in player_components:
        if player_state.state == PlayerState.IDLE:
            _do_idle_state(velocity, animation, player_state)
        elif player_state.state == PlayerState.MOVE:
            _do_move_state(velocity, animation, player_state)


def _do_idle_state(c_vel: CVelocity, c_a: CAnimation, c_pst: CPlayerState):
    _set_animation(c_a, 1)  # Set idle animation
    if c_vel.speed.magnitude_squared() > 0:
        c_pst.state = PlayerState.MOVE


def _do_move_state(c_vel: CVelocity, c_a: CAnimation, c_pst: CPlayerState):
    _set_animation(c_a, 0)  # Set move animation
    if c_vel.speed.magnitude_squared() <= 0:
        c_pst.state = PlayerState.IDLE


def _set_animation(c_a: CAnimation, num_anim: int):
    if c_a.current_animation == num_anim:
        return
    c_a.current_animation = num_anim
    c_a.curren_animation_time = 0
    c_a.current_frame = c_a.animation_list[num_anim].start
