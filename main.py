"""
This is the main module which starts the process/game
"""
from levels import *
from drawMap import *
from throwBubble import *
from bubbleCollision import *


def initialize_data(level):
    """
    Initialize the map data for the specified level

    :param level: the level you want to initialize (1 or 2)
    """
    generate_level_rect_grid()
    if level == 1:
        generate_balls_map_level1(row_len=[5, 6, 9, 10, 11, 10, 9, 6, 5])
    else:
        generate_balls_map_level1(row_len=[7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5])


def run_game(level):
    """
    The main function that runs the game and calls all necessary functions

    :param level: the current level
    """
    clock = pygame.time.Clock()
    throwing_bubble_rect = pygame.Rect(WIDTH/2-BALL_RADIUS, HEIGHT-2
                                       * BALL_RADIUS, BALL_RADIUS * 2,
                                       BALL_RADIUS * 2)
    bubble_color = random.choice(list(available_colors))
    next_bubble_color = random.choice(list(available_colors))
    game_running = True
    angle = -1
    status = 'continue'
    while game_running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and angle < 0:
                pos = pygame.mouse.get_pos()
                # get the angle between the bubble and the clicked area
                angle = ball_angle(THROW_BALL, pos)
                # the float value of the position
                exact_pos = [throwing_bubble_rect.x, throwing_bubble_rect.y]
            
        if angle > 0:  # throw the ball
            angle = throw_the_bubble(throwing_bubble_rect, angle, exact_pos)
        
        inserted_bubble = check_collision(throwing_bubble_rect, bubble_color)
        if inserted_bubble != (0, -1):
            if inserted_bubble != (-1, -1):
                status = break_bubbles(inserted_bubble[0], inserted_bubble[1])
            throwing_bubble_rect = pygame.Rect(WIDTH/2-BALL_RADIUS,
                                               HEIGHT-2*BALL_RADIUS,
                                               BALL_RADIUS*2, BALL_RADIUS*2)
            if status != 'Finnish':
                bubble_color = next_bubble_color
                next_bubble_color = random.choice(list(available_colors))
                angle = -1

        draw_window(throwing_bubble_rect, bubble_color,
                    next_bubble_color, status, level)

        if inserted_bubble == (-1, -1):  # if I lost the game
            reset_global_data(status, level)
            pygame.event.clear()
            main(1)
        if status == 'Finnish':  # if I won the game/level
            reset_global_data(status, level)
            pygame.event.clear()
            if level == 1:
                main(2)
            else:
                main(1)


def main(level=1):
    """
    Main function - run the game

    :param level: the current level that is going to play
    """
    allocate_mem()
    initialize_data(level)
    run_game(level)


if __name__ == "__main__":
    main(1)
