"""
This module draws everything on the screen
"""

from globalData import *
import pygame
import time


def draw_map_balls():
    """
    Draw the bubbles currently fixed on the map
    """
    for i in range(len(balls_center)):
        for j in range(len(balls_center[i])):
            if balls_center[i][j][0] == 1:
                pygame.draw.circle(GAME_WINDOW, balls_center[i][j][3],
                                   (balls_center[i][j][1],
                                    balls_center[i][j][2]),
                                   BALL_RADIUS)
                pygame.draw.circle(GAME_WINDOW, GRAY, (balls_center[i][j][1],
                                                       balls_center[i][j][2]),
                                   BALL_RADIUS, width=1)


def draw_setting_menu(throwing_bubble_rect, next_bubble_color):
    """
    Draw the components from the setting bar.

    :param throwing_bubble_rect:
    :param next_bubble_color:
    """
    pygame.draw.rect(GAME_WINDOW, LIGHT_GRAY, (0, 0, WIDTH, SETTINGS_SPACE))
    score_text = SCORE_FONT.render("Score: " + str(score[0]), 1, WHITE)
    GAME_WINDOW.blit(score_text,
                     ((WIDTH - score_text.get_width())/2,
                      (SETTINGS_SPACE - score_text.get_height())/2))
    #  draw the next bubble
    pygame.draw.circle(GAME_WINDOW, next_bubble_color,
                       (WIDTH - BALL_RADIUS * 1.2, BALL_RADIUS),
                       BALL_RADIUS - 5)
    pygame.draw.circle(GAME_WINDOW, GRAY,
                       (throwing_bubble_rect.x + BALL_RADIUS,
                        throwing_bubble_rect.y+BALL_RADIUS),
                       BALL_RADIUS, width=1)


def draw_window(throwing_bubble_rect, bubble_color,
                next_bubble_color, status, level):
    """
    Draw everything on the screen.

    :param throwing_bubble_rect: the thrown ball surrounding rect
    :param bubble_color: the thrown ball color
    :param next_bubble_color: the next bubble color
    :param status: the game current status 'Finnish' or not
    :param level: the game current level
    """
    GAME_WINDOW.fill(WHITE)
    GAME_WINDOW.blit(background_image, (0, 0))

    draw_setting_menu(throwing_bubble_rect, next_bubble_color)

    draw_map_balls()

    if status == 'Finnish':
        result_text[0] = "You Won"
    if result_text[0] != "":
        result = RESULT_FONT.render(result_text[0], 1, GREEN)
        level_text = RESULT_FONT.render("Level " + str(level), 1, GREEN)
        height = (HEIGHT - SETTINGS_SPACE - result.get_height())/2
        GAME_WINDOW.blit(result, ((WIDTH - result.get_width())/2, height))
        GAME_WINDOW.blit(level_text, ((WIDTH - level_text.get_width())/2,
                                      (height + level_text.get_height()+20)))

    pygame.draw.circle(GAME_WINDOW, bubble_color,
                       (throwing_bubble_rect.x + BALL_RADIUS,
                        throwing_bubble_rect.y+BALL_RADIUS), BALL_RADIUS)
    pygame.draw.circle(GAME_WINDOW, GRAY,
                       (throwing_bubble_rect.x + BALL_RADIUS,
                        throwing_bubble_rect.y+BALL_RADIUS),
                       BALL_RADIUS, width=1)
    pygame.display.update()

    if result_text[0] != "":
        result_text[0] = ""
        time.sleep(5)
