"""

"""

from globalData import *
import random


def allocate_mem():
    """
    Create the bubble map matrix with empty values
    """
    row_len = 11
    row_height = 14
    for i in range(row_height):
        # empty/not empty, circle.x, circle.y, color, pygame.rect
        balls_row = [[None, None, None, None, None]] * (row_len - i % 2)
        balls_center.append(balls_row)


def generate_level_rect_grid():
    """
    Generate all the possible positions on the map for the bubbles
    """
    for i in range(len(balls_center)):
        indent_x = (i % 2+1) * BALL_RADIUS
        indent_y = SETTINGS_SPACE + BALL_RADIUS - i * 7
        for j in range(len(balls_center[i])):
            balls_center[i][j] = [0, indent_x + 2 * j * BALL_RADIUS, indent_y
                                  + 2 * i * BALL_RADIUS, None, None]


def generate_balls_map_level1(row_len):
    """
    Generate the bubble map for level 1

    :param row_len: the bubbles' layout
    """
    for i in range(len(row_len)):
        first_pos = (len(balls_center[i]) - row_len[i])//2
        for j in range(row_len[i]):
            pos = first_pos+j
            balls_center[i][pos][0] = 1  # not empty
            balls_center[i][pos][3] = random.choice(colors)
            #  create a rectangle around the bubble for collision
            aux_rect = pygame.Rect(balls_center[i][pos][1] - BALL_RADIUS,
                                   balls_center[i][pos][2] - BALL_RADIUS,
                                   2 * BALL_RADIUS, 2 * BALL_RADIUS)
            balls_center[i][pos][4] = aux_rect
            available_colors.add(balls_center[i][pos][3])


def reset_global_data(status, level):
    """
    Reset the data if the game is done

    :param status: the status of the game - 'Finnish' if the level is completed
    :param level: the current level of the game
    """
    balls_center.clear()
    available_colors.clear()
    result_text[0] = ""
    if status != 'Finnish' or level == 2:
        score[0] = 0
