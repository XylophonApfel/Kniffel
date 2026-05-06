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

    dice_1 = dice.Dice(100, 100)
    dice_2 = dice.Dice(200, 100)
    dice_3 = dice.Dice(300, 100)
    dice_4 = dice.Dice(400, 100)
    dice_5 = dice.Dice(500, 100)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((52, 235, 55))
        dice_1.draw(window)
        dice_2.draw(window)
        dice_3.draw(window)
        dice_4.draw(window)
        dice_5.draw(window)

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()