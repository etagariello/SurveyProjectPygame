import sys
import pygame
import slow_print as slow
import input_box as inp
import loading_screen as load
import variables as var

pygame.init()

running = True
while running:
    # when user presses the X, the game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # START SCREEN
    # leave space at end so it inputs the last char(dk why it does that)
    slow.SLOW_PRINT("- Welcome to the Survey! -")
    slow.SLOW_PRINT("- Start -")
    slow.SLOW_PRINT("- Quit -")
    slow.SLOW_PRINT("(please be brutally honest with this survey, they can't see your answers)")
    inp.INPUT()
    load.LOADING()

    # ask for name
    slow.SLOW_PRINT("Hello there! What's your name?")

    # they put their name once but shows error
    inp.INPUT()
    slow.SLOW_PRINT("Invalid Response. Try Again.", font_color=var.DARK_RED)

    #they put it the second time, also shows error
    inp.INPUT()
    slow.SLOW_PRINT("Invalid Response. Try Again.", font_color=var.DARK_RED)

    # use this want to delete anything you want
    pygame.draw.rect(var.screen, var.LIGHTERER_GREY, (0, 0, 1200, 400))

    # tell them why it's not working
    slow.SLOW_PRINT("Oh... my survey can't recognize that name...")
    slow.SLOW_PRINT("Let me check it out")
    slow.SLOW_PRINT(".....", delay=1, font_color=)
    pygame.draw.rect(var.screen, var.LIGHTERER_GREY, (0, 0, 1200, 400))

    slow.SLOW_PRINT("Oooooooh, your name is just ugly.")
    slow.SLOW_PRINT("Well...", delay=1)

    # ask for gender
    slow.SLOW_PRINT("Then what's your gender?")
    slow.SLOW_PRINT("So I can name you. (male, female)")

    gender = inp.INPUT()
    pygame.draw.rect(var.screen, var.LIGHTERER_GREY, (0, 0, 1200, 500))

    # the male and female have different set of questions
    if gender == ">male":
        slow.SLOW_PRINT("Ah I see... your name is now Bob. Cherish it.")
        slow.SLOW_PRINT("Well Bob,")
        slow.SLOW_PRINT("How much do you know about whoever sent you this?")
        knowing = inp.INPUT()

        # if they say that they don't know enough about them, continue survey
        if knowing in var.no_knowledge_options:
            slow.SLOW_PRINT("Oh how disappointing.")
            slow.SLOW_PRINT("You should hang out more...", delay=0.5, font_color=var.DARK_RED)
            slow.SLOW_PRINT("Anyways...")

        # if they do, question them if they consider them friends
        elif knowing in var.knowledge_options:
            slow.SLOW_PRINT("ENOUGH TO CALL THEM A FRIEND?", delay=0.7, font_color=var.DARK_RED, font_size=90)
            friend = inp.INPUT()

            # if they say yes, continue the survey
            if friend == ">yes":
                slow.SLOW_PRINT("Well that's a great start.")
                slow.SLOW_PRINT("But then why would they send you this?...", delay=0.5, font_color=var.DARK_RED)
                slow.SLOW_PRINT("Anyways...")

            # if they say no or anything else, close survey
            else:
                slow.SLOW_PRINT("I NOW KNOW WHY THEY SENT THIS TO YOU...")
                slow.SLOW_PRINT("YOU. ARE. FAKE.")
                sys.exit()


        break
    elif gender == ">female":
        slow.SLOW_PRINT("Ah I see... your name is now Barbara. Cherish it.")
        slow.SLOW_PRINT("Well Barbara,")
        slow.SLOW_PRINT("How much do you know about whoever sent you this?")
        break
    else:
        slow.SLOW_PRINT("Invalid Response. Try Again.")
        inp.INPUT()

pygame.quit()
