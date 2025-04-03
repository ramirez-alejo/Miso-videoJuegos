from enum import Enum, auto

class PlayerAction(Enum):
    PLAYER_LEFT = auto()
    PLAYER_RIGHT = auto()
    PLAYER_UP = auto()
    PLAYER_DOWN = auto()
    PLAYER_FIRE = auto()

class CInputCommand:
    def __init__(self) -> None:
        self.actions = set()
    
    def add_action(self, action: PlayerAction) -> None:
        self.actions.add(action)
    
    def remove_action(self, action: PlayerAction) -> None:
        if action in self.actions:
            self.actions.remove(action)
    
    def clear_actions(self) -> None:
        self.actions.clear()
    
    def has_action(self, action: PlayerAction) -> bool:
        return action in self.actions
