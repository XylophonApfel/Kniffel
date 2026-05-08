import pygame
import random

class Dice:
    def __init__(self, x, y):
        self.value = random.randint(1, 6)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.color = "white"
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

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
        pass