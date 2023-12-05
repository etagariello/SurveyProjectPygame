import pygame
import slow_print as slow
import input_box as inp
import loading_screen as load
import  variables as var


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
    inp.INPUT()
    load.LOADING()

    # ask for name
    slow.SLOW_PRINT("Hello there! What's your name?")

    # they put their name once but shows error
    inp.INPUT()
    slow.SLOW_PRINT("Invalid Response. Try Again.")

    #they put it the second time, also shows error
    inp.INPUT()
    slow.SLOW_PRINT("Invalid Response. Try Again.")

    # use this want to delete to delete anything you want
    pygame.draw.rect(var.screen, var.LIGHTERER_GREY, (0, 0, 1200, 400))

    # tell them why it's not working
    slow.SLOW_PRINT("Oh... my survey can't recognize that name...")
    slow.SLOW_PRINT("Let me check it out")
    slow.SLOW_PRINT(".....", delay=1)
    pygame.draw.rect(var.screen, var.LIGHTERER_GREY, (0, 0, 1200, 400))

    slow.SLOW_PRINT("Oooooooh, your name is just ugly af.")
    slow.SLOW_PRINT("Well...", delay=1)

    # ask for gender
    slow.SLOW_PRINT("Then what's your gender?")
    slow.SLOW_PRINT("So I can call you by that. (male, female, other)")

    gender = inp.INPUT()
    pygame.draw.rect(var.screen, var.LIGHTERER_GREY, (0, 0, 1200, 500))
    # the male and female have different set of questions
    if gender == ">male":
        slow.SLOW_PRINT("Ah I see... your name is now Boy. Cherish it.")
        slow.SLOW_PRINT("Well Boy,")
        slow.SLOW_PRINT("How much do you think you know about whoever sent you this?")

        break
    elif gender == ">female":
        slow.SLOW_PRINT("Ah I see... your name is now Girl. Cherish it.")
        break
    else:
        slow.SLOW_PRINT("Invalid Response. Try Again.")
        inp.INPUT()

pygame.quit()
