  throwing_bubble_rect = pygame.Rect(WIDTH/2-BALL_RADIUS, HEIGHT-2*BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)
            bubble_color = next_bubble_color
            next_bubble_color = random.choice(list(available_colors))
            angle = -1