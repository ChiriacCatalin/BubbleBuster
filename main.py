import pygame
import os
import numpy as np
import random
import math 

WIDTH, HEIGHT = 550, 720
GAME_WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BubbleBuster")
background_image = pygame.image.load(os.path.join('Assets', 'background.jpg'))
SETTINGS_SPACE = 50

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
colors = [RED,PURPLE,CYAN,BLUE,YELLOW]

def intialize_data():
    generate_level_rect_grid()
    generate_balls_map()

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


def draw_map_balls():
    for i in range(len(balls_center)):
        for j in range(len(balls_center[i])):
            if balls_center[i][j][0] == 1:
                pygame.draw.circle(GAME_WINDOW, balls_center[i][j][3],(balls_center[i][j][1], balls_center[i][j][2]), BALL_RADIUS)
                pygame.draw.circle(GAME_WINDOW, GRAY, (balls_center[i][j][1], balls_center[i][j][2]), BALL_RADIUS,width=1)


def draw_window(throwing_bubble_rect, bubble_color):
    GAME_WINDOW.fill(WHITE)
    GAME_WINDOW.blit(background_image, (0,0))
    draw_map_balls()
    pygame.draw.rect(GAME_WINDOW, GRAY, (0,0,WIDTH, SETTINGS_SPACE))
    pygame.draw.circle(GAME_WINDOW, bubble_color,(throwing_bubble_rect.x + BALL_RADIUS, throwing_bubble_rect.y+BALL_RADIUS), BALL_RADIUS)
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
    if throwing_bubble_rect.y < SETTINGS_SPACE:
        throwing_bubble_rect.x = WIDTH/2-BALL_RADIUS
        throwing_bubble_rect.y = HEIGHT-2*BALL_RADIUS
        return -1
    return angle

def threat_collision_point(throwed_ball_rect, i, j, color = BLACK):
    collision_tolerance = BALL_VELOCIY + 1
    line = col = 0
    # if the bubble collides with the bottom of another bubble
    if abs(throwed_ball_rect.top - balls_center[i][j][4].bottom) < collision_tolerance:
        line = i+1
        if (throwed_ball_rect.x - balls_center[i][j][4].x) < 0: # if the bubble should be placed down, on the left side 
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
    if abs(throwed_ball_rect.right - balls_center[i][j][4].left) < collision_tolerance and check_clear_position(i, j-1):
        line = i
        col = j-1
    # if the bubble should be placed on the right side 
    if abs(throwed_ball_rect.left - balls_center[i][j][4].right) < collision_tolerance and check_clear_position(i, j+1):
        line = i
        col = j+1


    if line == 0 and col == 0:
        print("Error:",throwed_ball_rect, balls_center[i][j][4])
   # print(line, col)
    add_bubble_to_map(line, col, color)
    return(line, col)


def check_clear_position(i, j):
    if balls_center[i][j][0] != 0:
        return False
    return True

def add_bubble_to_map(line, col, color = BLACK):
    balls_center[line][col][0] = 1
    balls_center[line][col][3] = color
    aux_rect = pygame.Rect(balls_center[line][col][1] - BALL_RADIUS, balls_center[line][col][2] - BALL_RADIUS, 2 * BALL_RADIUS, 2* BALL_RADIUS)
    balls_center[line][col][4] = aux_rect

def check_collision(throwed_ball_rect, color = BLACK): # check if the throwed ball colides with any other ball, or the top of the screen
    for i in range(len(balls_center)):
        for j in range(len(balls_center[i])):
            if balls_center[i][j][4] != None:
                if throwed_ball_rect.colliderect(balls_center[i][j][4]):
                    (i,j) = threat_collision_point(throwed_ball_rect, i, j, color)
                    #print(i,j)
                    return (i,j)
    return (0,0)


