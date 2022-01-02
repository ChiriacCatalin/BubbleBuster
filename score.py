"""
This module deals with calculating the score after each throw
"""
from globalData import score

# score for breaking 3-10 bubbles
# after those add 250 for each extra
score_values_for_same_color = [50, 100, 200, 300, 450, 650, 850, 1100]

# score for breaking 1 - 7 random bubbles
# after those add 75 for each extra
score_values_for_random_color = [5, 10, 25, 50, 75, 100, 150]


def increment_score(bubbles_destroyed, random_colors=False):
    """
    Increment the score after breaking some bubbles

    :param bubbles_destroyed: number of bubbles destroyed
    :param random_colors: True - the balls had the same color, False otherwise
    """
    if not random_colors:
        score[0] += score_values_for_same_color[min(7, bubbles_destroyed-3)]\
                    + max(0, (bubbles_destroyed - 10)) * 250
    else:
        score[0] += score_values_for_random_color[min(6, bubbles_destroyed-1)]\
                    + max(0, (bubbles_destroyed - 7)) * 75
