
class AnimationData:
    def __init__(self, name: str, start: int, end: int, frame_rate: float) -> None:
        self.name = name
        self.start = start
        self.end = end
        self.frame_rate = frame_rate/frame_rate


class CAnimation:
    def __init__(self, number_frames: int, animation_list: list[AnimationData]) -> None:
        self.number_frames = number_frames
        self.animation_list = animation_list
        self.current_animation = 0
        self.curren_animation_time = 0
        self.current_frame = self.animation_list[self.current_animation].start

    @classmethod
    def from_dict(cls, animation_config: dict) -> 'CAnimation':
        number_frames = animation_config.get("number_frames", 1)
        animation_data = [
            AnimationData(
                name=anim["name"],
                start=anim["start"],
                end=anim["end"],
                frame_rate=anim["framerate"]
            )
            for anim in animation_config.get("list", [])
        ]
        return cls(number_frames, animation_data)