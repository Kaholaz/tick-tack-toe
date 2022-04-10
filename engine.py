from board import Board


def find_best_move(board: Board, depth=-1) -> tuple[tuple[int, int], int]:
    if board.check_winner():
        return (-1, -1), -1

    if not board.open_cells or depth == 0:
        return (-1, -1), 0

    best_cell, best_score = (-1, -1), 2
    for cell in board.open_cells:
        board_copy = board.copy()
        board_copy.place_tick_tack(*cell)
        _, score = find_best_move(board_copy, depth - 1)
        if score == -1:
            return cell, -score
        if score < best_score:
            best_cell, best_score = cell, score

    return best_cell, -best_score
