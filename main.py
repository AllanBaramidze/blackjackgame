import pygame
import sys

# pygame setup
pygame.init()
initial_width = 1500
initial_height = 800
screen = pygame.display.set_mode((initial_width, initial_height), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Blackjack Simulator")

text_font = pygame.font.SysFont("Times New Roman", 50, bold=True)

Header_Text = "BlackJack Simulator"
text_col = (0, 0, 0)

# prerender of text
text_surface = text_font.render(Header_Text, True, text_col)
text_rect = text_surface.get_rect()




def draw_text():
    # centerx calculates centering Header
    text_rect.centerx = screen.get_rect().centerx
    # y-pos fixed
    text_rect.y = 35

    screen.blit(text_surface, text_rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Update screen dimensions
            new_width, new_height = event.size
            screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

    # fill color to wipe anything from last frame
    screen.fill("#35654d")

    # Call the updated draw function
    draw_text()
    # Render Game Here

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits fps to 60
pygame.quit()