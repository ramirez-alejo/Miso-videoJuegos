import pygame

class CSurface:
    def __init__(self, size: pygame.Vector2, color: pygame.Color) -> None:
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
    
    def get_rect(self, topLeft: pygame.Vector2) -> pygame.Rect:
        return self.surf.get_rect(topleft=topLeft)