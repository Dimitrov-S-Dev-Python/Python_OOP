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
                elif board.check_is_game_over(player, player_move):
                    print("Awesome. You won the game!")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("Oops. The computer won!")
                        break

            play_again = input("Would u like to play again? Y/ N")
            if play_again == "N":
                print("Thank you!")
                break
            elif play_again == "Y":
                self.start_new_round(board)
            else:
                print("Your input was not valid, I guess u mean to continue.")
                self.start_new_round(board)

    def start_new_round(self, board):
        print("**************************")
        print("New Round")
        print("**************************")
        board.reset_board()
        board.print_board()
