import pygame

class Game:
    def __init__(self, window_obj, Player):
        # --- Attribute (Mittlerer Kasten) ---
        # + player: list[Player]
        self.player 
        
        # + count_turns: int
        self.count_turns: int = 0      
        
        # + window: window (Wahrscheinlich ein pygame display/surface)
        self.window = window_obj       

    def game_won(self, players) -> None:
        pass

    # + play_turn(): void
    def play_turn(self) -> None:
        pass

    # + quit: bool (Im Diagramm fehlen die Klammern, aber es ist eine Methode)
    def quit(self) -> bool:
        pass