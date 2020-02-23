from minesweeper.Board import Board

if __name__ == "__main__":
    difficulty = input("Enter difficulty (easy, medium, hard): ")

    difficulty = "easy" if difficulty == "" else difficulty
    if difficulty not in ["easy", "medium", "hard"]:
        raise ValueError

    board = Board(difficulty)

    board.play()

