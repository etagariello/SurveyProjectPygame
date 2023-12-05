import sys
import pygame
import variables as var

def SLOW_PRINT(text, X_Y_Position=var.middle, font_size=var.FONT_SIZE, delay=var.DELAY, font_color=var.FONT_COLOR):
    font = pygame.font.Font(None, font_size)

    x, y = 0, 0
    pixel_color = var.screen.get_at((x, y))
    # if the screen is black, write in white
    if pixel_color == (0, 0, 0, 255):
        text_surface = font.render("", True, var.WHITE)
        text_rect = text_surface.get_rect(center=X_Y_Position)

    # if the screen is light grey, write in black
    elif pixel_color == (200, 200, 200, 255):
        text_surface = font.render("", True, font_color)
        text_rect = text_surface.get_rect(center=X_Y_Position)

    # this is for screen setup
    if text == "- Welcome to the Survey! -":
        text_rect.top = 20  # Adjust this value as needed for precise y positioning
        text_rect.left = 300  # Adjust this value as needed for precise x positioning
    if text == "- Start -":
        font = pygame.font.Font(None, 55)
        text_rect.top = 150
        text_rect.left = 530
    if text == "- Quit -":
        font = pygame.font.Font(None, 55)
        text_rect.top = 250
        text_rect.left = 530

    # if invalid command/response is given
    if text == "Invalid Command. Try Again." or text == "Invalid Response. Try Again.":
        font = pygame.font.Font(None, 55)
        text_rect.top = 500
        text_rect.left = 0

    # normal sentence positioning
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Oh... my survey can't recognize that name...":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Let me check it out":
        text_rect.top = 220
        text_rect.left = 350
    if text == ".....":
        font = pygame.font.Font(None, 200)
        text_rect.top = 230
        text_rect.left = 500
    if text == "Oooooooh, your name is just ugly.":
        text_rect.top = 150
        text_rect.left = 170
    if text == "Well...":
        text_rect.top = 220
        text_rect.left = 520
    if text == "Then what's your gender?":
        text_rect.top = 290
        text_rect.left = 280
    if text == "So I can name you. (male, female)":
        text_rect.top = 360
        text_rect.left = 80
    if text == "Ah I see... your name is now Bob. Cherish it.":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Ah I see... your name is now Barbara. Cherish it.":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Well Bob,":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Well Bob,":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Well Bob,":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Well Bob,":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Well Bob,":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Well Bob,":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Well Bob,":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Well Bob,":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Well Bob,":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Well Bob,":
        text_rect.top = 150
        text_rect.left = 80



    char_index = 0
    next_char_time = pygame.time.get_ticks() + delay * 1000

    while char_index <= len(text):
        current_text = text[:char_index]
        # if screen black, write in white
        if pixel_color == (0, 0, 0, 255):
            text_surface = font.render(current_text, True, var.WHITE)
            text_rect.size = text_surface.get_size()
            var.screen.blit(text_surface, text_rect)

        # if screen is grey, write in black
        elif pixel_color == (200, 200, 200, 255):
            text_surface = font.render(current_text, True, font_color)
            text_rect.size = text_surface.get_size()
            var.screen.blit(text_surface, text_rect)

        pygame.display.flip()

        if pygame.time.get_ticks() > next_char_time:
            char_index += 1
            next_char_time = pygame.time.get_ticks() + delay * 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        var.clock.tick(var.FPS)
