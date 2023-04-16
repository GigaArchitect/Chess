pos_letters = ['a','b','c','d','e','f','g','h']
class Rook :
    def __init__(self,color,position) :
        self.color = str(color)
        self.position = position
        self.moved = 0

    def __repr__(self) -> str:
        if self.color == "b":
            return "rr"
        else:
            return "R"

    def move(self,current_pos):
        moves = []
        ch = current_pos[0]
        nm = int(current_pos[1])
        if self.moved == 0 :
            print(f"king will be {pos_letters[pos_letters.index(ch)-1]}{nm}")
            print("rook will be kingchar+1")
            self.moved = 1
            
        else :
            #Forward
            for i in range(9):
                if nm + i > 8 :
                    continue
                moves.append(f"{pos_letters[pos_letters.index(ch)]}{nm+i}")
            #Back
            for i in range(9):
                if nm - i < 1 :
                    continue
                moves.append(f"{pos_letters[pos_letters.index(ch)]}{nm-i}")
            #Right
            for i in range(9):
                if pos_letters.index(ch)+i > 7 :
                    continue
                moves.append(f"{pos_letters[pos_letters.index(ch)+i]}{nm}")
            #left
            for i in range(9):
                if pos_letters.index(ch)+i < 0 :
                    continue
                moves.append(f"{pos_letters[pos_letters.index(ch)-i]}{nm}")

        return moves

