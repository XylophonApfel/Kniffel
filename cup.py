import pygame

class Cup:
    def __init__(self):
        self.dice_list = []
        self.amount_roll = 0
        self.picked = False
    
    def add_dice(self, dice):
        self.dice_list.append(dice)
    
    def throw(self):
        if self.amount_roll < 3:
            for dice in self.dice_list:
                dice.roll()
            self.amount_roll += 1
            return True
        return False

    def get_dice_list(self):
        return self.dice_list

    def set_dice_list(self, dice_list):
        self.dice_list = dice_list

    def reset(self):
        self.amount_roll = 0
        for dice in self.dice_list:
            dice.hold = False
    