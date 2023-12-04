import sys
import pygame
import slow_print
import variables

def INPUT():
    # Font and text-related variables
    font = pygame.font.Font(None, 55)
    text = ">"

    pygame.draw.rect(variables.screen, variables.BLACK, (0, 550, 1200, 200))

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: #removes last char when hit backspace
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:

                    # ALL IF STATEMENTS DEPENDING ON WHAT THEY ENTER
                    if text.lower() == ">quit": #quit if player types quit
                        sys.exit()

                    elif text.lower() == ">start":
                        variables.screen.fill(variables.BLACK)
                    else:
                        slow_print.SLOW_PRINT("Invalid Command. Try Again. ")
                        text = ">"

                else:
                    text += event.unicode

        pygame.draw.rect(variables.screen, variables.BLACK, (0, 550, 1200, 200))

        # Rendering text input box centered horizontally
        input_box = font.render(text, True, variables.WHITE)
        input_box_rect = input_box.get_rect(center=(variables.middle_X, 600))
        input_box_rect.left = 0

        variables.screen.blit(input_box, input_box_rect)

        pygame.display.flip()
        variables.clock.tick(60)




