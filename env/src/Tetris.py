import pygame
import random

# Initialize pygame
pygame.init()

# Set up display dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
CELL_SIZE = 30

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tetromino shapes and colors
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1], [1, 1]]
]

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Game variables
grid = [[0] * (SCREEN_WIDTH // CELL_SIZE) for _ in range(SCREEN_HEIGHT // CELL_SIZE)]
current_shape = None
current_color = None
current_x = SCREEN_WIDTH // 2
current_y = 0

# Create a new tetromino
def new_tetromino():
    global current_shape, current_color, current_x, current_y
    current_shape = random.choice(SHAPES)
    current_color = random.choice(COLORS)
    current_x = (SCREEN_WIDTH // CELL_SIZE // 2) * CELL_SIZE
    current_y = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        current_x -= CELL_SIZE
    if keys[pygame.K_RIGHT]:
        current_x += CELL_SIZE

    # Clear screen
    screen.fill(BLACK)

    # Move tetromino down
    current_y += CELL_SIZE

    # Draw current shape
    for row in range(len(current_shape)):
        for col in range(len(current_shape[0])):
            if current_shape[row][col]:
                pygame.draw.rect(screen, current_color,(current_x + col * CELL_SIZE, current_y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)

# Quit pygame
pygame.quit()