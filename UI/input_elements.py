import pygame

#colour consts
colour_INACTIVE = pygame.Color('lightgoldenrod1')
colour_ACTIVE = pygame.Color('lightgoldenrod2')
colour_TEXT = pygame.Color('gray0')
colour_BG = pygame.Color('lightgoldenrod1')

FONT = pygame.font.Font(None, 32)

class StartingCap:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.colour = colour_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, colour_TEXT)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.colour = colour_ACTIVE if self.active else colour_INACTIVE

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(f"Input Valid: {self.text}")
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isdigit():
                self.text += event.unicode

            #update text surface
            self.txt_surface = FONT.render(self.text, True, colour_TEXT)

    def update(self):
        # will resize box if input too long
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        pygame.draw.rect(screen, colour_BG, self.rect, 0)
        pygame.draw.rect(screen, self.colour, self.rect, 3)

        #blit the text
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))