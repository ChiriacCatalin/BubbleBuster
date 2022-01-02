"""
    This module threats the collision between bubbles
"""
from updateMapData import *
import math
from globalData import SETTINGS_SPACE


def threat_collision_point(throwed_ball, i, j, color):
    """
    Look for the exact position of the collision and add the bubble in the
    corresponding place.

    :param throwed_ball: thrown bubble center coordinates
    :param i: line of the bubble that collides
    :param j: column of the bubble that collides
    :param color: color of the thrown bubble
    :return: (-1, -1) if the bubble should be placed above the maximum height
            and (line, column) otherwise
    """

    line = col = 0
    # if the bubble collides with the bottom of another bubble
    if abs(throwed_ball[1] - balls_center[i][j][2]) < 2 * BALL_RADIUS:
        line = i + 1
        # if the bubble should be placed down, on the left side
        if (throwed_ball[0] - balls_center[i][j][1]) < 0:
            # if it's a line with more bubbles per line(12 instead of 11)
            if i % 2 == 0:
                col = max(j - 1, 0)
            else:  # if it's a line with fewer bubbles per line
                col = j
        else:  # if the bubble should be placed down, on the right side
            # and it's a line with more bubbles per line(12 instead of 11)
            if i % 2 == 0:
                col = min(j, len(balls_center[i]) - 2)
            else:  # if it's a line with fewer bubbles per line
                col = j + 1

    # if the bubble should be placed on the left side 
    if throwed_ball[0] - balls_center[i][j][1] \
            < -BALL_RADIUS and check_clear_position(i, j - 1):
        line = i
        col = j - 1
    # if the bubble should be placed on the right side 
    if throwed_ball[0] - balls_center[i][j][1] \
            > BALL_RADIUS and check_clear_position(i, j + 1):
        line = i
        col = j + 1

    if line == 0 and col == 0:
        print("Error:", throwed_ball, balls_center[i][j][4])
    add_bubble_to_map(line, col, color)
    if line != len(balls_center):
        return line, col
    else:
        return -1, -1


def check_clear_position(i, j):
    """
    Check if the position we want to add the bubble to is free.

    :param i: line number in matrix
    :param j: column number in matrix
    :return: value of Truth
    """

    if balls_center[i][j][0] != 0:
        return False
    return True


def get_euclidian_distance(throwed_ball, ball_center):
    """
    Get the exact distance between the center of 2 bubbles.

    :param throwed_ball: the first bubble center coordinates
    :param ball_center: the second bubble center coordinates
    :return: return the distance
    """
    return (math.sqrt((throwed_ball[0] - ball_center[1]) ** 2
                      + (throwed_ball[1] - ball_center[2]) ** 2))


def check_collision(throwed_ball_rect, color):
    """
    Check if the thrown ball collides with any other bubble from the map and
    automatically call for the threat_collision_point() function

    :param throwed_ball_rect: thrown ball surrounding rectangle
    :param color: the color of the thrown bubble
    :return: return (0, -1 ) if no collision happened and (line, column)
        otherwise
    """
    bubble_center = (throwed_ball_rect.x + BALL_RADIUS, throwed_ball_rect.y
                     + BALL_RADIUS)
    for i in range(len(balls_center)):
        for j in range(len(balls_center[i])):
            if balls_center[i][j][0] == 1:
                if get_euclidian_distance(bubble_center, balls_center[i][j]) \
                        < 2 * BALL_RADIUS:
                    (i, j) = threat_collision_point(bubble_center, i, j, color)
                    return i, j
    if throwed_ball_rect.y < SETTINGS_SPACE:
        add_bubble_to_map(0, (throwed_ball_rect.x + BALL_RADIUS)
                          // (2 * BALL_RADIUS), color)
        return 0, (throwed_ball_rect.x + BALL_RADIUS) // (2 * BALL_RADIUS)
    return 0, -1
