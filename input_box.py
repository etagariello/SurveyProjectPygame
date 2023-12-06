import sys
import pygame
import variables as var

def INPUT():
    # Font and text-related variables
    font = pygame.font.Font(None, 55)
    text = ">"

    x, y = 0, 0
    pixel_color = var.screen.get_at((x, y))

    # if the screen is black, make the rectangle black
    if pixel_color == (0, 0, 0, 255):
        pygame.draw.rect(var.screen, var.BLACK, (0, 470, 1200, 200))

    # if the screen is light grey, make the rectangle light gray
    elif pixel_color == (200, 200, 200, 255):
        pygame.draw.rect(var.screen, var.LIGHTERER_GREY, (0, 470, 1200, 200))

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: #removes last char when hit backspace
                    if text != ">":
                        text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    var.all_responses.append(text)
                    print(var.all_responses)
                    return text

                else:
                    text += event.unicode

        # this is to clean up whatever is written when necessary
        # if the screen is black, make the rectangle black
        if pixel_color == (0, 0, 0, 255):
            pygame.draw.rect(var.screen, var.BLACK, (0, 470, 1200, 200))

        # if the screen is light grey, make the rectangle light gray
        elif pixel_color == (200, 200, 200, 255):
            pygame.draw.rect(var.screen, var.LIGHTERER_GREY, (0, 470, 1200, 200))

        # Rendering text input box centered horizontally
        # if the screen is black, write the text in white
        if pixel_color == (0, 0, 0, 255):
            input_box = font.render(text, True, var.WHITE)
            input_box_rect = input_box.get_rect(center=(var.middle_X, 600))
            input_box_rect.left = 0
            var.screen.blit(input_box, input_box_rect)

        # if it's light grey, write the text in black
        elif pixel_color == (200, 200, 200, 255):
            input_box = font.render(text, True, var.BLACK)
            input_box_rect = input_box.get_rect(center=(var.middle_X, 600))
            input_box_rect.left = 0
            var.screen.blit(input_box, input_box_rect)

        pygame.display.flip()
        var.clock.tick(60)