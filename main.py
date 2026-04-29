import pygame
import os
import cup
import dice
import game
import player
import rules
import scorecard

os.system("cls")




def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Kniffel")
    clock = pygame.time.Clock()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((52, 235, 55))

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()