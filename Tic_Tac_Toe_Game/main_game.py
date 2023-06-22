from board import Board
from player import Player


class TicTacToeGame:

    def start(self):
        print("******************************")
        print(" Welcome to Tic - Tac - Toe ")
        print("******************************")

    board = Board()
    player = Player()
    computer = Player(False)

    board.print_board()
    #  Ask user to play another round

    while True:
        # Game logic

        while True:
            player_move = player.get_move()
            board.submit_move(player, player_move)
            board.print_board()

            if board.check_is_tie():
                print("It is tie! Try again")
                break
            elif board.check_is_game_over(player, player_move)
                print("Awesome. You won the game!")
                break
            else:
                computer_move = computer.get_move()
                board.submit_move((computer, computer_move))
                board.print_board()

                if board.check_is_game_over(computer,computer_move):
                    print("Ooops. The computer won!")
                    break