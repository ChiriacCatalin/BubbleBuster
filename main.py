import pygame
import os
import numpy as np
import random
import math 

WIDTH, HEIGHT = 550, 720
GAME_WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BubbleBuster")

BALL_RADIUS = 25
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

BALL_VELOCIY = 10
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
            pygame.draw.circle(GAME_WINDOW, GRAY, balls_center[i][j], BALL_RADIUS,width=1)


def draw_window(throwing_bubble_rect):
    GAME_WINDOW.fill(WHITE)
    #draw_map_balls()
    pygame.draw.circle(GAME_WINDOW, RED,(throwing_bubble_rect.x + BALL_RADIUS, throwing_bubble_rect.y+BALL_RADIUS), BALL_RADIUS)
    pygame.draw.circle(GAME_WINDOW, GRAY,(throwing_bubble_rect.x + BALL_RADIUS, throwing_bubble_rect.y+BALL_RADIUS), BALL_RADIUS,width=1)
    pygame.display.update()

def ball_angle(p1, p2):
    xDiff = p2[0] - p1[0]
    yDiff = p2[1] - p1[1]
    return -math.degrees(math.atan2(yDiff, xDiff))

def next_ball_position(init_pos, angle):
    new_x = init_pos[0] + BALL_VELOCIY * math.cos(math.radians(angle))
    new_y = init_pos[1] - BALL_VELOCIY * math.sin(math.radians(angle))
    return (new_x, new_y)



def throw_the_bubble(pos, throwing_bubble_rect, angle, exact_position):
    (exact_position[0], exact_position[1]) = next_ball_position(exact_position, angle)
    (throwing_bubble_rect.x, throwing_bubble_rect.y) = (int(exact_position[0]),int(exact_position[1])) # update the positon of the ball

    # change angle on collision with the right or left margin
    if throwing_bubble_rect.x + 2 * BALL_RADIUS >= WIDTH or throwing_bubble_rect.x <=0:
        angle = 180 - angle
    if throwing_bubble_rect.y < 0:
        throwing_bubble_rect.x = WIDTH/2-BALL_RADIUS
        throwing_bubble_rect.y = HEIGHT-2*BALL_RADIUS
        return -1
    return angle


def main():
    intialize_data()
    clock = pygame.time.Clock()

    throwing_bubble_rect = pygame.Rect(WIDTH/2-BALL_RADIUS, HEIGHT-2*BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)
    game_running = True
    pos = (None,None)
    angle = -1
    while game_running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and angle < 0:
                pos = pygame.mouse.get_pos()
                angle = ball_angle(THROW_BALL,pos) # get the angle between the center of the bubble and the clicked area
                exact_position = [throwing_bubble_rect.x, throwing_bubble_rect.y] # the float value of the position
            
        if angle > 0:# throw the ball
            angle = throw_the_bubble(pos, throwing_bubble_rect, angle, exact_position)
            
        draw_window(throwing_bubble_rect)



if __name__ == "__main__":
    main()