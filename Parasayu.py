import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I Don't Have Money, Sorry")

font = pygame.font.SysFont("arial", 60, bold=True)
clock = pygame.time.Clock()

text = "I don't have money, sorry"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Starting position (off-screen left)
x = -800
y = HEIGHT // 2
alpha = 0

# Render text
text_surface = font.render(text, True, WHITE)
text_surface.set_alpha(alpha)
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

running = True
phase = "fade_in"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Slide-in effect
    if x < WIDTH // 2 - text_rect.width // 2:
        x += 10

    # Fade-in effect
    if phase == "fade_in" and alpha < 255:
        alpha += 5
    elif phase == "fade_in" and alpha >= 255:
        time.sleep(1)
        phase = "fade_out"

    # Fade-out effect
    if phase == "fade_out" and alpha > 0:
        alpha -= 5
    elif phase == "fade_out" and alpha <= 0:
        running = False

    text_surface.set_alpha(alpha)
    screen.blit(text_surface, (x, y - text_rect.height // 2))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
