import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox


#consts
TEXT_COLOUR = (0, 0, 0) #black
INACTIVE_COLOUR = (200, 200, 200) #lightgray
ACTIVE_COLOUR = (255, 255, 255) #white
OUTLINE_COLOUR = (50, 50, 50) #darkgrey
SLIDER_ACTIVE_COLOUR = (255, 165, 0) #orange
    #slider
SLIDER_HEIGHT = 8 #thickness of line
HANDLE_SIZE = 16 #diameter of dot
HOVER_TEXT_OFFSET = 30 #distance of text above handle

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

class InputBox:
    def __init__(self, x, y, width, height, font, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = INACTIVE_COLOUR
        self.text = text
        self.font = pygame.font.SysFont("Times New Roman", 10, bold=False)
        self.max_length = 10
        self.text_surface = None
        self.active = False
        self._update_text() #init render

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            #is box clicked?
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

            self.color = ACTIVE_COLOUR if self.active else INACTIVE_COLOUR

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(f"Pressed: {self.text}")
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.unicode.isdigit() and len(self.text) < self.max_length:
                    self.text += event.unicode

            self._update_text()

    def _update_text(self):
        #re-render text
        self.text_surface = self.font.render(self.text, True, TEXT_COLOUR)

    def draw(self, screen):
        #rectangle box
        pygame.draw.rect(screen, self.color, self.rect, 0)
        #border
        pygame.draw.rect(screen, OUTLINE_COLOUR, self.rect, 2)

        if self.text_surface is not None:
            text_y_padding = (self.rect.height - self.text_surface.get_height()) // 2
            screen.blit (self.text_surface, (self.rect.x + 5, self.rect.y +text_y_padding))

class InputSlider:
    def __init__(self, screen, x, y, width, height, min_val, max_val, initial_value):
        self.slider = Slider(
            screen = screen,
            x=x,
            y=y,
            width=width,
            height=height,
            min=min_val,
            max=max_val,
            initial=initial_value,
            step=1,
            color=INACTIVE_COLOUR,
            handleColour=SLIDER_ACTIVE_COLOUR,
        )

        output_x = x + width // 2 - 25 # centered above slider
        output_y = y - 60
        self.output_label = TextBox(
            screen=screen,
            x=output_x,
            y=output_y,
            width=50,
            height=50,
            fontSize=20,
            color=TEXT_COLOUR,
        )

        self.output_label.disable()

    def update_logic(self):
        """reads current slider values and updates slider label"""
        #get current val. from slider, rounded
        current_value = int(self.slider.getValue())

        self.output_label.setText(str(current_value))
        return current_value

    def get_value(self):
        return self.slider.getValue()