from board import Board
from solver import Solver
from pytimedinput import timedInput
from time import perf_counter

CLEAR_LINE = "\033[A\033[K"


class Game:
    def __init__(self):
        print("Welcome to Boggle! Enter a number to proceed:")

        self.board = None
        self.solutions = set()

    def run(self):
        while self.board == None:
            self.__print_menu()
            board_option = ""

            while board_option not in {"1", "2"}:
                board_option = input(">>> ")

            dimension = self.__get_int("Board dimension?")
            self.__execute_option(board_option, dimension)

        self.__play_game()

    def __print_menu(self):
        print("  1: Generate a new board")
        print("  2: Load a custom board")

    def __execute_option(self, board_option, dimension):
        if board_option == "1":
            self.__generate_board(dimension)
        else:
            print("  Enter the board, separating the die by spaces:")
            self.__load_board(dimension)

    def __load_board(self, dim: int):
        self.board = Board(dim, True)

    def __generate_board(self, dim: int):
        self.board = Board(dim)

    def __get_int(self, command: str) -> int:
        num = input(f"  {command} ")
        while True:
            try:
                num = int(num)

                if num > 0:
                    if num > 25:
                        raise ValueError("Choose a smaller number:")
                    return num
                else:
                    raise ValueError("Enter a whole number:")

            except ValueError as e:
                num = input(f"  {e} ")

    def __play_game(self):
        timer = self.__get_int("How many minutes will your game be?") * 60
        print("\n  (Enter 'r' to rotate the board clockwise)")

        while timer > 0:
            start_input = perf_counter()

            print(self.board)
            self.__print_timer(timer)
            word, _ = timedInput(prompt=">>> ", timeout=2)
            self.__process_word(word)
            self.__clear_board()
            finish_input = perf_counter()
            timer -= finish_input - start_input

        self.__print_results()

    def __print_timer(self, timer: float):
        mins_remaining = int(timer // 60)
        secs_remaining = int(timer % 60)

        if secs_remaining < 10:
            secs_remaining = f"0{secs_remaining}"

        print(f"{mins_remaining}:{secs_remaining}")

    def __process_word(self, word: str):
        if word:
            if word.lower() == "r":
                self.board.rotate_board()
            else:
                self.solutions.add(word.upper())

    def __clear_board(self):
        for _ in range(self.board.BOARD_DIM + 6):
            print(CLEAR_LINE, end="")

    def __print_results(self):
        solver = Solver(self.board, words=set())
        solver.solve_board()

        print(self.board)
        print("You got these words:")
        print(f"  {solver.words.intersection(self.solutions)}")

        print("You missed these words:")
        print(f"  {solver.words.difference(self.solutions)}")


if __name__ == "__main__":
    game = Game()
    game.run()
