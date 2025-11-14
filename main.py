from json.encoder import py_encode_basestring_ascii

import pygame
import sys

#pygame setup
pygame.init()
screen = pygame.display.set_mode((1500, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Blackjack Simulator")


text_font = pygame.font.SysFont("Times New Roman", 50, bold=True)

def draw_text(text, font, size, x, y):
    text_col = (0, 0, 0)
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill color to wipe anything from last frame
    screen.fill("#35654d")

    draw_text("BlackJack Simulator", text_font, 50, 525, 35)
    #Render Game Here

    #flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60) #limits fps to 60
pygame.quit()