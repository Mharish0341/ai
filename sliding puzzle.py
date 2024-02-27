import random

class SlidingPuzzle:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.empty_pos = (2, 2)
        self.shuffle()

    def shuffle(self):
        numbers = list(range(1, 9))
        random.shuffle(numbers)
        for i in range(3):
            for j in range(3):
                if i == 2 and j == 2:
                    self.board[i][j] = 0
                else:
                    self.board[i][j] = numbers.pop()
        self.empty_pos = (2, 2)

    def print_board(self):
        for row in self.board:
            print(" | ".join(str(num) if num != 0 else " " for num in row))
            print("-" * 9)

    def get_move(self):
        while True:
            move = input("Enter a move (W/A/S/D to move up/left/down/right, Q to quit): ").upper()
            if move in ['W', 'A', 'S', 'D', 'Q']:
                return move
            else:
                print("Invalid move! Please enter W, A, S, D, or Q.")

    def move_tile(self, move):
        dx, dy = 0, 0
        if move == 'W':
            dx, dy = -1, 0
        elif move == 'A':
            dx, dy = 0, -1
        elif move == 'S':
            dx, dy = 1, 0
        elif move == 'D':
            dx, dy = 0, 1

        new_x, new_y = self.empty_pos[0] + dx, self.empty_pos[1] + dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            self.board[self.empty_pos[0]][self.empty_pos[1]] = self.board[new_x][new_y]
            self.board[new_x][new_y] = 0
            self.empty_pos = (new_x, new_y)
        else:
            print("Invalid move! Please try again.")

    def is_solved(self):
        return all(self.board[i][j] == i * 3 + j + 1 for i in range(3) for j in range(3)) and self.board[2][2] == 0

    def play(self):
        while not self.is_solved():
            self.print_board()
            move = self.get_move()
            if move == 'Q':
                print("Quitting game.")
                break
            self.move_tile(move)

        if self.is_solved():
            print("Congratulations! You solved the puzzle.")

if __name__ == "__main__":
    game = SlidingPuzzle()
    game.play()
