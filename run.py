from board import Board
from engine import find_best_move


def print_devider():
    print("------------")


if __name__ == "__main__":
    board = Board(grid_size=3)
    board.turn = 1

    # Main loop
    while board.open_cells:
        print_devider()
        print(board)

        # Human move
        if board.turn == 1:
            while True:
                try:
                    str_point = input("Point: ")
                    x, y = map(int, str_point.split(","))
                    board.place_tick_tack(x, y)
                    break
                except ValueError as e:
                    print(e)

        # Computer move
        else:
            (x, y), score = find_best_move(board, 6)
            board.place_tick_tack(x, y)
            if score == 1:
                print("The computer is winning!")
            if score == 0:
                print("Looks like a draw")
            if score == -1:
                print("You are winning!")

        # Someone won
        if board.check_winner():
            print_devider()
            print(board)
            if board.turn == 2:
                print("Human won!")
            if board.turn == 1:
                print("The computer won!")
            break

    # Its a draw
    else:
        print_devider()
        print(board)
        print("Draw!")
