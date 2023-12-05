import sys
import pygame
import variables as var


def LOADING(first=var.BLACK, second=var.GREY, third=var.LIGHT_GREY, fourth=var.LIGHTER_GREY, fifth=var.LIGHTERER_GREY):
    color = first
    timer = 0.5
    dt = 0

    running = True
    while running:
        # Handle the events.
        for event in pygame.event.get():
            # This allows the user to quit by pressing the X button.
            if event.type == pygame.QUIT:
                sys.exit()

        timer -= dt  # Decrement the timer by the delta time.
        if timer <= 0:  # When the time is up ...
            # Swap the colors.
            if color == first:
                var.screen.fill(color)
                color = second
                timer = 0.5
            elif color == second:
                var.screen.fill(color)
                color = third
                timer = 0.5
            elif color == third:
                var.screen.fill(color)
                color = fourth
                timer = 0.5
            elif color == fourth:
                var.screen.fill(color)
                color = fifth
                timer = 0.5
            elif color == fifth:
                var.screen.fill(color)
                return

        pygame.display.flip()
        # dt is the passed time since the last clock.tick call.
        dt = var.clock.tick(60) / 1000  # / 1000 to convert milliseconds to second
