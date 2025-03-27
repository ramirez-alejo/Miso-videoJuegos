import pygame
import esper
import sys
import os

from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.systems.s_enemy_spawner import system_spawner

# Add the root directory to path to be able to import config_loader
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config_loader import get_window_config, get_enemies_config, get_level_config

from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce


class GameEngine:
    def __init__(self) -> None:
        pygame.init()
        
        # Load window configuration
        self.window_config = get_window_config()
        
        # Get screen size from config
        self.screen_width = self.window_config.get("size", {}).get("w", 640)
        self.screen_height = self.window_config.get("size", {}).get("h", 360)
        
        # Get background color from config
        bg_color = self.window_config.get("bg_color", {})
        self.bg_color = (
            bg_color.get("r", 0),
            bg_color.get("g", 0),
            bg_color.get("b", 0)
        )
        
        # Get framerate from config
        self.framerate = self.window_config.get("framerate", 60)
        
        # Create the screen with configured dimensions
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height), 
            pygame.SCALED
        )
        
        # Set the window title
        pygame.display.set_caption(self.window_config.get("title", "Game"))
        
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.delta_time = 0

        # Initialize ECS world
        self.ecs_world = esper.World()
        
        # Load enemy configurations
        self.enemies_config = get_enemies_config()
        
        # Load level configuration
        self.level_config = get_level_config("level_01")

        self.enemySpawner = None
        self.time = 0

       
    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):             
        self.enemySpawner = CEnemySpawner.from_dict(self.level_config, self.enemies_config)

    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0
        self.time += self.delta_time

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):

        system_spawner(self.ecs_world, self.enemySpawner, self.time)
        
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)

    def _draw(self):
        self.screen.fill(self.bg_color)
        system_rendering(self.ecs_world, self.screen)
        pygame.display.flip()

    def _clean(self):
        pygame.quit()
