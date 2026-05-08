import pygame,os, cup, dice, game, player, rules, scorecard, button

os.system("cls")



def creat_dice():
    global dice_1, dice_2, dice_3, dice_4, dice_5
    dice_1 = dice.Dice(50, 100)
    dice_2 = dice.Dice(150, 100)
    dice_3 = dice.Dice(250, 100)
    dice_4 = dice.Dice(350, 100)
    dice_5 = dice.Dice(450, 100)




def main():
    pygame.init()
    window = pygame.display.set_mode((1000, 650))
    font = pygame.font.SysFont("Arial", 30)
    font_2 = pygame.font.SysFont("Arial", 20)
    background = pygame.transform.scale(pygame.image.load("Download.jpg"), (1000, 650))
    pygame.display.set_caption("Kniffel")
    clock = pygame.time.Clock()


    button_dice = button.Button("Würfeln", 550, 100, 100, 50, "blue", creat_dice)
    scorecard_1 = scorecard.Scorecard(700, 0)
    creat_dice()




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
        scorecard_1.draw(window, font_2)

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()