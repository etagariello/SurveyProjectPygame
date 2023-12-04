import pygame

# Constants
WIDTH, HEIGHT = 1200, 800
middle = (WIDTH // 2, HEIGHT // 2)
middle_X = WIDTH // 2
middle_Y = HEIGHT // 2
FPS = 60
DELAY = 0.05  # Adjust the delay for character printing speed
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frenemy: The Survey")
clock = pygame.time.Clock()

# font
FONT_SIZE = 70
FONT_COLOR = (255, 255, 255)