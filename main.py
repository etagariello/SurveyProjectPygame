import pygame
import slow_print
import input_box
import variables

pygame.init()

running = True
while running:
    # when user presses the X, the game quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # START SCREEN
    # leave space at end so it inputs the last char(dk why it does that)
    slow_print.SLOW_PRINT("- Welcome to the Survey! - ", variables.middle)
    slow_print.SLOW_PRINT("- Start - ", variables.middle)
    slow_print.SLOW_PRINT("- Quit - ", variables.middle)

    input_box.INPUT()


pygame.quit()
