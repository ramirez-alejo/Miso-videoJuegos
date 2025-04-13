import pygame

class CSurface:
    def __init__(self, size: pygame.Vector2, color: pygame.Color) -> None:
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.area = self.surf.get_rect()


    @classmethod
    def from_surface(cls, surface: pygame.Surface) -> 'CSurface':
        instance = cls(pygame.Vector2(0,0), pygame.Color(0, 0, 0))
        instance.surf = surface
        instance.area = surface.get_rect()
        return instance