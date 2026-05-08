import pygame
import os
import cup
import dice
import game
import player
import rules
import scorecard
import button

os.system("cls")



def creat_dice():
    global dice_1, dice_2, dice_3, dice_4, dice_5
    dice_1 = dice.Dice(100, 100)
    dice_2 = dice.Dice(200, 100)
    dice_3 = dice.Dice(300, 100)
    dice_4 = dice.Dice(400, 100)
    dice_5 = dice.Dice(500, 100)




def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("Arial", 30)
    creat_dice()
    background = pygame.transform.scale(pygame.image.load("Download.jpg"), (1200, 700))
    pygame.display.set_caption("Kniffel")
    clock = pygame.time.Clock()


    button_dice = button.Button("Würfeln", 650, 100, 100, 50, "blue", creat_dice)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        button_dice.check_event(event)

        window.blit(background, (0, 0))
        dice_1.draw(window)
        dice_2.draw(window)
        dice_3.draw(window)
        dice_4.draw(window)
        dice_5.draw(window)
        button_dice.draw(window, font)

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()