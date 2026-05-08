import pygame

class Scorecard:
    def __init__(self, x, y):
        self.sum_all = 0
        self.points = 0
        self.scorecard = 0
        self.bonus = 0
        self.sum_above = 0
        self.sum_lower = 0
        self.color = "white"
        self.rect = pygame.Rect(x, y, 300, 700)
    
    def draw(self, window, font):
        pygame.draw.rect(window, (0, 255, 0), self.rect)
        list = ["Eins", "Zweien", "Dreien", "Vieren", "Fünfen", "Sechsen", "Gesamt", "Bonus", "Gesamt Bonus", "Dreierpasch", "Viererpasch", "Full-House", "Kleine Straße", "Große Straße", "Knüller", "Chance", "Gesamt unten", "Gesamt oben", "Ergebnis" ]
        y = 0
        for i in list:
            y += 30
            text_surf = font.render(i, True, (0, 255, 255))
            window.blit(text_surf, (720, y))
        
        y = 0
        for i in list:
            y += 30
            text_surf = font.render("0", True, (0, 255, 255))
            window.blit(text_surf, (870, y))
        
        y = 0
        for i in list:
            y += 30
            text_surf = font.render("0", True, (0, 255, 255))
            window.blit(text_surf, (920, y))

        

    def fill_categorie(self):
        pass

    def calculate(self):
        pass