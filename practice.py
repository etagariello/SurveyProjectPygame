import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 30
FONT_SIZE = 32
TEXT = "Hello, world!"
FONT_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)
DELAY = 0.1  # Adjust the delay for character printing speed

# Set up Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slow Text Printing")
clock = pygame.time.Clock()

# Font initialization
font = pygame.font.Font(None, FONT_SIZE)
text_surface = font.render("", True, FONT_COLOR)
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Initialize variables for text printing
current_text = ""
next_char_time = pygame.time.get_ticks() + DELAY * 1000
char_index = 0

running = True
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Print text gradually
    if char_index < len(TEXT):
        if pygame.time.get_ticks() > next_char_time:
            current_text += TEXT[char_index]
            char_index += 1
            text_surface = font.render(current_text, True, FONT_COLOR)
            next_char_time = pygame.time.get_ticks() + DELAY * 1000

    # Blit text to the screen
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(FPS)
