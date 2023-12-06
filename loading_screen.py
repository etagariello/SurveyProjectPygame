import sys
import pygame
import variables as var

def LOADING(first=var.BLACK, second=var.GREY, third=var.LIGHT_GREY, fourth=var.LIGHTER_GREY, fifth=var.LIGHTERER_GREY, timer=0.5):
    color = first
    dt = 0
    given_timer = timer

    running = True
    while running:
        # Handle the events.
        for event in pygame.event.get():
            # This allows the user to quit by pressing the X button.
            if event.type == pygame.QUIT:
                sys.exit()

        given_timer -= dt  # Decrement the timer by the delta time.
        if given_timer <= 0:  # When the time is up ...
            # Swap the colors.
            if color == first:
                var.screen.fill(color)
                color = second
                given_timer = timer
            elif color == second:
                var.screen.fill(color)
                color = third
                given_timer = timer
            elif color == third:
                var.screen.fill(color)
                color = fourth
                given_timer = timer
            elif color == fourth:
                var.screen.fill(color)
                color = fifth
                given_timer = timer
            elif color == fifth:
                var.screen.fill(color)
                return

        pygame.display.flip()
        # dt is the passed time since the last clock.tick call.
        dt = var.clock.tick(60) / 1000  # / 1000 to convert milliseconds to second