import pygame
import sys
from input_elements import InputBox
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

#consts
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
FPS = 60
BACKGROUND_COLOR = "#35654d"
TEXT_COLOR = (0, 0, 0)

class Text:
    def __init__(self, text, font, color, initial_y, initial_x, centered=True):
        self.text = text
        self.font = font
        self.color = color
        self.initial_y = initial_y
        self.initial_x = initial_x
        self.centered = centered
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.y = self.initial_y
        if self.centered:
            pass
        else:
            self.rect.x = self.initial_x

    def draw(self, screen):
        if self.centered:
            self.rect.centerx = screen.get_rect().centerx
        screen.blit(self.surface, self.rect)

#pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Blackjack Simulator Statistics")
clock = pygame.time.Clock()
#default font
text_font = pygame.font.SysFont("Arial", 50, bold=True)
smaller_font = pygame.font.SysFont("Arial", 35, bold=True)

#texts
header_text = Text("BlackJack Simulator", text_font, TEXT_COLOR, 35, 0, True)
table_heading2 = Text("Table", text_font, TEXT_COLOR, 155,0, True)
startingcap_heading2 = Text("Starting Capital", smaller_font, TEXT_COLOR, 135, 200, False)
decks_heading2 = Text("Decks", smaller_font, TEXT_COLOR, 275, 250, False)
decks_output = TextBox(screen, 400, 200, 50, 50, font = smaller_font)
players_heading2 = Text("Players", smaller_font, TEXT_COLOR, 400, 234, False)
players_output = TextBox(screen, 400, 400, 50, 50, font = smaller_font)

decks_output.disable()
players_output.disable()

#inputs
startingcap_input = InputBox(40, 138, 140, 35, 30, " ")
deck_slider = Slider(screen, 150, 275, 800, 40, min=1, max=7)
player_slider = Slider(screen, 150, 400, 800, 40, min=0, max=7)

#game
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()
        elif event.type == pygame.VIDEORESIZE:
            new_width, new_height = event.size
            screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

        startingcap_input.handle_event(event)

    decks_output.setText(deck_slider.getValue())
    players_output.setText(player_slider.getValue())

    #draws
    screen.fill(BACKGROUND_COLOR)
        #texts
    header_text.draw(screen)
    table_heading2.draw(screen)
    startingcap_heading2.draw(screen)
    decks_heading2.draw(screen)
    players_heading2.draw(screen)
        #input boxes
    startingcap_input.draw(screen)

    #render game

    #update display
    pygame_widgets.update(events)
    pygame.display.update()
    pygame.display.flip()


    #frame limit
    clock.tick(FPS)

