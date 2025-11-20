import pygame
import sys
import pygame_widgets
from input_elements import InputBox, Text, InputSlider



#consts
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
FPS = 60
BACKGROUND_COLOR = "#35654d"
TEXT_COLOR = (0, 0, 0)



#pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Blackjack Simulator Statistics")
clock = pygame.time.Clock()

#fonts
text_font = pygame.font.SysFont("Arial", 50, bold=True)
smaller_font = pygame.font.SysFont("Arial", 35, bold=True)

#texts
header_text = Text("BlackJack Simulator", text_font, TEXT_COLOR, 35, 0, True)
table_heading2 = Text("Table", text_font, TEXT_COLOR, 155,0, True)
startingcap_heading2 = Text("Starting Capital", smaller_font, TEXT_COLOR, 135, 200, False)
decks_heading2 = Text("Decks", smaller_font, TEXT_COLOR, 275, 250, False)
players_heading2 = Text("Players", smaller_font, TEXT_COLOR, 400, 234, False)

#inputs
startingcap_input = InputBox(40, 138, 140, 35, 30, " ")

#slider
slider_width = 800
start_x = (SCREEN_WIDTH - slider_width) // 2
center_y = SCREEN_HEIGHT // 2
decks_slider = InputSlider(screen=screen,x = start_x,y = center_y,width = slider_width, height = 40, min_val = 1, max_val = 7, initial_value= 1)


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
    current_deck = decks_slider.update_logic()




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

