import pygame, os, cup, dice, game, player, rules, scorecard, button

os.system("cls")


def roll_dice():
    if game_cup.throw():
        print(f"Würfe: {game_cup.amount_roll}")
        for i, d in enumerate(game_cup.get_dice_list()):
            print(f"Würfel {i+1}: {d.value}")
    else:
        print("Maximale Würfe erreicht!")


def creat_dice():
    global game_cup
    game_cup = cup.Cup()
    game_cup.add_dice(dice.Dice(50, 100))
    game_cup.add_dice(dice.Dice(150, 100))
    game_cup.add_dice(dice.Dice(250, 100))
    game_cup.add_dice(dice.Dice(350, 100))
    game_cup.add_dice(dice.Dice(450, 100))


def main():
    global game_cup
    pygame.init()
    window = pygame.display.set_mode((1000, 650))
    font = pygame.font.SysFont("Arial", 30)
    font_2 = pygame.font.SysFont("Arial", 20)
    background = pygame.transform.scale(pygame.image.load("Download.jpg"), (1000, 650))
    pygame.display.set_caption("Kniffel")
    clock = pygame.time.Clock()

    button_dice = button.Button("Würfeln", 550, 100, 100, 50, "blue", roll_dice)
    scorecard_1 = scorecard.Scorecard(700, 0)
    creat_dice()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Würfel anklicken zum Halten
            if event.type == pygame.MOUSEBUTTONDOWN:
                for dice_obj in game_cup.get_dice_list():
                    if dice_obj.is_clicked(event.pos):
                        dice_obj.toggle_hold()
                        print(f"Würfel: {'Gehalten' if dice_obj.hold else 'Freigegeben'} - Wert: {dice_obj.value}")
            
            button_dice.check_event(event)

        window.blit(background, (0, 0))
        
        for dice_obj in game_cup.get_dice_list():
            dice_obj.draw(window)
        
        button_dice.draw(window, font)
        scorecard_1.draw(window, font_2)

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()