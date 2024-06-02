import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dodge the Blocks!')

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player properties
player_size = 50
player_pos = [screen_width // 2, screen_height - 2 * player_size]
player_speed = 10

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, screen_width - enemy_size), 0]
enemy_speed = 10

# Set up the game loop
clock = pygame.time.Clock()
running = True

def detect_collision(player_pos, enemy_pos):
    p_x, p_y = player_pos
    e_x, e_y = enemy_pos
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed

    # Update the enemy position
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > screen_height:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, screen_width - enemy_size)

    # Collision detection
    if detect_collision(player_pos, enemy_pos):
        running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    # Draw the enemy
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

pygame.quit()
