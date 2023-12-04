import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def clear_rect(surface, rect):
    # Create a surface with the same color as the background
    transparent_color = (0, 0, 0, 0)  # Transparent color with alpha = 0
    pygame.draw.rect(surface, transparent_color, rect)

running = True
while running:
    screen.fill(WHITE)  # Fill the screen with a background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Example: Clearing a rectangle (200x100) at position (300, 200)
    rect_to_clear = pygame.Rect(300, 200, 200, 50)
    clear_rect(screen, rect_to_clear)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
