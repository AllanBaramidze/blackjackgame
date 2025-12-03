import pygame
import array as arr
import sys
import pygame_widgets
from input_elements import InputBox, Text, InputSlider, PlayerToggleButton
from consts import *
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox

#consts
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 800
FPS = 60


#textbox
header_text = Text("BlackJack Simulator", 'arial', 'black', 35, 0, True)





class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()


        self.gameStateManager = GameStateManager('Menu')
        self.menu = Menu(self.screen, self.gameStateManager)
        self.game = MainGame(self.screen, self.gameStateManager)

        self.states = {'Menu': self.menu, 'MainGame': self.game}
    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.gameStateManager.set_state('MainGame')

            self.states[self.gameStateManager.get_state()].run()

            pygame_widgets.update(events)
            pygame.display.update()
            self.clock.tick(FPS)

class Menu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('#35654d')
        header_text.draw(self.display)

class MainGame:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('green')

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state



if __name__ == '__main__':
    game = Game()
    game.run()

