import sys
import pygame
import variables as var

pygame.init()
# Function to display wrapped and slow-printed text on the screen
def slow_print_wrapped_text(text, X_Y_Position=var.middle, font_size=var.FONT_SIZE, delay=var.DELAY):
    font = pygame.font.Font(None, font_size)

    x, y = 0, 0
    pixel_color = var.screen.get_at((x, y))
    if pixel_color == (0, 0, 0, 255):
        text_surface = font.render("", True, var.WHITE)
        text_rect = text_surface.get_rect(center=X_Y_Position)

    elif pixel_color == (200, 200, 200, 255):
        text_surface = font.render("", True, var.BLACK)
        text_rect = text_surface.get_rect(center=X_Y_Position)

    # this is for screen setup
    if text == "- Welcome to the Survey! - ":
        text_rect.top = 20  # Adjust this value as needed for precise y positioning
        text_rect.left = 300  # Adjust this value as needed for precise x positioning
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

    # normal questions positioning
    if text == "Hello there! What's your name?":
        text_rect.top = 150
        text_rect.left = 230

    # Split text into lines that fit within the screen width
    def wrap_text(text, max_width):
        words = text.split(' ')
        lines = []
        line = ''

        for word in words:
            test_line = line + word + ' '
            test_rect = font.render(test_line, True, var.BLACK).get_rect()

            if test_rect.width < max_width:
                line = test_line
            else:
                lines.append(line)
                line = word + ' '

        lines.append(line)  # Add the last line
        return lines

    char_index = 0
    next_char_time = pygame.time.get_ticks() + delay * 1000

    lines = wrap_text(text, 1000)  # Wrap the text

    for line in lines:
        while char_index <= len(line):
            current_text = line[:char_index]

            if pixel_color == (0, 0, 0, 255):
                text_surface = font.render(current_text, True, var.WHITE)
                text_rect.size = text_surface.get_size()
                var.screen.blit(text_surface, text_rect)

            elif pixel_color == (200, 200, 200, 255):
                text_surface = font.render(current_text, True, var.BLACK)
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


# Usage:
slow_print_wrapped_text("This is a long text so i can test if this wraps or not")
