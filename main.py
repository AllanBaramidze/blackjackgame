import pygame
import sys
import pygame_widgets
from input_elements import InputBox, Text, InputSlider, PlayerToggleButton
from consts import *
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
gamescreen =pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
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


#Empty grouped list for player seats
seat_selection_group = []

#Toggle Seat Buttons
BTN_seat1 = PlayerToggleButton(screen, 500, 200, "1", seat_selection_group )
BTN_seat2 = PlayerToggleButton(screen, 550, 270, "2", seat_selection_group)
BTN_seat3 = PlayerToggleButton(screen, 620, 340, "3", seat_selection_group)
BTN_seat4 = PlayerToggleButton(screen, 700, 410, "4", seat_selection_group)
BTN_seat5 = PlayerToggleButton(screen, 780, 340, "5", seat_selection_group)
BTN_seat6 = PlayerToggleButton(screen, 850, 270, "6", seat_selection_group)
BTN_seat7 = PlayerToggleButton(screen, 900, 200, "7", seat_selection_group)

BTN_seat1.activate()

game_state = "MENU"

def start_game():
    global game_state
    game_state = "GAME"

btn_begin = Button(win=screen,x=1000, y=600,width=200, height=60,text="BEGIN",fontSize=40,radius=15,
    pressedColour=(0, 200, 0),
    inactiveColour=(0, 150, 0),
    hoverColour=(50, 255, 50),
    onClick=start_game
)

def back_to_menu_action():
    global game_state
    game_state = "MENU"


btn_back = Button(win=gamescreen,x=10, y=10,width=100, height=40,text="BACK",fontSize=20, radius=10,
    pressedColour=(200, 0, 0),
    inactiveColour=(150, 0, 0),
    hoverColour=(255, 50, 50),
    onClick=back_to_menu_action
)


#game
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            new_width, new_height = event.size
            screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
        if game_state == "MENU":
            startingcap_input.handle_event(event)

    if game_state == "MENU":
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
            #update display
        pygame_widgets.update(events)

    # render game
    elif game_state == "GAME":

        #draws
        screen.fill(BACKGROUND_COLOR)
        #backbtn
        #texts
        font = pygame.font.SysFont(None, 60)
        game_text = font.render("GAME STARTED!", True, (255, 255, 255))
        screen.blit(game_text, (300, 300))









    pygame.display.update()
    pygame.display.flip()


    #frame limit
    clock.tick(FPS)



