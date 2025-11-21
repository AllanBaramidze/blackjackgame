import pygame
import sys
import pygame_widgets
from input_elements import InputBox, Text, InputSlider, PlayerToggleButton
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox



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
smaller_font = pygame.font.SysFont("Times New Roman", 45, bold=True)

#texts
header_text = Text("BlackJack Simulator", text_font, TEXT_COLOR, 35, 0, True)
table_heading2 = Text("Table", smaller_font, TEXT_COLOR, 155,0, True)
startingcap_heading2 = Text("Starting Capital", smaller_font, TEXT_COLOR, 125, 200, False)
decks_heading2 = Text("Decks", smaller_font, TEXT_COLOR, 275, 250, False)
players_heading2 = Text("Players", smaller_font, TEXT_COLOR, 400, 234, False)
settings_heading2 = Text("Settings", smaller_font, TEXT_COLOR, 100, 1200, False)

#inputs
startingcap_input = InputBox(40, 138, 140, 35, smaller_font, " ")

#slider for deck
slider_width = 150
deck_start_x = 40
deck_start_y = 280
decks_slider = InputSlider(screen=screen,x = deck_start_x,y = deck_start_y,width = slider_width, height = 40, min_val = 1, max_val = 8, initial_value= 1)

#slider for players
player_start_x = 40
player_start_y = 410
player_slider = InputSlider(screen=screen, x = player_start_x, y = player_start_y, width = slider_width, height = 40, min_val = 0, max_val = 7, initial_value= 0)

#Toggle Seat Buttons
BTN_seat1 = PlayerToggleButton(screen, 500, 200, "1" )
BTN_seat2 = PlayerToggleButton(screen, 550, 270, "2" )
BTN_seat3 = PlayerToggleButton(screen, 620, 340, "3" )
BTN_seat4 = PlayerToggleButton(screen, 700, 410, "4" )
BTN_seat5 = PlayerToggleButton(screen, 780, 340, "5" )
BTN_seat6 = PlayerToggleButton(screen, 850, 270, "6" )
BTN_seat7 = PlayerToggleButton(screen, 900, 200, "7" )





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
    current_player = player_slider.update_logic()




    #draws
    screen.fill(BACKGROUND_COLOR)
        #texts
    header_text.draw(screen)
    table_heading2.draw(screen)
    startingcap_heading2.draw(screen)
    decks_heading2.draw(screen)
    players_heading2.draw(screen)
    settings_heading2.draw(screen)
        #input boxes
    startingcap_input.draw(screen)

    #render game

    #update display
    pygame_widgets.update(events)
    pygame.display.update()
    pygame.display.flip()


    #frame limit
    clock.tick(FPS)

