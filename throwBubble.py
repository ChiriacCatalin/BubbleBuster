"""
This module deals with throwing the bubble
"""

import math
from globalData import BALL_RADIUS, BALL_VELOCITY, WIDTH


def ball_angle(p1, p2):
    """
    Get the angle between 2 points

    :param p1: ball center coordinates
    :param p2: click area coordinates
    """
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]
    return -math.degrees(math.atan2(y_diff, x_diff))


def next_ball_position(init_pos, angle):
    """
    Update the position of the thrown ball considering the angle and the
    BALL_VELOCITY

    :param init_pos: the previous bubble position
    :param angle: the angle of the bubble
    """
    new_x = init_pos[0] + BALL_VELOCITY * math.cos(math.radians(angle))
    new_y = init_pos[1] - BALL_VELOCITY * math.sin(math.radians(angle))
    return new_x, new_y


def throw_the_bubble(throwing_bubble_rect, angle, exact_pos):
    """
    Update the position of the thrown ball and change the angle if it collides
    with a margin

    :param throwing_bubble_rect: the rect surrounding the thrown ball
    :param angle: the bubble angle
    :param exact_pos: the float value of the coordinates
    :return:
    """
    (exact_pos[0], exact_pos[1]) = next_ball_position(exact_pos, angle)
    (throwing_bubble_rect.x, throwing_bubble_rect.y) = \
        (int(exact_pos[0]), int(exact_pos[1]))

    # change angle on collision with the right or left margin
    if throwing_bubble_rect.x + 2 * BALL_RADIUS >= WIDTH or \
            throwing_bubble_rect.x <= 0:
        angle = 180 - angle
    # if throwing_bubble_rect.y < SETTINGS_SPACE:
    #     throwing_bubble_rect.x = WIDTH/2-BALL_RADIUS
    #     throwing_bubble_rect.y = HEIGHT-2*BALL_RADIUS
    #     return -1
    return angle
