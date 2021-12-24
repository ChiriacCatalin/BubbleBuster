import math
from globalData import BALL_RADIUS, BALL_VELOCIY, SETTINGS_SPACE, HEIGHT, WIDTH

def ball_angle(p1, p2):
    xDiff = p2[0] - p1[0]
    yDiff = p2[1] - p1[1]
    return -math.degrees(math.atan2(yDiff, xDiff))

def next_ball_position(init_pos, angle):
    new_x = init_pos[0] + BALL_VELOCIY * math.cos(math.radians(angle))
    new_y = init_pos[1] - BALL_VELOCIY * math.sin(math.radians(angle))
    return (new_x, new_y)

def throw_the_bubble(throwing_bubble_rect, angle, exact_position):
    (exact_position[0], exact_position[1]) = next_ball_position(exact_position, angle)
    (throwing_bubble_rect.x, throwing_bubble_rect.y) = (int(exact_position[0]),int(exact_position[1])) # update the positon of the ball

    # change angle on collision with the right or left margin
    if throwing_bubble_rect.x + 2 * BALL_RADIUS >= WIDTH or throwing_bubble_rect.x <=0:
        angle = 180 - angle
    if throwing_bubble_rect.y < SETTINGS_SPACE:
        throwing_bubble_rect.x = WIDTH/2-BALL_RADIUS
        throwing_bubble_rect.y = HEIGHT-2*BALL_RADIUS
        return -1
    return angle