"""
Class that contain the core of the
game engine. This class is responsible
to manage the lifecycle of the game (load -> run).
"""
import pygame

from simian.canvas import GameCanvas
from simian.utils.singleton import Singleton
from simian.scene.scene_manager import SceneManager
from simian.input.keyboard_manager import Keyboard
# from simian.config import Configuration


NUMBER_OF_FRAMES = 60


class GameEngine(metaclass=Singleton):
    """
    Class that wraps the mainloop
    of the game.
    """
    def load(self, game_name, window_size):
        """
        Initialize the main canvas, the screen_manager
        and the keyboard.
        """
        self.game_canvas = GameCanvas(game_name, window_size)
        self.scene_manager = SceneManager()
        self.keyboard = Keyboard()
        # self.configuration = Configuration()

    def add_scene(self, *args):
        """
        Add one or many scenes to scene manager.
        """
        self.scene_manager.add_scene(args)

    def set_initial_scene(self, scene_name):
        """
        Set the first scene to be loaded on the engine.
        """
        self.scene_manager.load_scene(scene_name)

    def set_next_scene(self, scene_name):
        """
        Set the next scene to be loaded on the engine.
        """
        self.scene_manager.set_next_scene(scene_name)

    def run(self):
        """
        Initialize pygame, open window and start
        game loop.
        """
        pygame.init()

        clock = pygame.time.Clock()
        self.game_canvas.open()
        self.screen = self.game_canvas.get_screen()

        pygame.key.set_repeat(True)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.scene_manager.update(clock.get_time()/1000)
            groups = pygame.sprite.OrderedUpdates()
            self.scene_manager.draw(groups)
            groups.draw(self.screen)

            # Refresh screen
            self.game_canvas.refresh()

            # Set the number of frames per second
            clock.tick(NUMBER_OF_FRAMES)
