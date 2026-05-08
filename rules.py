import pygame

class Rules:
    def __init__(self):
        self.rules = {}

    def count_dice(self, dice_list, number):
        count = 0
        for dice in dice_list:
            if dice.value == number:
                count += 1
        return count
    
    def sum_all_dice(self, dice_list):
        total = 0
        for dice in dice_list:
            total += dice.value
        return total

    # Oberer Teil
    def ones(self, dice_list):
        return self.count_dice(dice_list, 1) * 1

    def twos(self, dice_list):
        return self.count_dice(dice_list, 2) * 2

    def threes(self, dice_list):
        return self.count_dice(dice_list, 3) * 3

    def fours(self, dice_list):
        return self.count_dice(dice_list, 4) * 4

    def fives(self, dice_list):
        return self.count_dice(dice_list, 5) * 5

    def sixes(self, dice_list):
        return self.count_dice(dice_list, 6) * 6

    # Unterer Teil
    def three_of_a_kind(self, dice_list):
        for i in range(1, 7):
            if self.count_dice(dice_list, i) >= 3:
                return self.sum_all_dice(dice_list)
        return 0

    def four_of_a_kind(self, dice_list):
        for i in range(1, 7):
            if self.count_dice(dice_list, i) >= 4:
                return self.sum_all_dice(dice_list)
        return 0

    def full_house(self, dice_list):
        has_three = False
        has_two = False
        for i in range(1, 7):
            count = self.count_dice(dice_list, i)
            if count == 3:
                has_three = True
            if count == 2:
                has_two = True
        if has_three and has_two:
            return 25
        return 0

    def small_straight(self, dice_list):
        values = sorted(set([d.value for d in dice_list]))
        straights = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
        for straight in straights:
            if all(num in values for num in straight):
                return 30
        return 0

    def large_straight(self, dice_list):
        values = sorted(set([d.value for d in dice_list]))
        if values == [1,2,3,4,5] or values == [2,3,4,5,6]:
            return 40
        return 0

    def kniffel(self, dice_list):
        for i in range(1, 7):
            if self.count_dice(dice_list, i) == 5:
                return 50
        return 0

    def chance(self, dice_list):
        return self.sum_all_dice(dice_list)