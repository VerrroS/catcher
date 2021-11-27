import pygame


class Settings:
    """
    a class to represent the settings of the game

    """
    def __init__(self):
        self.fg_color = (0, 0, 0)
        self.bg_color = (255, 255, 255)
        self.hl_color = (0, 255, 0)
        self.screen_width = 640
        self.screen_height = 480
        self.top_left_corner = (0, 0)
        self.buffer = 15
        self.fps = 30
        self.caption = 'Catcher'
        self.ball_speed = 5
        self.player_speed = 10
        self.font_size = 30
        self.player_size = (50, 30)
        self.ball_size = (20, 20)


class Game(Settings):
    """
    a class to initialize the game's display

    """
    def __init__(self):
        Settings.__init__(self)
        self.font = pygame.font.SysFont('arial', self.font_size)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.background = pygame.Surface((self.screen_width, self.screen_height))
        self.background.fill(self.bg_color)
        pygame.display.set_caption(self.caption)
