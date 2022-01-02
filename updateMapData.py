"""
This module deals with adding and removing bubbles from the bubble map
"""

from globalData import balls_center, BALL_RADIUS, available_colors, result_text
from score import *
import pygame


def add_bubble_to_map(line, col, color):
    """
    Add new bubbles to the map.

    :param line: the line at which the bubble should be added
    :param col: the column at which the bubble should be added
    :param color: the color of the bubble that should be added
    """
    if line == len(balls_center):
        result_text[0] = "You Lost!"
    else:
        balls_center[line][col][0] = 1
        balls_center[line][col][3] = color
        aux_rect = pygame.Rect(balls_center[line][col][1] - BALL_RADIUS,
                               balls_center[line][col][2] - BALL_RADIUS,
                               2 * BALL_RADIUS, 2 * BALL_RADIUS)
        balls_center[line][col][4] = aux_rect


def break_bubbles(i, j):
    """
     Break the bubbles of the same color on impact, and call to remove the
     bubbles that remain floating in the air

    :param i: the line at which the new bubble attached
    :param j: the column at which the new bubble attached
    :return: 'Finnish' if all bubbles were broken, 'continue' otherwise
    """
    neighbours_short_line = [(0, 1), (0, -1), (1, 0), (1, 1), (-1, 0), (-1, 1)]
    neighbours_long_line = [(0, 1), (0, -1), (1, 0),
                            (1, -1), (-1, 0), (-1, -1)]
    tail = [(i, j)]
    head = 0
    while head < len(tail):
        current = tail[head]
        if current[0] % 2 == 0:  # if it's a line with more bubbles
            for x in range(len(neighbours_long_line)):
                new_line = tail[head][0] + neighbours_long_line[x][0]
                new_col = tail[head][1] + neighbours_long_line[x][1]
                if len(balls_center) > new_line >= 0:
                    if 0 <= new_col < len(balls_center[new_line]):
                        if balls_center[new_line][new_col][3] == \
                                balls_center[i][j][3] and\
                                (new_line, new_col) not in tail:
                            # if both conditions happened
                            tail.append((new_line, new_col))
        else:  # if it's a line with fewer bubbles
            for x in range(len(neighbours_short_line)):
                new_line = tail[head][0] + neighbours_short_line[x][0]
                new_col = tail[head][1] + neighbours_short_line[x][1]
                if len(balls_center) > new_line >= 0:
                    if 0 <= new_col < len(balls_center[new_line]):
                        if balls_center[new_line][new_col][3] == \
                                balls_center[i][j][3] and\
                                (new_line, new_col) not in tail:
                            #  if both conditions happened
                            tail.append((new_line, new_col))
        head += 1
    if len(tail) > 2:
        delete_bubbles(tail)
        increment_score(len(tail))
        balls_left = remove_floating_bubbles()
        if balls_left == 0:
            return 'Finnish'
    return 'continue'


def delete_bubbles(bubbles):
    """
    Delete the data of the broken bubbles from the matrix.

    :param bubbles: The bubbles that need to be deletes
    """
    for i in range(len(bubbles)):
        balls_center[bubbles[i][0]][bubbles[i][1]][0] = 0
        balls_center[bubbles[i][0]][bubbles[i][1]][3] = None
        balls_center[bubbles[i][0]][bubbles[i][1]][4] = None


def remove_floating_bubbles():
    """
    This functions looks for the floating bubbles and removes them
    """
    neighbours_short_line = [(0, 1), (0, -1), (1, 0), (1, 1), (-1, 0), (-1, 1)]
    neighbours_long_line = [(0, 1), (0, -1), (1, 0),
                            (1, -1), (-1, 0), (-1, -1)]
    tail = []
    available_colors.clear()
    for i in range(len(balls_center[0])):
        if balls_center[0][i][0] == 1:
            tail.append((0, i))
            available_colors.add(balls_center[0][i][3])
    head = 0
    while head < len(tail):
        current = tail[head]
        if current[0] % 2 == 0:  # if it's a line with more bubbles
            for x in range(len(neighbours_long_line)):
                new_line = tail[head][0] + neighbours_long_line[x][0]
                new_col = tail[head][1] + neighbours_long_line[x][1]
                if len(balls_center) > new_line >= 0:
                    if 0 <= new_col < len(balls_center[new_line]):
                        if balls_center[new_line][new_col][0] == 1 and\
                                (new_line, new_col) not in tail:
                            #  if both conditions happened
                            tail.append((new_line, new_col))
                            available_colors.add(
                                balls_center[new_line][new_col][3])
        else:  # if it's a line with fewer bubbles
            for x in range(len(neighbours_short_line)):
                new_line = tail[head][0] + neighbours_short_line[x][0]
                new_col = tail[head][1] + neighbours_short_line[x][1]
                if len(balls_center) > new_line >= 0:
                    if 0 <= new_col < len(balls_center[new_line]):
                        if balls_center[new_line][new_col][0] == 1 and \
                                (new_line, new_col) not in tail:
                            #  if both conditions happened
                            tail.append((new_line, new_col))
                            available_colors.add(
                                balls_center[new_line][new_col][3])
        head += 1
    
    to_remove = []
    for i in range(len(balls_center)):
        for j in range(len(balls_center[i])):
            if balls_center[i][j][0] == 1 and (i, j) not in tail:
                to_remove.append((i, j))
    if len(to_remove) > 0:
        delete_bubbles(to_remove)
        increment_score(len(to_remove), True)
    return len(tail)
