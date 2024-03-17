class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print(f'| {" | ".join(self.board[i:i+3])} |')
            if i < 6:
                print('|---+---+---|')

    def is_move_valid(self, position):
        return 1 <= position <= 9 and self.board[position - 1] == ' '

    def make_move(self, position):
        if self.is_move_valid(position):
            self.board[position - 1] = self.current_player
            if self.check_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                return True
            elif ' ' not in self.board:
                self.print_board()
                print("It's a draw!")
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move! Try again.")
        return False

    def check_winner(self, player):

        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                return True

        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player:
                return True

        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True

        return False

    def play_game(self):
        while True:
            self.print_board()
            position = input(f"Player {self.current_player}, enter a position (1-9): ")
            try:
                position = int(position)
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue
            if self.make_move(position):
                break

game = TicTacToe()
game.play_game()