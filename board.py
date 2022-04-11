class Board:
    def __init__(self, grid_size=3) -> None:
        """
        Creates a new instance of the board class.

        The grid_size determines the size of the grid. If grid_size fore example is 3,
        a 3x3 grid is constructed.
        """
        self.grid_size = grid_size
        self.reset_grid()
        self.turn: int = 1

    def reset_grid(self) -> None:
        """
        Resets and clears the board.
        """
        self._grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.open_cells = {
            (x, y) for x in range(self.grid_size) for y in range(self.grid_size)
        }

    def place_tick_tack(self, x: int, y: int) -> None:
        """
        Places an 'X' or 'O' on the board at the given coordinates based on whos turn it is.
        0,0 is the corner at the top left. The first coordinate increases the column number,
        while the second corner increases the row number.

        :throws ValueError: Throws an exception if the cell is out of bounds, or the square
        already is occupied.
        """
        if x not in range(self.grid_size) or y not in range(self.grid_size):
            raise ValueError("Cell out of bounds")

        if (x, y) not in self.open_cells:
            raise ValueError("This square is already occupied")

        self._grid[y][x] = self.turn
        self.open_cells.remove((x, y))

        # Advance the turn
        self.turn = (self.turn % 2) + 1

    def check_winner(self) -> int:
        """
        Checks for a filled row, column or diagonal
        of placed "tick-tacs".

        If the algorithm finds a filled row, column or diagonal,
        a the number of the player that owns the cells is returned (1 or 2).

        If no filled row, column or diagonal is found, 0 is returned.
        """

        # Checks rows
        for row in range(self.grid_size):
            # If the cell is empty
            if not self._grid[row][0]:
                continue

            # If the set has lenght 1, ther is only one unique element
            if len(set(self._grid[row])) == 1:
                return self._grid[row][0]

        # Checks columns
        for col in range(self.grid_size):
            if not self._grid[0][col]:
                continue

            if len(set(row[col] for row in self._grid)) == 1:
                return self._grid[0][col]

        # Left to right diagonal
        if self._grid[0][0]:
            if len(set(self._grid[i][i] for i in range(self.grid_size))) == 1:
                return self._grid[0][0]

        # Right to left diagonal
        if self._grid[-1][0]:
            if len(set(self._grid[-i - 1][i] for i in range(self.grid_size))) == 1:
                return self._grid[-1][0]

        return 0

    def copy(self) -> "Board":
        """
        Creates a new instance with the exact same state.
        """
        new_board = Board()

        new_board._grid = [[cell for cell in row] for row in self._grid]
        new_board.open_cells = set(self.open_cells)
        new_board.turn = self.turn
        new_board.grid_size = self.grid_size

        return new_board

    def __str__(self) -> str:
        symbols = [" ", "X", "O"]
        out = ""
        for row in self._grid:
            for cell in row:
                out += symbols[cell] + "  "
            out += "\n"

        return out
