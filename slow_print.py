import sys
import pygame
import variables as var

pygame.font.init()

def SLOW_PRINT(text, X_Y_Position=var.middle, font_size=var.FONT_SIZE, delay=var.DELAY, font_color=var.FONT_BLACK):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render("", True, font_color)
    text_rect = text_surface.get_rect(center=X_Y_Position)

    # this is for screen setup
    if text == "- Welcome -":
        text_rect.top = 20  # Adjust this value as needed for precise y positioning
        text_rect.left = 460  # Adjust this value as needed for precise x positioning
    if text == "- Start -":
        text_rect.top = 150
        text_rect.left = 530
    if text == "- Quit -":
        text_rect.top = 250
        text_rect.left = 530
    if text == "(type your command)":
        text_rect.top = 350
        text_rect.left = 410

    # if invalid command/response is given
    if text == "Invalid Command. Try Again." or text == "Invalid Response. Try Again.":
        text_rect.top = 500
        text_rect.left = 0

    # for name func
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Oh... my system can't recognize that name...":
        text_rect.top = 150
        text_rect.left = 65
    if text == "Let me check it out.":
        text_rect.top = 220
        text_rect.left = 350
    if text == ".....":
        font = pygame.font.Font(None, 200)
        text_rect.top = 230
        text_rect.left = 500
    if text == "Oooooooh, your name is just ugly.":
        text_rect.top = 150
        text_rect.left = 170
    if text == "Weeell":
        text_rect.top = 220
        text_rect.left = 500

    # for gender func
    if text == "Then what's your gender?":
        text_rect.top = 290
        text_rect.left = 280
    if text == "So I can name you.":
        text_rect.top = 360
        text_rect.left = 350
    if text == "Ah I see... your name is now Bob. Cherish it.":
        text_rect.top = 150
        text_rect.left = 80
    if text == "Ah I see... your name is now Barbara. Cherish it.":
        text_rect.top = 150
        text_rect.left = 30

    # how much do you know func
    if text == "Well Bob":
        text_rect.top = 220
        text_rect.left = 500
    if text == "Well Barbara":
        text_rect.top = 220
        text_rect.left = 445
    if text == "How much do you know about who sent you this?":
        text_rect.top = 290
        text_rect.left = 20
    if text == "Oh how disappointing.":
        text_rect.top = 150
        text_rect.left = 345
    if text == "DO BETTER":
        text_rect.left = 200

    # friend func
    if text == "ENOUGH TO CALL THEM A FRIEND?":
        text_rect.left = 20
    if text == "GOOD":
        text_rect.left = 350
    if text == "I SEE WHY THEY SENT THIS TO YOU...":
        text_rect.left = 30
    if text == "HAHAHAHA":
        text_rect.left = 30
    if text == "YES OR NO":
        text_rect.left = 100
    if text == "LET'S BEGIN :)":
        text_rect.left = 60

    # first try question func
    if text == "Let's start simple, alright Bob?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Let's start simple, alright Barbara?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230


    # what makes the text go slow
    char_index = 0
    next_char_time = pygame.time.get_ticks() + delay * 1000

    while char_index <= len(text):
        current_text = text[:char_index]
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
