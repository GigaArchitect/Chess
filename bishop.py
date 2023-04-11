pos_letters = ['a','b','c','d','e','f','g','h']
class bishop :
    def __init__(self,color,position) :
        self.color = str(color)
        self.position = position

    def move(self,current_pos):
        moves = []
        ch = current_pos[0]
        nm = int(current_pos[1])
        for i in range(9):
            if pos_letters.index(ch)+i > 7 or nm+i > 8 :
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)+i]}{nm+i}")
        for i in range(9):
            if pos_letters.index(ch)-i < 0 or nm-i < 1 :
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)-i]}{nm-i}")
        for i in range(9):
            if pos_letters.index(ch)+i > 7 or nm-i < 1 :
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)+i]}{nm-i}")
        for i in range(9):
            if pos_letters.index(ch)-i < 0 or nm+i > 8 :
                continue
            moves.append(f"{pos_letters[pos_letters.index(ch)-i]}{nm+i}")
        return moves