def break_bubbles(i, j):
    neighbours_short_line = [(0,1), (0,-1), (1, 0), (1,1),(-1,0),(-1,1)]
    neighbours_long_line = [(0,1), (0,-1), (1,0),(1,-1),(-1,0),(-1,-1)] #extra checking for out of bounds
    tail = [(i,j)]
    head = 0
    while head < len(tail):
        current = tail[head]
        if current[0] % 2 == 0: # if it's a line with more bubbles
            for x in range(len(neighbours_long_line)):
                new_line = tail[head][0] + neighbours_long_line[x][0]
                new_col = tail[head][1] + neighbours_long_line[x][1]
                if new_col >= 0 and new_col < len(balls_center[new_line]): # if i'm not of bounds
                    if balls_center[new_line][new_col][3] == balls_center[i][j][3] and (new_line, new_col) not in tail: # and if they have the same color
                        tail.append((new_line, new_col))
        else:  # if it's a line with less bubbles
            for x in range(len(neighbours_short_line)):
                new_line = tail[head][0] + neighbours_short_line[x][0]
                new_col = tail[head][1] + neighbours_short_line[x][1]
                if new_col >= 0 and new_col < len(balls_center[new_line]): # if i'm not of bounds
                    if balls_center[new_line][new_col][3] == balls_center[i][j][3] and (new_line, new_col) not in tail: # and if they have the same color
                        tail.append((new_line, new_col))
        head +=1
    if len(tail) > 2:
        delete_bubbles(tail)
        remove_floating_bubbles()

def delete_bubbles(bubbles):
    for i in range(len(bubbles)):
        balls_center[bubbles[i][0]][bubbles[i][1]][0] = 0
        balls_center[bubbles[i][0]][bubbles[i][1]][3] = None
        balls_center[bubbles[i][0]][bubbles[i][1]][4] = None
    

def remove_floating_bubbles():
    neighbours_short_line = [(0,1), (0,-1), (1, 0), (1,1),(-1,0),(-1,1)]
    neighbours_long_line = [(0,1), (0,-1), (1,0),(1,-1),(-1,0),(-1,-1)] #extra checking for out of bounds
    tail = []
    for i in range(len(balls_center[0])):
        if balls_center[0][i][0] == 1:
            tail.append((0,i))
    head = 0
    while head < len(tail):
        current = tail[head]
        if current[0] % 2 == 0: # if it's a line with more bubbles
            for x in range(len(neighbours_long_line)):
                new_line = tail[head][0] + neighbours_long_line[x][0]
                new_col = tail[head][1] + neighbours_long_line[x][1]
                if new_col >= 0 and new_col < len(balls_center[new_line]): # if i'm not of bounds
                    if balls_center[new_line][new_col][0] == 1 and (new_line, new_col) not in tail: # and if they have the same color
                        tail.append((new_line, new_col))
        else:  # if it's a line with less bubbles
            for x in range(len(neighbours_short_line)):
                new_line = tail[head][0] + neighbours_short_line[x][0]
                new_col = tail[head][1] + neighbours_short_line[x][1]
                if new_col >= 0 and new_col < len(balls_center[new_line]): # if i'm not of bounds
                    if balls_center[new_line][new_col][0] == 1 and (new_line, new_col) not in tail: # and if they have the same color
                        tail.append((new_line, new_col))
        head +=1
    
    to_remove = []
    for i in range(len(balls_center)):
        for j in range(len(balls_center[i])):
            if balls_center[i][j][0] ==1 and (i,j) not in tail:
                to_remove.append((i,j))
    delete_bubbles(to_remove)
def main():
    intialize_data()
    clock = pygame.time.Clock()

    throwing_bubble_rect = pygame.Rect(WIDTH/2-BALL_RADIUS, HEIGHT-2*BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)
    bubble_color = random.choice(colors)
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
        
        inserted_bubble = check_collision(throwing_bubble_rect, bubble_color)
        if inserted_bubble != (0,0):
            break_bubbles(inserted_bubble[0], inserted_bubble[1])
            throwing_bubble_rect = pygame.Rect(WIDTH/2-BALL_RADIUS, HEIGHT-2*BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)
            bubble_color = random.choice(colors)
            angle = -1
            
        draw_window(throwing_bubble_rect, bubble_color)



if __name__ == "__main__":
    main()