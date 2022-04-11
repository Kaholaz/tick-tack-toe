from board import Board


def find_best_move(board: Board, depth=-1) -> tuple[tuple[int, int], int]:
    """
    Finds the best move by an exaustive depth-first reccursive search
    """
    # If there is a winner, the previous mover won (this gives a score of -1)
    if board.check_winner():
        return (-1, -1), -1

    # If there is no winner, and there are no more cells, it's a draw.
    # If there is no more depth, 0 is returned (draw evaluation).
    if not board.open_cells or depth == 0:
        return (-1, -1), 0

    # The best move should be the worst move for the next player
    # (the one with the lowest score)
    best_cell, best_score = (-1, -1), 2
    for cell in board.open_cells:
        board_copy = board.copy()
        board_copy.place_tick_tack(*cell)
        _, score = find_best_move(board_copy, depth - 1)
        if score == -1:  # Forced win. This is the best move regardless.
            return cell, -score
        if score < best_score:
            best_cell, best_score = cell, score

    return best_cell, -best_score
