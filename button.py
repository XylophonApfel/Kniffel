import pygame

class Button:
    def __init__(self, text, x, y, width, height, color, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.callback = callback
        self.is_hovered = False


    def draw(self, window, font):
        # Farbe ändern, wenn Maus drüber ist (Hover-Effekt)
        color = (200, 200, 200) if self.is_hovered else self.color  
        pygame.draw.rect(window, color, self.rect)

        #Text rendern
        text_surf = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        window.blit(text_surf, text_rect)

    def check_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        
        if event.type == pygame.MOUSEBUTTONDOWN: #and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()       