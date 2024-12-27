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
        self._run_menu()

    def _run_menu(self):
        while self.board == None:
            self._print_menu()
            board_option = input()

            if board_option not in {"1", "2"}:
                continue

            dimension = self._get_int("Enter board dimension:")
            self._execute_option(board_option, dimension)

        self._play_game()

    def _print_menu(self):
        print("  1: Generate a new board")
        print("  2: Load a custom board")
        print(">>>", end=" ")

    def _execute_option(self, board_option, dimension):
        if board_option == "1":
            self._generate_board(dimension)
        else:
            print("  Enter the board, separating the die by spaces:")
            self._load_board(dimension)

    def _load_board(self, dim: int):
        self.board = Board(dim, True)

    def _generate_board(self, dim: int):
        self.board = Board(dim)

    def _get_int(self, command: str) -> int:
        num = input(f"  {command} ")
        while True:
            try:
                num = int(num)

                if num > 0:
                    return num
                else:
                    raise ValueError

            except ValueError:
                num = input(f"  Enter a whole number: ")

    def _play_game(self):
        timer = self._get_int("How many minutes will your game be?") * 60

        while timer > 0:
            print(self.board)
            self._print_timer(timer)

            start_input = perf_counter()
            word = timedInput(prompt=">>> ", timeout=1)
            finish_input = perf_counter()

            self.solutions.add(word)
            timer -= finish_input - start_input

            self._clear_board()

        self._print_solution()

    def _clear_board(self):
        for _ in range(self.board.BOARD_DIM + 5):
            print(CLEAR_LINE, end="")

    def _print_timer(self, timer):
        mins_remaining = int(timer // 60)
        secs_remaining = int(timer % 60)

        if secs_remaining < 10:
            secs_remaining = f"0{secs_remaining}"

        print(f"{mins_remaining}:{secs_remaining}")

    def _print_solution(self):
        solver = Solver(self.board, words=set())
        solver.solve_board()
        solver.print_results()


if __name__ == "__main__":
    Game()
