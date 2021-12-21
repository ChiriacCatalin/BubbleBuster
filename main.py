import pygame
import os
import numpy as np
import random

WIDTH, HEIGHT = 550, 720
GAME_WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BubbleBuster")

BALL_RADIUS = 25

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

THROW_BALL = (WIDTH/2, HEIGHT-BALL_RADIUS)

balls_center = []
balls_color = []
colors = [RED,PURPLE,CYAN,BLUE,YELLOW]

def intialize_data():
    generate_ball_positions()
    define_ball_colors()

def generate_ball_positions():
    row_len = [5,6,9,10,11,10,9,6,5]
    for i in range(len(row_len)):
        balls_row = [(None,None)] * row_len[i]
        x_indent = (max(row_len) - row_len[i] + 1) * BALL_RADIUS
        y_indent  = BALL_RADIUS - i* 7
        for j in range(row_len[i]):
            balls_row[j] = (x_indent + 2 * j * BALL_RADIUS, y_indent + 2 * i * BALL_RADIUS)
        balls_center.append(balls_row)

def define_ball_colors():
    row_len = [5,6,9,10,11,10,9,6,5]
    for i in range(len(row_len)):
        balls_row_color = [(None,None)] * row_len[i]
        for j in range(row_len[i]):
            balls_row_color[j] = random.choice(colors)
        balls_color.append(balls_row_color)

def draw_map_balls():
    for i in range(len(balls_center)):
        for j in range(len(balls_center[i])):
            pygame.draw.circle(GAME_WINDOW, balls_color[i][j], balls_center[i][j], BALL_RADIUS)


def draw_window():
    GAME_WINDOW.fill(WHITE)
    draw_map_balls()
    pygame.draw.circle(GAME_WINDOW, RED,THROW_BALL, BALL_RADIUS)
    pygame.display.update()

def main():
    intialize_data()
    game_running = True
    while game_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
        draw_window()



if __name__ == "__main__":
    main()