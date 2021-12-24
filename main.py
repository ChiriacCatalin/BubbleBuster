import random
from score import *
from levels import *
from drawMap import *
from throwBubble import *
from bubbleCollision import *

def intialize_data():
    generate_level_rect_grid()
    generate_balls_map()

def main():
    intialize_data()
    clock = pygame.time.Clock()
    throwing_bubble_rect = pygame.Rect(WIDTH/2-BALL_RADIUS, HEIGHT-2*BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)
    bubble_color = random.choice(list(available_colors))
    next_bubble_color = random.choice(list(available_colors))
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
            angle = throw_the_bubble(throwing_bubble_rect, angle, exact_position)
        
        inserted_bubble = check_collision(throwing_bubble_rect, bubble_color)
        if inserted_bubble != (0,0):
            if inserted_bubble != (-1,-1):
                break_bubbles(inserted_bubble[0], inserted_bubble[1])
            throwing_bubble_rect = pygame.Rect(WIDTH/2-BALL_RADIUS, HEIGHT-2*BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)
            bubble_color = next_bubble_color
            next_bubble_color = random.choice(list(available_colors))
            angle = -1
        
        draw_window(throwing_bubble_rect, bubble_color, next_bubble_color)


if __name__ == "__main__":
    main()