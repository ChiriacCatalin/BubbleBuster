import pygame
import os
import numpy as np

WIDTH, HEIGHT = 520, 720
GAME_WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BubbleBuster")

BALL_RADIUS = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

balls_center = []

def intialize_data():
    generate_ball_positions()

def generate_ball_positions():
    for i in range(8):
        balls_row = [(None,None)] * 13
        for j in range(13):
            balls_row[j] = (20 + 2 * j * BALL_RADIUS, 20 + 2 * i * BALL_RADIUS)
        balls_center.append(balls_row)

def draw_balls():
    for i in range(len(balls_center)):
        for j in range(len(balls_center[i])):
            pygame.draw.circle(GAME_WINDOW, RED,balls_center[i][j], BALL_RADIUS)


def draw_window():
    GAME_WINDOW.fill(BLACK)
    draw_balls()
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