"""
This module has most of the global variables and constants, like color
and screen size
"""

import pygame
import os
pygame.font.init()


WIDTH, HEIGHT = 550, 720
SETTINGS_SPACE = 50

GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BubbleBuster")
background_image = pygame.image.load(os.path.join('Assets', 'background.jpg'))

SCORE_FONT = pygame.font.SysFont('comicsans', 30)
score = [0]

RESULT_FONT = pygame.font.SysFont('comicsans', 80)
result_text = [""]


BALL_RADIUS = 25
GRAY = (100, 100, 100)
LIGHT_GRAY = (175, 175, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
GREEN = (50, 190, 40)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
colors = [RED, PURPLE, CYAN, BLUE, YELLOW]

BALL_VELOCITY = 10
THROW_BALL = (WIDTH/2, HEIGHT-BALL_RADIUS)

balls_center = []
available_colors = set()
