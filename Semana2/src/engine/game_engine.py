import pygame
import esper
import sys
import os

from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.systems.s_enemy_spawner import system_spawner
from src.create.i_player import create_player
from src.ecs.systems.s_player_input import system_player_input
from src.ecs.systems.s_input_command import system_input_command
from src.ecs.systems.s_player_boundary import system_player_boundary
from src.ecs.systems.s_bullet_boundary import system_bullet_boundary
from src.ecs.systems.s_bullet_enemy_collision import system_bullet_enemy_collision
from src.ecs.systems.s_player_enemy_collision import system_player_enemy_collision

# Add the root directory to path to be able to import config_loader
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config_loader import get_window_config, get_enemies_config, get_level_config, get_player_config, get_bullet_config

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
        
        # Load player configuration
        self.player_config = get_player_config()
        
        # Load bullet configuration
        self.bullet_config = get_bullet_config()
        
        # Get max bullets from level config
        self.max_bullets = self.level_config.get("player_spawn", {}).get("max_bullets", 4)

        self.enemySpawner = None
        self.player_entity = None
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
        
        # Create player entity at the spawn position from level config
        player_spawn = self.level_config.get("player_spawn", {}).get("position", {"x": 100, "y": 100})
        self.player_entity = create_player(
            self.ecs_world,
            self.player_config,
            pygame.Vector2(player_spawn["x"], player_spawn["y"])
        )

    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0
        self.time += self.delta_time

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        # Process input commands
        system_input_command(self.ecs_world)
        
        # Process player input
        system_player_input(self.ecs_world, self.bullet_config, self.max_bullets)
        
        # Spawn enemies
        system_spawner(self.ecs_world, self.enemySpawner, self.time)
        
        # Update positions
        system_movement(self.ecs_world, self.delta_time)
        
        # Handle boundaries
        system_player_boundary(self.ecs_world, self.screen)
        system_bullet_boundary(self.ecs_world, self.screen)
        system_screen_bounce(self.ecs_world, self.screen)
        
        # Handle collisions
        system_bullet_enemy_collision(self.ecs_world)
        
        # Get player spawn position
        player_spawn = self.level_config.get("player_spawn", {}).get("position", {"x": 100, "y": 100})
        player_spawn_pos = pygame.Vector2(player_spawn["x"], player_spawn["y"])
        
        # Handle player-enemy collisions
        system_player_enemy_collision(self.ecs_world, player_spawn_pos)

    def _draw(self):
        self.screen.fill(self.bg_color)
        system_rendering(self.ecs_world, self.screen)
        pygame.display.flip()

    def _clean(self):
        pygame.quit()
