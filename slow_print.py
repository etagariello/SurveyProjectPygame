import sys
import pygame
import variables
def SLOW_PRINT(text, X_Y_Position = (variables.middle_X, 150), font_size=variables.FONT_SIZE, font_color=variables.FONT_COLOR, delay=variables.DELAY):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render("", True, font_color)
    text_rect = text_surface.get_rect(center=X_Y_Position)

    # For top alignment, set the Y-coordinate of text_rect to the top of the screen
    # this is for screen setup
    if text == "- Welcome to the Survey! - ":
        text_rect.top = 20  # Adjust this value as needed for precise y positioning
        text_rect.left = 300 #  Adjust this value as needed for precise x positioning
    if text == "- Start - ":
        font = pygame.font.Font(None, 55)
        text_rect.top = 150
        text_rect.left = 530
    if text == "- Quit - ":
        font = pygame.font.Font(None, 55)
        text_rect.top = 250
        text_rect.left = 530

    # if invalid command is given
    if text == "Invalid Command. Try Again. ":
        font = pygame.font.Font(None, 55)
        text_rect.top = 500
        text_rect.left = 0

    char_index = 0
    next_char_time = pygame.time.get_ticks() + delay * 1000

    while char_index <= len(text):
        current_text = text[:char_index]
        text_surface = font.render(current_text, True, font_color)
        text_rect.size = text_surface.get_size()

        variables.screen.blit(text_surface, text_rect)
        pygame.display.flip()

        if pygame.time.get_ticks() > next_char_time:
            char_index += 1
            next_char_time = pygame.time.get_ticks() + delay * 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        variables.clock.tick(variables.FPS)

