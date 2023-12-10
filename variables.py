import pygame

# Constants
WIDTH, HEIGHT = 1200, 800
middle = (WIDTH // 2, HEIGHT // 2)
middle_X = WIDTH // 2
middle_Y = HEIGHT // 2
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
LIGHT_GREY = (100, 100, 100)
LIGHTER_GREY = (150, 150, 150)
LIGHTERER_GREY = (200, 200, 200)
DARK_RED = (150, 0, 0)

# Set up Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frustration: The Test")
clock = pygame.time.Clock()

# font
FONT_SIZE = 70
FONT_SIZE_INVALIDS = 55
FONT_BLACK = BLACK
FONT_COLOR_FOR_WARNINGS = DARK_RED
FONT_WHITE = WHITE
DELAY = 0.05  # Adjust the delay for character printing speed
DELAY_FOR_WARNINGS = 0.075

# list of all responses
all_responses = []

# this list is of phrases if they don't know the person well
no_knowledge_options = [">nothing", ">a little", ">little", ">little to nothing", ">somewhat", ">barely",
                        ">barely anything"]
# this list is if they do
knowledge_options = [">a lot", ">everything", ">a good amount", ">a decent amount", ">decently"]

# list of valid responses
valid_answers = [">addition", ">adding", ">summation", ">increment", ">increase", ">sum", ">incrementing",
                 ">increasing"]

