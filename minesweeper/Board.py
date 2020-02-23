import pandas as pd
import random as rand

class Board:
    def __init__(self, difficulty = 'easy'):
        if difficulty == 'easy':
            size = 9
            self._bomb_locs = set()
            self._size = size
            self._real_board = pd.DataFrame([[' ' for _ in range(size)] for _ in range(size)])

    def get_bombs(self):
        bomb_locs = set()
        while len(bomb_locs) < 9:
            loc = (rand.randint(0, 8), rand.randint(0, 8))
            if loc not in bomb_locs:
                bomb_locs.add(loc)
        self._bomb_locs = bomb_locs

    def show_board(self):
        print(self._real_board)

    def is_gameover(self, x, y):
        if (x, y) in self._bomb_locs:
            return True

    def place_bombs(self):
        for x, y in self._bomb_locs:
            self._real_board[x][y] = "*"

    def get_coords(self):
        coords = input("Please Enter comma separated coordiants:")
        if coords == "cheat":
            print(self._bomb_locs)
            return self.get_coords()
        else:
            return (int(coord.strip()) for coord in coords.split(","))

    def play(self):
        self.get_bombs()
        self.show_board()
        while True:
            x, y = self.get_coords()
            if self.is_gameover(x, y):
                print("Game Over. You have selected a bomb")
                self.place_bombs()
                self.show_board()
                break
            self._real_board[x][y] = "-"
            self.show_board()