
import esper

from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_surface import CSurface


def system_animation(world: esper.World, delta_time: float) -> None:
    components = world.get_components(CAnimation, CSurface)
    for _, (animation, surface) in components:
        animation.curren_animation_time -= delta_time
        if animation.curren_animation_time <= 0:
            animation.curren_animation_time = animation.animation_list[animation.current_animation].frame_rate
            animation.current_frame += 1
            if animation.current_frame > animation.animation_list[animation.current_animation].end:
                animation.current_frame = animation.animation_list[animation.current_animation].start
            surface_rect = surface.surf.get_rect()
            surface.area.width = surface_rect.width / animation.number_frames
            surface.area.x = animation.current_frame * surface.area.width