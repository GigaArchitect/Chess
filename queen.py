pos_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]


class Queen:
    def __init__(self, color, position):
        self.color = str(color)
        self.position = position

    def __repr__(self) -> str:
        if self.color == "b":
            return "q"
        else:
            return "Q"

    def move(self, current_pos):
        moves = []
        ch = current_pos[0]
        nm = int(current_pos[1])
        # Bishop Moves
        for i in range(9):
            if pos_letters.index(ch) + i > 7 or nm + i > 8:
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)+i]}{nm+i}")
        for i in range(9):
            if pos_letters.index(ch) - i < 0 or nm - i < 1:
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)-i]}{nm-i}")
        for i in range(9):
            if pos_letters.index(ch) + i > 7 or nm - i < 1:
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)+i]}{nm-i}")
        for i in range(9):
            if pos_letters.index(ch) - i < 0 or nm + i > 8:
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)-i]}{nm+i}")
        # rook moves
        # Forward
        for i in range(9):
            if nm + i > 8:
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)]}{nm+i}")
            # Back
        for i in range(9):
            if nm - i < 1:
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)]}{nm-i}")
            # Right
        for i in range(9):
            if pos_letters.index(ch) + i > 7:
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)+i]}{nm}")
            # left
        for i in range(9):
            if pos_letters.index(ch) + i < 0:
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)-i]}{nm}")

        return moves

    def draw(self):
        if self.color == "w":
            return "white_queen"
        return "black_queen"
