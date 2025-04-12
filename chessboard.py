import pygame

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 800
BOARD_SIZE = 8
SQUARE_SIZE = WINDOW_SIZE // BOARD_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Chess Board")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the chessboard
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Calculate square position
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            
            # Alternate between white and black squares
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
