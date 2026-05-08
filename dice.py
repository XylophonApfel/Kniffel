import pygame
import random

class Dice:
    def __init__(self, x, y):
        self.value = random.randint(1, 6)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.color = "white"
        self.hold = False
    
    def draw(self, window):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        
        # Andere Farbe wenn gehalten
        if self.hold:
            pygame.draw.rect(window, (100, 100, 100), self.rect)
        else:
            pygame.draw.rect(window, (a, b, c), self.rect)

        if self.value == 1:
            pygame.draw.circle(window, "black",(self.x+25, self.y+25), 5)
        elif self.value == 2:
            pygame.draw.circle(window, "black",(self.x+8, self.y+8), 5)
            pygame.draw.circle(window, "black",(self.x+40, self.y+40), 5)
        elif self.value == 3:
            pygame.draw.circle(window, "black",(self.x+8, self.y+8), 5)
            pygame.draw.circle(window, "black",(self.x+43, self.y+43), 5)
            pygame.draw.circle(window, "black",(self.x+25, self.y+25), 5)
        elif self.value == 4:
            pygame.draw.circle(window, "black",(self.x+8, self.y+8), 5)
            pygame.draw.circle(window, "black",(self.x+8, self.y+43), 5)
            pygame.draw.circle(window, "black",(self.x+43, self.y+8), 5)
            pygame.draw.circle(window, "black",(self.x+43, self.y+43), 5)
        elif self.value == 5:
            pygame.draw.circle(window, "black",(self.x+8, self.y+8), 5)
            pygame.draw.circle(window, "black",(self.x+8, self.y+43), 5)
            pygame.draw.circle(window, "black",(self.x+43, self.y+8), 5)
            pygame.draw.circle(window, "black",(self.x+43, self.y+43), 5)
            pygame.draw.circle(window, "black",(self.x+25, self.y+25), 5)
        elif self.value == 6:
            pygame.draw.circle(window, "black",(self.x+8, self.y+8), 5) 
            pygame.draw.circle(window, "black",(self.x+8, self.y+43), 5)
            pygame.draw.circle(window, "black",(self.x+8, self.y+25), 5)
            pygame.draw.circle(window, "black",(self.x+43, self.y+8), 5)
            pygame.draw.circle(window, "black",(self.x+43, self.y+43), 5)
            pygame.draw.circle(window, "black",(self.x+43, self.y+25), 5)


    def roll(self):
        if not self.hold:
            self.value = random.randint(1, 6)
    
    def toggle_hold(self):
        self.hold = not self.hold
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)