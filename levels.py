from globalData import *
import random
import pygame

def generate_level_rect_grid(): # generate all the possible positions on the map for the bubbles
    row_len = 11
    row_height = 14
    for i in range(row_height):
        balls_row= [[None, None, None, None, None]] * (row_len - i%2) # empty/not empty, circle.x, circle.y, color, pygame.rect
        indent_x = (i%2+1) * BALL_RADIUS
        indent_y = SETTINGS_SPACE + BALL_RADIUS - i * 7 
        for j in range(len(balls_row)):
            balls_row[j] = [0, indent_x + 2* j * BALL_RADIUS, indent_y + 2* i * BALL_RADIUS, None, None]
        balls_center.append(balls_row)

def generate_balls_map():
    row_len = [5,6,9,10,11,10,9,6,5] # the starting map layout
    for i in range(len(row_len)):
        first_pos = (len(balls_center[i]) - row_len[i])//2
        for j in range (row_len[i]):
            balls_center[i][first_pos+j][0] = 1 # not empty
            balls_center[i][first_pos+j][3] = random.choice(colors) # set a color
            #create a rectangle around the bubble for collision
            aux_rect = pygame.Rect(balls_center[i][first_pos+j][1] - BALL_RADIUS, balls_center[i][first_pos+j][2] - BALL_RADIUS, 2 * BALL_RADIUS, 2* BALL_RADIUS)
            balls_center[i][first_pos+j][4] = aux_rect
            available_colors.add(balls_center[i][first_pos+j][3])