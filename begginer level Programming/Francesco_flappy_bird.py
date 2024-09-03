import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Define game variables
bird_width = 32
bird_height = 24
bird_x = 100
bird_y = int(screen_height / 2 - bird_height / 2)
bird_velocity = 0
gravity = 0.5

# Load the bird image
bird_image = pygame.image.load("C:\\Users\\franc\\Desktop\\Preply Lessons Python\\begginer level Programming\\bird.png").convert_alpha()
bird_rect = bird_image.get_rect(center=(bird_x, bird_y))

# Load the pipe images
pipe_image_top = pygame.image.load("C:\\Users\\franc\\Desktop\\Preply Lessons Python\\begginer level Programming\\upper_pipe.png").convert_alpha()
pipe_image_bottom = pygame.image.load("C:\\Users\\franc\\Desktop\\Preply Lessons Python\\begginer level Programming\\upper_pipe.png").convert_alpha()

# Define the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -10

    bird_y += bird_velocity
    bird_velocity += gravity

    if bird_y + bird_height >= screen_height or bird_y <= 0:
        running = False

    screen.fill((0, 0, 0))
    screen.blit(bird_image, bird_rect)

    # Add collision detection with pipes
    pipe_width = 52
    pipe_height = 320
    pipe_x = screen_width
    pipe_y = random.randint(0, screen_height - pipe_height)
    pipe_velocity = 5

    if pipe_x + pipe_width < bird_x:
        pipe_x = screen_width
        pipe_y = random.randint(0, screen_height - pipe_height)

    if bird_y + bird_height >= pipe_y and bird_y <= pipe_y + pipe_height:
        running = False

    pipe_x -= pipe_velocity
    screen.blit(pipe_image_top, (pipe_x, pipe_y))
    screen.blit(pipe_image_bottom, (pipe_x, pipe_y + pipe_height))

    pygame.display.flip()

# Quit the game
pygame.quit()