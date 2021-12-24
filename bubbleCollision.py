from updateMapData import *
import math

def threat_collision_point(throwed_ball, i, j, color):
    line = col = 0
    # if the bubble collides with the bottom of another bubble
    if abs(throwed_ball[1] - balls_center[i][j][2]) < 2*BALL_RADIUS:
        line = i+1
        if (throwed_ball[0] - balls_center[i][j][1]) < 0: # if the bubble should be placed down, on the left side 
            if i % 2 == 0: # if its a line with more bubbles per line(12 instead of 11)
                col = max(j-1, 0)
            else: # if its a line with less bubbles per line
                col = j
        else: # if the bubble should be placed down, on the right side 
            if i % 2 == 0: # if its a line with more bubbles per line(12 instead of 11)
                col = min (j, len(balls_center[i])-2)
            else: # if its a line with less bubbles per line
                col = j+1
   
    # if the bubble should be placed on the left side 
    if throwed_ball[0] - balls_center[i][j][1] <  -BALL_RADIUS and check_clear_position(i, j-1):
        line = i
        col = j-1
    # if the bubble should be placed on the right side 
    if throwed_ball[0] - balls_center[i][j][1] > BALL_RADIUS and check_clear_position(i, j+1):
        line = i
        col = j+1

    if line == 0 and col == 0:
        print("Error:",throwed_ball, balls_center[i][j][4])
    #print("WTF", line, col)
    add_bubble_to_map(line, col, color)
    if line != len(balls_center):
        return(line, col)
    else:
         return (-1,-1)


def check_clear_position(i, j):
    if balls_center[i][j][0] != 0:
        return False
    return True


def get_euclidian_distance(throwed_ball, ball_center):
    return (math.sqrt((throwed_ball[0] - ball_center[1])**2 + (throwed_ball[1] - ball_center[2])**2))


def check_collision(throwed_ball_rect, color): # check if the throwed ball colides with any other ball, or the top of the screen
    bubble_center = (throwed_ball_rect.x + BALL_RADIUS, throwed_ball_rect.y + BALL_RADIUS)
    for i in range(len(balls_center)):
        for j in range(len(balls_center[i])):
            if balls_center[i][j][0] == 1:
                if get_euclidian_distance(bubble_center, balls_center[i][j]) < 2* BALL_RADIUS:
                    (i,j) = threat_collision_point(bubble_center, i, j, color)
                    return (i,j)
    return (0,0)